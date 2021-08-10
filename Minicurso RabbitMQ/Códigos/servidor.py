#!/usr/bin/env python
import pika

#define a conexao utilizando a biblioteca do Python
credentials = pika.PlainCredentials('usuario', 'senha')
parameters = pika.ConnectionParameters('192.168.56.1',
                                   5672,
                                   '/',
                                   credentials)
connection = pika.BlockingConnection (parameters)

#connection = pika.BlockingConnection(
#   pika.ConnectionParameters(host='localhost'))

#cria canal de conexao
channel = connection.channel()

#estabelece a conexão e declara a fila 'rpc_queue'
channel.queue_declare(queue='rpc_queue')

#operacao de soma
def soma(a,b):
    return int(a)+int(b)

#operacao de subtracao
def sub(a,b):
    return int(a)-int(b)

#operacao de multiplicacao
def mult(a,b):
    return int(a)*int(b)

#operacao de divisao
def div(a,b):
    return int(int(a)/int(b))

#funcao de retorno para o cliente
#é executada quando a solicitacao é recebida
#realiza a operacao e devolve o valor para o cliente
def on_request(ch, method, props, body):
    resposta_cliente = str(body)
    resposta_cliente = resposta_cliente.replace("b", "")
    resposta_cliente = resposta_cliente.replace("'", "")

    #pega a opcao digitada pelo cliente
    opcao =  resposta_cliente.split("-")[0]
   
    #seta response como 0
    response = 0
    # pega o primeiro e segundo numero
    a =  resposta_cliente.split("-")[1]
    b =  resposta_cliente.split("-")[2]

    #se a opcao for 1 faz soma, printa a operacao #escolhida e os digitos
    if(opcao == "1"):
        response = soma(a,b)
        print("\n [.] soma("+str(a)+","+str(b)+")")

    #se a opcao for 2 faz subtracao, printa a operacao #escolhida e os digitos
    elif(opcao == "2"):
        response = sub(a,b)
        print("\n [.] subtracao("+str(a)+","+str(b)+")")
    
    #se a opcao for 3 faz multiplicacao, printa a #operacao escolhida e os digitos
    elif(opcao == "3"):
        response = mult(a,b)
        print("\n [.] multiplicacao("+str(a)+","+str(b)+")")

    #se a opcao for 4 faz divisao, printa a operacao #escolhida e os digitos
    elif(opcao == "4"):
        response = div(a,b)
        print("\n [.] divisao("+str(a)+","+str(b)+")")   


    #método para saber para onde enviar a resposta:
    #fila do campo reply_to
    #correlation_id tem valor unico para cada solicitacao
    #com isso, pode-se corresponder uma resposta a uma #solicitacao
    #basic_publish publica a resposta passando o reply_to
    #e correlation_id
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))

    #Quando enviado pelo servidor, este método reconhece uma ou mais mensagens publicadas com o #método Publish em um canal em modo de confirmação
    ch.basic_ack(delivery_tag=method.delivery_tag)

#prefetch_count é o numero de processos por servidor
channel.basic_qos(prefetch_count=1)

#Este método pede ao servidor para iniciar um #"consumidor", que é um pedido transitório de #mensagens de uma fila específica. Os consumidores duram tanto #quanto o canal em que foram #declarados ou até que o cliente os cancele.
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print("[x] Esperando requisições")

#comeca escutar o cliente a partir do start_consuming 
channel.start_consuming()