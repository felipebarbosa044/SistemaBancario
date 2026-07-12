import os
from rich import print
from sistemabancario import *


def main():
    while True:
        print("""Digite [green]C[/] para [green]Cadastrar[/]
Digite [blue]D[/] para [blue]Depositar[/]
Digite [yellow]S[/] para [yellow]Sacar[/]
Digite [orange3]E[/] para  ver o [orange3]EXTRATO[/]
Digite [red]Q[/] para [red]Sair""")


        opcao = input().lower().strip()
        os.system('cls')

        if opcao == "c":
            criar_usuario()


        elif opcao == "d":
            try:
                dinheiro = float(input("Digite o dinheiro que deseja depositar: "))
                deposito(dinheiro)
                continue
            except ValueError:
                os.system('cls')
                print("[red]Digite um valor válido para essa operação")
                continue

        elif opcao == "s":
            try:
                dinheiro = float(input("Digite o dinheiro que deseja sacar: "))
                saque(dinheiro)

            except ValueError:
                os.system('cls')
                print("[red]Digite um valor válido para essa operação")

            except Exception as erro:
                os.system('cls')
                print(f"[red]{erro}")

        elif opcao == "e":
            try:
                extrato()
            except Exception as erro:
                print(f"[red] {erro}")

        elif opcao == "q":
            break

        else:
            print("[red]Digite uma opção válida")



if __name__ == '__main__':
    main()


