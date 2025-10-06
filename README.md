# Sistema de Gerenciamento de Usuários (Refatorado)

## 📘 Descrição
Este projeto é uma refatoração do código original fornecido, com foco em:
- Melhor organização do código
- Redução de dependências diretas
- Testabilidade e reuso de componentes
- Uso de uma biblioteca externa para melhor experiência visual

## 🧠 Principais mudanças
- Código dividido em módulos: `UserService`, `EmailService`, `APIService` e `Utils`
- Uso da biblioteca **Rich** para formatação e cores no terminal
- Criação de um diretório `core` para separar responsabilidades
- Eliminação de variáveis globais
- Log de e-mails separado em `data/log_email.txt`
- Gerenciamento de dependências via **pip**

## 📦 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/YuriDamin/exercicio09-dependencias.git
   cd user-manager-refatorado
