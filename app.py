from core.user_service import UserService
from core.api_service import APIService
from rich.console import Console

console = Console()
user_service = UserService()
api_service = APIService()

def menu():
    while True:
        console.print("\n[bold green]=== Sistema de Usuários ===[/bold green]")
        console.print("1 - Adicionar usuário")
        console.print("2 - Listar usuários")
        console.print("3 - Desativar usuário")
        console.print("4 - Buscar usuário na API")
        console.print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o email: ")
                user_service.adicionar_usuario(nome, email)
            case "2":
                user_service.listar_usuarios()
            case "3":
                user_id = int(input("Digite o ID do usuário para desativar: "))
                user_service.desativar_usuario(user_id)
            case "4":
                user_id = input("Digite o ID do usuário para buscar na API: ")
                api_service.buscar_usuario_api(user_id)
            case "0":
                console.print("[yellow]Saindo...[/yellow]")
                break
            case _:
                console.print("[red]Opção inválida![/red]")

if __name__ == "__main__":
    menu()
