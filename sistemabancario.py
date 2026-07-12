from rich import print
from rich.panel import Panel

saldo = 0
SAQUES_DIARIO = 3
valor_saque = 0
depositos = 0
valor_deposito = 0

usuarios = []
contas = []

def saque(valor):
    global saldo
    global SAQUES_DIARIO
    global valor_saque
    if SAQUES_DIARIO == 0:
        print("[red]Você excedeu o saque diário")
    elif saldo <= 0:
        print("[red]Valor inválido , você deve informar um valor acima de 0")
    elif saldo < valor:
        print("[red]Você não tem dinheiro suficiente para sacar")
    elif valor > 500:
        print("[red]O valor máximo é de [green]500R$")
    else:
        saldo -= valor
        valor_saque += valor
        SAQUES_DIARIO -= 1
        #extrato()

def deposito(valor):
    global saldo
    global depositos
    global valor_deposito

    saldo+= valor
    depositos += 1
    valor_deposito += valor


def plural(texto,obj):
    if obj > 1:
        return f"{texto}s"
    else:
        return texto

def extrato():
    if len(usuarios) > 0:
        extrato = (f"""[cyan]{usuarios[-1][0]}[/][bright_white] esse é seu extrato atual:
Saldo atual [green]R&{saldo:,.2f}[/]
Saques diários: [yellow]{SAQUES_DIARIO}[/]
No total você realizou [blue]{depositos} {plural("depósito", depositos)}[/] que gerou uma renda de [green]R${valor_deposito:,.2f}[/]
Também efetuou [purple]{3 - SAQUES_DIARIO} {plural("saque", 3 - SAQUES_DIARIO)}[/] que retornou no total [green]R${valor_saque:,.2f}[/][/]""")
    else:
        extrato = "[red]Crie uma conta para ver seu [orange3]extrato"


    painel = Panel(extrato, title="---EXTRATO---", width=75, border_style="orange3")
    print(painel)

def criar_usuario():
    encerrado = False
    nome = str(input("Digite seu nome: ").strip()).title()

    dta_nasc = int(input("Digite sua data de Nascimento: "))

    cpf = input("Digite seu CPF: ")

    if len(cpf) > 11 or len(cpf) < 11:
        print("[red]Digite um cpf válido")
        return

    if len(usuarios) > 0:
        for usuario in usuarios:
            if cpf == usuario[2]:
                print("[red]CPF Já cadastrado")
                encerrado = True

    if encerrado == True:
        return

    endereco = input("Digite seu Endereço: ").strip().title()


    usuarios.append((nome,dta_nasc,cpf,endereco))
    print("[green]Usuário cadastrado[/]")
    criar_conta(usuarios[-1])

def criar_conta(usuario):
    agencia = "001"
    conta = range(1,10)
    contas.append((agencia,conta,))
    print("[green]Conta bancaria criada")










