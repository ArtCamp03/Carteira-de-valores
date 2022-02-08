from dataclasses import dataclass
import datetime
import mysql.connector
from mysql.connector import errorcode

cnx = None

def conectar():
    # schema mywallet 
    
    try:
        cnx = mysql.connector.connect(user='root', password='123456', host='localhost', database='mywallet')
        print('conexao estabelecida')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Algo errado com usuario ou senha')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Banco de dados nao existe')
        else:
            print(err)
    return cnx

def ConfirmaLogin(nome,senha):
    cnx = conectar()
    cursor = cnx.cursor()
    flag = False
    consultaCLI = ("SELECT Nome, CPF FROM cliente ")
    cursor.execute(consultaCLI)
    for (Nome ,CPF) in cursor:
        if Nome == nome and CPF == senha:
            flag = True

    cursor.close()
    cnx.close()

    return flag

# INSERE DADOS
def InsereCliente(Nome ,Data_Nascimento ,CPF):
    cnx = conectar()
    cursor = cnx.cursor()
    add_consultaCLI = ("INSERT INTO cliente(Nome ,Data_Nascimento ,CPF ) VALUES (%s,%s, %s)")
    dadosCliente = (Nome ,Data_Nascimento ,CPF )
    cursor.execute(add_consultaCLI, dadosCliente)
    print('Insercao concluida !')
    
    cnx.commit()
    cursor.close()
    cnx.close()

    return True


def recupera_Deposito(cpf):
    cnx = conectar()
    cursor = cnx.cursor()
    flag = False
    consultaCLI = ("SELECT CPF,Invest_Total_Atual ,Lucro_Total FROM cliente ")
    cursor.execute(consultaCLI)
    for (CPF, Invest_Total_Atual ,Lucro_Total) in cursor:
        if CPF == cpf:
            valor = (CPF,Invest_Total_Atual ,Lucro_Total)

    cursor.close()
    cnx.close()
    return valor

def dados_conta(cpf):
    cnx = conectar()
    cursor = cnx.cursor()
    flag = False
    consultaCLI = ("SELECT Nome ,Data_Nascimento ,CPF FROM cliente ")
    cursor.execute(consultaCLI)
    for (Nome ,Data_Nascimento ,CPF) in cursor:
        if CPF == cpf:
            valor = (Nome ,Data_Nascimento ,CPF)

    cursor.close()
    cnx.close()
    return valor

#def Empresa():

#def transacao():

# CARREGA DADOS
#ClienteTable()

def consultaEMP(tick):
    cnx = conectar()
    cursor = cnx.cursor()
    flag = False
    consultaEmp = ("SELECT Ticker, Nome, Setor_Atuante FROM empresa")
    cursor.execute(consultaEmp)
    for (Ticker, Nome, Setor_Atuant) in cursor:
        if Ticker == tick:
            valor = (Ticker, Nome, Setor_Atuant)

    cursor.close()
    cnx.close()
    return valor

def consultaTRANS(id):
    cnx = conectar()
    cursor = cnx.cursor()
    flag = False
    consultaEmp = ("SELECT ID, Tipo, Empresa,Data_Negociada ,Corretora ,N_Acoes ,Cotacao FROM empresa")
    cursor.execute(consultaEmp)
    for (ID, Tipo, Empresa,Data_Negociada ,Corretora ,N_Acoes ,Cotacao) in cursor:
        if ID == id:
            valor = (ID, Tipo, Empresa,Data_Negociada ,Corretora ,N_Acoes ,Cotacao)

    cursor.close()
    cnx.close()
    return valor

def AlteraCliente(usuario,dataNesc,cpf,cpfAntigo):
    cnx = conectar()
    cursor = cnx.cursor()
    flag = False
    alteraTabela = ("UPDATE cliente SET  Nome = {} ,Data_Nascimento = {} ,CPF = {} WHERE cliente.CPF = {}".format(usuario,dataNesc,cpf,cpfAntigo))
    cursor.execute(alteraTabela)
    for (Nome,Data_Nascimento, CPF ) in cursor:
        val = (Nome,Data_Nascimento, CPF)
    
    cnx.commit()
    cursor.close()
    cnx.close()

    return val


print("dados carregados!! \n")