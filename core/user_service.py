from datetime import datetime
from core.email_service import EmailService
from rich.console import Console

console = Console()

class UserService:
    def __init__(self):
        self.usuarios = []
        self.email_service = EmailService()

    def adicionar_usuario(self, nome, email):
        usuario = {
            "id": len(self.usuarios) + 1,
            "nome": nome,
            "email": email,
            "ativo": True
        }
        self.usuarios.append(usuario)
        self.email_service.enviar_boas_vindas(usuario)
        console.print(f"[green]Usuário {nome} adicionado com sucesso![/green]")

    def listar_usuarios(self):
        if not self.usuarios:
            console.print("[yellow]Nenhum usuário cadastrado.[/yellow]")
            return
        console.print("\n[bold cyan]Lista de Usuários:[/bold cyan]")
        for u in self.usuarios:
            status = "Ativo" if u['ativo'] else "Inativo"
            console.print(f"{u['id']}: {u['nome']} ({u['email']}) - {status}")

    def desativar_usuario(self, user_id):
        usuario = next((u for u in self.usuarios if u["id"] == user_id), None)
        if usuario:
            usuario["ativo"] = False
            console.print(f"[red]Usuário {usuario['nome']} desativado.[/red]")
        else:
            console.print("[red]Usuário não encontrado.[/red]")
