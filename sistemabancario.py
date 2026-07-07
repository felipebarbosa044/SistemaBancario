import os
from rich import print
from rich.panel import Panel


class NegativeValueError(Exception):
    pass


class SistemaBancario:
    """
     Representa um sistema bancário simples.

    A classe permite realizar operações de depósito, saque e consulta
    de extrato. Também controla o saldo da conta, a quantidade de
    depósitos realizados, o valor total depositado, o número de saques
    disponíveis e o valor total sacado.

    Attributes:
        _saldo (float): Saldo atual da conta.
        _depositos (int): Quantidade de depósitos realizados.
        _valor_deposito (float): Valor total depositado.
        SAQUES (int): Quantidade de saques diários disponíveis.
        _valor_saque (float): Valor total sacado.
    """
    def __init__(self,saldo = 0):
        self._saldo = saldo
        self._depositos = 0
        self._valor_deposito = 0
        self.SAQUES = 3
        self._valor_saque = 0


    @property
    def saldo(self):
        return self._saldo

    def depositar(self,dinheiro):
        if dinheiro <= 0:
            os.system("cls")
            raise NegativeValueError("Valor inválido, o valor do depósito não pode ser negativo e nem ter nenhum valor")
        self._saldo += dinheiro
        self._depositos+= 1
        self._valor_deposito += dinheiro
        os.system("cls")
        print(f"Você depositou [cyan]R${dinheiro:,.2f}[/] e sua conta tem [green]R${self._saldo:,.2f}")


    def sacar(self,dinheiro):
        if dinheiro <= 0:
            os.system("cls")
            raise NegativeValueError("Valor inválido, o valor do saque não pode ser negativo e nem ter nenhum valor")
        elif self.SAQUES == 0:
            raise PermissionError("Você não tem SAQUES diponíveis")
        elif dinheiro > 500:
            raise PermissionError("O valor máximo de saque é de R$500")
        elif dinheiro > self._saldo:
            raise PermissionError(f"Você não tem dinheiro suficiente para sacar o valor de R${dinheiro:,.2f}")

        self._saldo -= dinheiro
        self.SAQUES -= 1
        self._valor_saque += dinheiro
        os.system('cls')
        print(f"Você sacou [cyan]R${dinheiro:,.2f}[/] e sua conta tem [green]R${self._saldo:,.2f}")


    def extrato(self) -> str:
        def plural(texto,obj):
            if obj > 1:
                return f"{texto}s"
            else:
                return texto


        extrato = (f"""[bright_white]Saldo atual [green]R&{self._saldo:,.2f}[/]
Saques diários: [yellow]{self.SAQUES}[/]
No total você realizou [blue]{self._depositos} {plural("depósito",self._depositos)}[/] que gerou uma renda de [green]R${self._valor_deposito:,.2f}[/]
Também efetuou [purple]{3 - self.SAQUES} {plural("saque", 3 - self.SAQUES)}[/] que retornou no total [green]R${self._valor_saque:,.2f}[/][/]""")

        painel = Panel(extrato,title="---EXTRATO---",width=75,border_style="orange3")
        print(painel)









