from tkinter import Button
from PySimpleGUI import PySimpleGUI as sg
from numpy import size 
import banco as bd

# janela Login
def janelaLogin():
    # tema
    sg.theme('Dark Grey 13')

    layout = [
        [sg.Text('usuario:', size=(20,1))],
        [sg.Input(key= 'usuario', size=(20,15))],
        [sg.Text('CPF:', size=(20,1))],
        [sg.Input(key= 'senha', password_char='*', size=(20,15))],
        [sg.Button('cadastrar'), sg.Button('entrar')]
    ]
    
    return sg.Window('Login My_Wallet', layout=layout, finalize=True)

# janela cadastro
def janelaCadastro():
    # tema
    sg.theme('Reddit')

    layout = [
        [sg.Text('Nome:')],
        [sg.Input(key= 'usuario')],
        [sg.Text('Data Nascimento:')],
        [sg.Input(key= 'data')],
        [sg.Text('CPF:')],
        [sg.Input(key= 'cpf')],
        [sg.Button('cadastrar')]
    ]
    
    return sg.Window('Cadastro My_Wallet', layout=layout, finalize=True)


# menu
def menu():
    sg.theme('Reddit')

    nav = [sg.Button('Geral'), sg.Button('Deposito'),sg.Button('Transacao'),sg.Button('Historico'),sg.Button('Conta')]

    return nav

# janela Geral
def janelaGeral(cpf,lucro_total, porcento):
    # tema
    sg.theme('Reddit')

    linha = [
        [sg.Text('Ativo', size=(10,1)),sg.Text('Preço', size=(10,1)), sg.Text(' % da carteira', size=(10,1)) ],
        [sg.Text('BR3', size=(10,1)),sg.Text('R$ 200,00', size=(10,1)), sg.Text('40%', size=(10,1)) ]
    ]

    soma = lucro_total+porcento
    saldoTotal = [
        [sg.Text('R$ {}'.format(soma), size=(10,1))]
    ]

    valorInvestido = [
        [sg.Text("R$ {}".format(lucro_total), size=(10,1))]
    ]

    lucroTotal = [
        [sg.Text('{} % '.format(porcento), size=(10,1))]
    ]

    layout = [
        [menu()],
        [sg.Frame('Ativos disponiveis:', layout=linha , key=('ativos')), [sg.Frame('Saldo Total:', layout=saldoTotal , key=('sdTotal')),
        sg.Frame('Valor investido:', layout=valorInvestido , key=('valInvest')),
        sg.Frame('Lucro Total:', layout=lucroTotal , key=('lucTotal'))]
        ]
    ]
    
    return sg.Window('Inicio My_Wallet', layout=layout, finalize=True)

# janela deposito
def janelaDeposito():
    # tema
    sg.theme('Reddit')

    valor = [
        [sg.Input('R$ 0,00', key=('val_deposito'))],
        [sg.Button('Sacar'), sg.Button('Depositar')]
    ]

    disponivel =  lucro_total - porcento
    saldoDisponivel = [
        [sg.Text('R$ {}'.format(disponivel), size=(10,1))]
    ]

    valorInvestido = [
        [sg.Text('R$ {}'.format(lucro_total), size=(10,1))]
    ]

    layout = [
        [menu()],
        [sg.Frame('Valor :', layout=valor , key=('valorDP')), [sg.Frame('Saldo Disponivel:', layout=saldoDisponivel , key=('saldoDSP')),
        sg.Frame('Valor investido:', layout=valorInvestido , key=('valInvest'))]
        ]
    ]
    
    return sg.Window('Deposito My_Wallet', layout=layout, finalize=True)


# janela transaçao
def janelaTransacao():
    # tema
    sg.theme('Reddit')

    Ativos = [
        [sg.Text('ID', size=(10,1)),sg.Text('Ativo', size=(10,1)),sg.Text('Empresa', size=(10,1)),sg.Text('Corretora', size=(10,1)), sg.Text('Cotaçao', size=(10,1)), sg.Text('Tipo', size=(10,1)), sg.Text('Nº Açoes', size=(10,1)), sg.Text('Data Negociaçao', size=(15,1)) ],
        [sg.Text('45127', size=(10,1)),sg.Text('BR3',size=(10,1)),sg.Text('BrsailTelecom', size=(10,1)),sg.Text('CLEAR', size=(10,1)),sg.Text('R$ 200,00', size=(10,1)), sg.Text('V', size=(10,1)), sg.Text('3', size=(10,1)), sg.Text('01/01/2022', size=(10,1)) ]
    ]

    saldoDisponivel = [
        [sg.Text('R$ 500,00', size=(10,1))]
    ]

    evento = [
        [sg.Text('BR3',size=(10,1)), sg.Text('Valor unitario',size=(10,1))],
        [sg.Text('  ',size=(10,3)),sg.Text('R$ 500,00',size=(10,3))],
        [sg.Text('Min:',size=(10,1)), sg.Text('Max:',size=(10,1))],
        [sg.Text('R$ 50,00',size=(10,3)), sg.Text('R$ 250,00',size=(10,3))],
        [sg.Button('Compra', size=(10,1)), sg.Button('Venda', size=(10,1))]
    ]

    layout = [
        [menu()],
         [sg.Frame('Ativos :', layout=Ativos , key=('ativosDSP')), [sg.Frame('Saldo Disponivel:', layout=saldoDisponivel , key=('saldoDSP')),
        sg.Frame('Açao', layout=evento , key=('evento'))]
        ]
    ]
    
    return sg.Window('Transaçao My_Wallet', layout=layout, finalize=True)


# janela historico
def janelaHistorico():
    # tema
    sg.theme('Reddit')

    AtivosCompra = [
        [sg.Text('ID', size=(10,1)),sg.Text('Ativo', size=(10,1)),sg.Text('Empresa', size=(10,1)),sg.Text('Corretora', size=(10,1)), sg.Text('Cotaçao', size=(10,1)), sg.Text('Tipo', size=(10,1)), sg.Text('Nº Açoes', size=(10,1)), sg.Text('Data Negociaçao', size=(15,1)) ],
        [sg.Text('45127', size=(10,1)),sg.Text('BRASTEL',size=(10,1)),sg.Text('BrsailTelecom', size=(10,1)),sg.Text('CLEAR', size=(10,1)),sg.Text('R$ 200,00', size=(10,1)), sg.Text('V', size=(10,1)), sg.Text('3', size=(10,1)), sg.Text('01/01/2022', size=(10,1)) ],
         [sg.Text('45127', size=(10,1)),sg.Text('BR4',size=(10,1)),sg.Text('OI', size=(10,1)),sg.Text('CLEAR', size=(10,1)),sg.Text('R$ 200,00', size=(10,1)), sg.Text('V', size=(10,1)), sg.Text('3', size=(10,1)), sg.Text('01/01/2022', size=(10,1)) ]
    ]

    AtivosVendas = [
        [sg.Text('ID', size=(10,1)),sg.Text('Ativo', size=(10,1)),sg.Text('Empresa', size=(10,1)),sg.Text('Corretora', size=(10,1)), sg.Text('Cotaçao', size=(10,1)), sg.Text('Tipo', size=(10,1)), sg.Text('Nº Açoes', size=(10,1)), sg.Text('Data Negociaçao', size=(15,1)) ],
        [sg.Text('45127', size=(10,1)),sg.Text('BRASTEL',size=(10,1)),sg.Text('BrsailTelecom', size=(10,1)),sg.Text('CLEAR', size=(10,1)),sg.Text('R$ 200,00', size=(10,1)), sg.Text('V', size=(10,1)), sg.Text('3', size=(10,1)), sg.Text('01/01/2022', size=(10,1)) ],
         [sg.Text('45127', size=(10,1)),sg.Text('BR4',size=(10,1)),sg.Text('OI', size=(10,1)),sg.Text('CLEAR', size=(10,1)),sg.Text('R$ 200,00', size=(10,1)), sg.Text('V', size=(10,1)), sg.Text('3', size=(10,1)), sg.Text('01/01/2022', size=(10,1)) ]
    ]

    layout = [
        [menu()],
        [sg.Frame('Compras:', layout=AtivosCompra , key=('Hcompras'))],
        [sg.Frame('Vendas:', layout=AtivosVendas , key=('Hvendas'))],
        [sg.Button('relatorio detalhado', size=(15,2)), sg.Button('relatorio por ativo', size=(15,2))]
    ]
    
    return sg.Window('Historico My_Wallet', layout=layout, finalize=True)

# janela conta
def janelaConta(cpf):
    # tema
    sg.theme('Reddit')
    val =  bd.dados_conta(cpf)

    nome, data,reqCPF = val
    layout = [
        [menu()],
        [sg.Text('Nome:')],
        [sg.Text(nome)],
        [sg.Text('Data Nascimento:')],
        [sg.Text(data)],
        [sg.Text('CPF:')],
        [sg.Text(reqCPF)],
        [sg.Button('Editar'), sg.Button('SAIR')]
    ]
    
    return sg.Window('Conta My_Wallet', layout=layout, finalize=True)


def janelaEditar():
    # tema
    sg.theme('Reddit')

    layout = [
        [menu()],
        [sg.Text('Nome:')],
        [sg.Input(key=('Nome'))],
        [sg.Text('Data Nascimento:')],
        [sg.Input(key=('Data'))],
        [sg.Text('CPF:')],
        [sg.Input(key=('CPF'))],
        [sg.Button('Salvar')]
    ]
    
    return sg.Window('Conta_edita My_Wallet', layout=layout, finalize=True)

# janelas 
janela1 = janelaLogin()     # janelas Login
janela2 = None              # janelas cadastro
janela3 = None              # janelas geral
janela4 = None              # janelas deposito
janela5 = None              # janelas transacao
janela6 = None              # janelas historico
janela7 = None              # janelas conta
janela8 = None              # janelas conta_edita

# loop de eventos
 
while True:
    #conecta banco
   if bd.conectar():
       print("conexao estabelecida")

   window, eventos, valores = sg.read_all_windows()
   
   # fechar janela
   if window == janela1 and eventos == sg.WINDOW_CLOSED:
       break
   if window == janela2 and eventos == sg.WINDOW_CLOSED:
       break
   if window == janela3 and eventos == sg.WINDOW_CLOSED:
       break
   if window == janela4 and eventos == sg.WINDOW_CLOSED:
       break
   if window == janela5 and eventos == sg.WINDOW_CLOSED:
       break
   if window == janela6 and eventos == sg.WINDOW_CLOSED:
       break
   if window == janela7 and eventos == sg.WINDOW_CLOSED:
       break
   if window == janela8 and eventos == sg.WINDOW_CLOSED:
       break

   # janela de cadastro
   if window == janela1 and eventos == 'cadastrar':
       janela2 = janelaCadastro()
       janela1.hide()

    # janela de login
   if window == janela1 and eventos == 'entrar':
       usuario = valores['usuario']
       cpf = valores['senha']
       if bd.ConfirmaLogin(usuario,cpf):
           val = bd.recupera_Deposito(cpf)
           # Recupera valor investido
           ident,lucro_total, porcento = val 
           janela3 = janelaGeral(ident,lucro_total, porcento)
           janela1.hide()
           #print(val)
       else:
           sg.popup('usuario ou esnha nao confirmados ')
  
   # Salva cadastro
   if window == janela2 and eventos == 'cadastrar':
       usuario = valores['usuario']
       dataNesc = valores['data']
       cpf = valores['cpf']
       if bd.InsereCliente(usuario,dataNesc,cpf):
           sg.popup('Cadastro realizado!!')
       else:
           sg.popup('Erro ao Cadastrar!! Tente novamente')
       janela2.hide()
       janela1.un_hide()

    # janela geral
   if window == janela3 and eventos == 'Deposito':
       if janela4 == None:
           janela4 = janelaDeposito()
       else:
           janela4.un_hide()
       janela3.hide()
   if window == janela3 and eventos == 'Transacao':
       if janela5 == None:
           janela5 = janelaTransacao()
       else:
           janela5.un_hide()
       janela3.hide()
   if window == janela3 and eventos == 'Historico':
       if janela6 == None:
           janela6 = janelaHistorico()
       else:
           janela6.un_hide()
       janela3.hide()
   if window == janela3 and eventos == 'Conta':
       if janela7 == None:
           janela7 = janelaConta(cpf)
       else:
           janela7.un_hide()
       janela3.hide()

 # janela Deposito
   if window == janela4 and eventos == 'Geral':
       if janela3 == None:
           janela3 = janelaGeral(ident,lucro_total, porcento)
       else:
           janela3.un_hide()
       janela4.hide()
   if window == janela4 and eventos == 'Transacao':
       if janela5 == None:
           janela5 = janelaTransacao()
       else:
           janela5.un_hide()
       janela4.hide()
   if window == janela4 and eventos == 'Historico':
       if janela6 == None:
           janela6 = janelaHistorico()
       else:
           janela6.un_hide()
       janela4.hide()
   if window == janela4 and eventos == 'Conta':
       if janela7 == None:
           janela7 = janelaConta(cpf)
       else:
           janela7.un_hide()
       janela4.hide()


# janela Transacao
   if window == janela5 and eventos == 'Geral':
       if janela3 == None:
           janela3 = janelaGeral(ident,lucro_total, porcento)
       else:
           janela3.un_hide()
       janela5.hide()
   if window == janela5 and eventos == 'Deposito':
       if janela4 == None:
           janela4 = janelaDeposito()
       else:
           janela4.un_hide()
       janela5.hide()
   if window == janela5 and eventos == 'Historico':
       if janela6 == None:
           janela6 = janelaHistorico()
       else:
           janela6.un_hide()
       janela5.hide()
   if window == janela5 and eventos == 'Conta':
       if janela7 == None:
           janela7 = janelaConta(cpf)
       else:
           janela7.un_hide()
       janela5.hide()

# janela Historico
   if window == janela6 and eventos == 'Geral':
       if janela3 == None:
           janela3 = janelaGeral(ident,lucro_total, porcento)
       else:
           janela3.un_hide()
       janela6.hide()
   if window == janela6 and eventos == 'Deposito':
       if janela4 == None:
           janela4 = janelaDeposito()
       else:
           janela4.un_hide()
       janela6.hide()
   if window == janela6 and eventos == 'Transacao':
       if janela5 == None:
           janela5 = janelaTransacao()
       else:
           janela5.un_hide()
       janela6.hide()
   if window == janela6 and eventos == 'Conta':
       if janela7 == None:
           janela7 = janelaConta(cpf)
       else:
           janela7.un_hide()
       janela6.hide()

 # janela Conta
   if window == janela7 and eventos == 'Geral':
       if janela3 == None:
           janela3 = janelaGeral(ident,lucro_total, porcento)
       else:
           janela3.un_hide()
       janela7.hide()
   if window == janela7 and eventos == 'Deposito':
       if janela4 == None:
           janela4 = janelaDeposito()
       else:
           janela4.un_hide()
       janela7.hide()
   if window == janela7 and eventos == 'Transacao':
       if janela5 == None:
           janela5 = janelaTransacao()
       else:
           janela5.un_hide()
       janela7.hide()
   if window == janela7 and eventos == 'Historico':
       if janela6 == None:
           janela6 = janelaHistorico()
       else:
           janela6.un_hide()
       janela7.hide()
   if window == janela7 and eventos == 'SAIR':
       sg.popup("Encerrar ?")
       break
   if window == janela7 and eventos == 'Editar':
       if janela8 == None:
           janela8 = janelaEditar()
       else:
           janela8.un_hide()
       usuario = valores['usuario']
       dataNesc = valores['Data']
       cpf = valores['CPF']
       cpfAntigo = valores['senha']
       if bd.AlteraCliente(usuario,dataNesc,cpf,cpfAntigo):
           sg.popup('Cadastro salvo')
       else:
           sg.popup('Erro ao salvar!! Tente novamente')
       janela7.hide()