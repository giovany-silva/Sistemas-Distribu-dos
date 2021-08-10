import pika
import psycopg2
import time
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

  
preferencias_tipo = {'Renda fixa', 'Ação', 'Fundo Imobiliário', 'Criptomoeda'}
  
preferencias_prazo = {'Curto', 'Médio', 'Longo'}
  
preferencias_risco = {'Baixo', 'Alto'} 
  
preferencias_segmento = {'Mineração', 'Bancário', 'Energia', 'Alimentício', 'Agrícola'}

second_time = time.time()+10

def runBroker():
    global second_time

    while True :
        if time.time() < second_time:
          continue

        else:
          second_time = time.time() + 10
     
        conn = psycopg2.connect(host="localhost", dbname='Corretora', user='postgres', password='root')
        conn.autocommit = True
        cmd = conn.cursor()

           
        for preferencia in preferencias_tipo:
          sql = "select * from oferta where tipo = '"+ preferencia + "'"
          cmd.execute(sql)

          retorno = cmd.fetchall()
          if(retorno == []):
              continue
          message = str(retorno)
             
          channel.basic_publish(
            exchange='topic_logs', routing_key = preferencia, body = message
          )
          print(" {x} Enviando ofertas %r:%r" % (preferencia, message))
          
        for preferencia in preferencias_prazo:
          sql = "select * from oferta where prazo = '"+ preferencia + "'"
          cmd.execute(sql)
          
          
          retorno = cmd.fetchall()
          if(retorno == []):
              continue

          message = str(retorno)
          

          channel.basic_publish(
            exchange='topic_logs', routing_key = preferencia, body = message
          )
          print(" {x} Enviando ofertas %r:%r" % (preferencia, message))
          
        for preferencia in preferencias_risco:
          sql = "select * from oferta where risco = '"+ preferencia + "'"
          cmd.execute(sql)

          retorno = cmd.fetchall()
          if(retorno == []):
              continue
          message = str(retorno)
          
          
          channel.basic_publish(
            exchange='topic_logs', routing_key = preferencia, body = message
          )
          print(" {x} Enviando ofertas %r:%r" % (preferencia, message))
          
        for preferencia in preferencias_segmento:
          sql = "select * from oferta where segmento = '"+ preferencia + "'"
          cmd.execute(sql)

          retorno = cmd.fetchall()
          if(retorno == []):
              continue
          message = str(retorno)
          

          channel.basic_publish(
            exchange='topic_logs', routing_key = preferencia, body = message
          )
          print(" {x} Enviando ofertas %r:%r" % (preferencia, message))
          
def main():
    runBroker()
main()

#connection.close()

