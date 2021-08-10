import os
import psycopg2


nome = None
cpf = None
registro = None
email = None
telefone = None
endereco = None

class oferta:
    global tipo 
    global valor
    global prazo 
    global risco 
    global segmento_mercado 
    def __init__(self,tipo,valor,prazo,risco,segmento_mercado):
        self.tipo = tipo
        self.valor = valor
        self.prazo = prazo
        self.risco = risco
        self.segmento_mercado = segmento_mercado


def insereBanco(conn,cmd,oferta):
    sql = "insert into analista(nome,cpf,registro,email,telefone,endereco) values('"+nome+"','"
    sql += cpf+"','"
    sql += registro
    sql += "','"+email+"','"+telefone
    sql += "','"+ endereco
    sql += "');\n"
    print(sql)
    cmd.execute(sql)

     
    sql = "insert into oferta(tipo,valor,prazo,risco,segmento,analista_cpf) values('"+oferta.tipo+"','"
    sql += oferta.valor+"','"
    sql += oferta.prazo
    sql += "','"+oferta.risco+"','"+oferta.segmento_mercado
    sql += "','" + cpf + "');\n"
    print(sql)
    cmd.execute(sql)

def menu(conn,cmd):
    global nome 
    global cpf
    global registro 
    global email 
    global telefone 
    global endereco 
    print("Dados do analista")
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    registro = input("Digite o CVM: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    endereco = input("Digite o endereco: ")

    os.system('cls' if os.name == 'nt' else 'clearprint("")')
    print("Dados da oferta")

    tipo = input("Digite o tipo: ")
    valor = input("Digite o valor: ") 
    prazo = input("Digte o prazo: ")
    risco = input("Digite o risco: ")
    segmento_mercado = input("Digite o segmento de mercado: ")

    novaOferta = oferta(tipo,valor,prazo,risco,segmento_mercado)
    
    insereBanco(conn,cmd,novaOferta)
    


def main():
    conn = psycopg2.connect(host="localhost", dbname='Corretora', user='postgres', password='root')
    conn.autocommit = True
    cmd = conn.cursor()


    menu(conn ,cmd)

main()

