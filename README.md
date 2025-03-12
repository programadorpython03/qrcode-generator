# QR Code Generator

Este é um projeto Django para gerar QR codes temporários ou permanentes. Os usuários podem adicionar links, arquivos para download e definir um período de validade para os QR codes temporários.

## Funcionalidades

- Geração de QR codes para links ou arquivos.
- QR codes temporários com data de expiração.
- Interface simples e intuitiva.
- Estilização com Tailwind CSS (via CDN).

## Pré-requisitos

- Python 3.8 ou superior.
- Django 4.2 ou superior.
- Biblioteca `qrcode` e `Pillow` para geração de QR codes.

## Como Configurar

1. Clone o repositório:
   ```bash
   git clone https://github.com/programadorpython03/qrcode-generator.git
   cd qrcode-generator

2. Crie e ative um ambiente virtual:
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:
  pip install -r requirements.txt

4. Execute as migrações:
  python manage.py migrate

5. Crie um superusuário (opcional):
  python manage.py createsuperuser

6. Execute o servidor de desenvolvimento:
  python manage.py runserver

7. Acesse a aplicação no navegador:
  http://127.0.0.1:8000/generate/

### Como Usar

  1. Acesse a página de geração de QR codes.

  2. Insira um link ou faça upload de um arquivo.

  3. Marque a opção "Temporary QR Code" se desejar definir uma data de expiração.

  4. Clique em "Generate QR Code" para criar o QR code.

  5. Visualize o QR code gerado na página de detalhes.

### Estrutura do Projeto

  1. qrcode_app/: Contém os modelos, views e templates do aplicativo.

  2. qrcode_generator/: Configurações do projeto Django.

  3. static/: Arquivos estáticos (CSS, JS, etc.).

  4. media/: Arquivos de mídia (QR codes gerados e arquivos enviados).

### Contribuição

### Contribuições são bem-vindas! Siga os passos abaixo:

    Faça um fork do projeto.

    Crie uma branch para sua feature (git checkout -b feature/nova-feature).

    Commit suas mudanças (git commit -m 'Adiciona nova feature').

    Faça push para a branch (git push origin feature/nova-feature).

    Abra um Pull Request.

### Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.