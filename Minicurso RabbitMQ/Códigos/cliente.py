#!/usr/bin/env python
import pika#biblioteca para fazer a conexao entre cliente e servidor
import uuid#biblioteca util para gerar o id da solicitacacao

class Operacao_cliente(object):

    def __init__(self):
        credentials = pika.PlainCredentials('usuario', 'senha')
        parameters = pika.ConnectionParameters('192.168.1.9',
                                        5672,
                                        '/',
                                        credentials)

        self.connection = pika.BlockingConnection(parameters)

        self.channel = self.connection.channel()

        
        #Conexão para ser possível obter a respota do servidor
        #result = self.channel.queue_declare(queue='', durable=True)
        result = self.channel.queue_declare(queue='', exclusive=True)

        #Assinamos a callback_queue , para que possamos receber respostas do Remote Procedure Call (RPC)
        self.callback_queue = result.method.queue 

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)
        #Função que eh executada em cada resposta do servidor
        #Para cada mensagem de resposta ela verifica se a correlacao_id eh a que estamos procurando.Nesse caso, salva a resposta em self.response e interrompe o consumo

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

        #Método de chamada principal - ele faz a solicitação RPC real
    def call(self, n):
        self.response = None
        #geração de um número de correlacao_id unico( será utilizado pela função de retorno de chamada on_response para capturar a resposta apropriada)

        self.corr_id = str(uuid.uuid4()) 
        self.channel.basic_publish(# Ocorre a publicação da mensagem de solicitação com duas propriedades o o correlacao_id e o reply_to(campo que possui uma fila que será utilizada para transmitir a resposta do serv para client)

            exchange='',
            routing_key='rpc_queue',#faz a vinculação com a fila para que seja possível a exchange coloque mensagens nessa fila
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=n)
        #Espera até que a resposta adequada chegue e depois disso devolve a resposta ao usuário.
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

#Função que contém as operações criar conexao client-serv,criacao e assinatura da callback,craicao do canal de comunicacao,recepcao da resposta do servidor e envio de solicitacao ao servidor
operacao_rpc = Operacao_cliente()
#menu para escolha de opcoes
print("Escolha uma opcao:")
#separacao de numeros da entrada
entrada =input("1-Soma 2-Subtracao 3-Multiplicacao 4-divisao\n")
entrada+="-"
entrada+=input("Digite o 1º valor\n")
entrada+="-"
entrada+=input("Digite o 2º valor\n")
#chamada da funcao que contata o servidor para o calculo
response = operacao_rpc.call(entrada)
print(" [.] Got %r" % response)