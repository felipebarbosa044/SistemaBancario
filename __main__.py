import os
from rich import print
from sistemabancario import SistemaBancario, NegativeValueError


def main():
    conta = SistemaBancario()
    while True:
        print("""Digite [blue]D[/] para [blue]Depositar[/]
Digite [yellow]S[/] para [yellow]Sacar[/]
Digite [orange3]E[/] para  ver o [orange3]EXTRATO[/]
Digite [red]Q[/] para [red]Sair""")

        opcao = input().lower().strip()
        os.system('cls')


        if opcao == "d":
            try:
                dinheiro = float(input("Digite o dinheiro que deseja depositar: "))
                conta.depositar(dinheiro)
                continue
            except ValueError:
                os.system('cls')
                print("[red]Digite um valor válido para essa operação")
                continue

            except NegativeValueError as erro:
                print(f"[red]{erro}")
                continue

        elif opcao == "s":
            try:
                dinheiro = float(input("Digite o dinheiro que deseja sacar: "))
                conta.sacar(dinheiro)

            except ValueError:
                os.system('cls')
                print("[red]Digite um valor válido para essa operação")

            except Exception as erro:
                os.system('cls')
                print(f"[red]{erro}")

        elif opcao == "e":
            try:
                conta.extrato()
            except Exception as erro:
                print(f"[red] {erro}")

        elif opcao == "q":
            break

        else:
            print("[red]Digite uma opção válida")



if __name__ == '__main__':
    main()


