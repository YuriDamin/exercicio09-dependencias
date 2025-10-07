import requests
from rich.console import Console

console = Console()

class APIService:
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    def buscar_usuario_api(self, user_id: str):
        try:
            r = requests.get(f"{self.BASE_URL}/{user_id}", timeout=5)
            r.raise_for_status()
            dados = r.json()
            console.print(f"[bold magenta]Usuário encontrado:[/bold magenta] {dados['name']} ({dados['email']})")
        except requests.RequestException as e:
            console.print(f"[red]Erro ao buscar usuário: {e}[/red]")
