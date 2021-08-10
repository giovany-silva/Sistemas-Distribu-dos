import pika
import sys
import os

def inscrever():
    print("Informe suas preferências")
    tipo = input("Tipo de investimento {Renda fixa, Acao, Fundo Imobiliario, Criptomoeda}: ")
    prazo = input("Informe o prazo do investimento da sua preferência {Curto, Medio, Longo}: ")
    risco = input("Informe o risco de investimento da sua preferência {Baixo, Alto}: ")
    segmento = input("Informe o segmento de investimento da sua preferência {Mineracao, Bancario, Energia, Alimenticio, Agricola}: ")
  
    
    preferencias = tipo + "\n" + prazo + "\n" + risco + "\n" + segmento

    os.system('cls' if os.name == 'nt' else 'clear')
    f = open("preferencias.txt", "a")
    f.write("\n")
    f.write(preferencias)
    f.close()

def desinscrever():
  f = open("preferencias.txt", "r")
  preferencias = f.readlines()
  lista = []
  print("Escolhe o tópico a remover:")
  for preferencia in preferencias:
      lista.append(preferencia.replace("\n",""))

  lista_dif = set(lista)

  try:
      lista_dif.remove("\n")
  except:
      print()
  
  for dado in lista_dif:
      print(dado)      

  topico = input()    
      
  lista_dif.remove(topico)   

  f.close()
  f = open("preferencias.txt", "w")
  for topico in lista_dif:
      f.write(topico+"\n")
  f.close()
def associa_topico():
  f = open("preferencias.txt", "r")

  preferencias = f.readlines()

  for i in range(len(preferencias)):
    preferencias[i] = preferencias[i].replace("\n","") 
  
  connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
  
  channel = connection.channel()

  channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

  result = channel.queue_declare('', exclusive=True)
  queue_name = result.method.queue

  binding_keys = preferencias

  for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key
    )

  print(' [*] Esperando por ofertas\n')
  
  channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

  channel.start_consuming()


def callback(ch, method, properties, body):
#    resultado = str(body).replace("b\"","").replace("\"","")
#    print(" [x] %r:%r" % (resultado))
#print(" [x] %r:%r" % (method.routing_key, body))
    if(body is not None):
        print(" [x] %r" % ( body))
    ch.stop_consuming()
    


def main():

  opcao = 1
  while opcao !=3:
      print("Escolha uma opção:")
      print("1- Inscrever em tópico")
      print("2- Desinscrever em algum tópico")
      print("3 - Receber ofertas")
      print("4 - Sair")
      opcao = input()

      if opcao =="1":
          inscrever()
          associa_topico()
          
      elif opcao == "2":
          desinscrever()
          associa_topico()
      elif opcao == "3":
          associa_topico()
      else:
          break
    
main()
