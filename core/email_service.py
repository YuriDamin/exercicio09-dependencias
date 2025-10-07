from datetime import datetime
from core.utils import append_to_file
from rich.console import Console

console = Console()

class EmailService:
    LOG_PATH = "data/log_email.txt"

    def enviar_boas_vindas(self, usuario):
        mensagem = f"Olá {usuario['nome']}, bem-vindo ao sistema!"
        console.print(f"[italic blue]Enviando email para {usuario['email']}...[/italic blue]")
        append_to_file(self.LOG_PATH, f"{datetime.now()} - {usuario['email']} - {mensagem}")
        console.print(f"[green]Email enviado com sucesso![/green]")
