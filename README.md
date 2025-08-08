# MinhaPrimeiraPaginaCamargo

Projeto Django estilo blog com:

- Gerenciamento de páginas (CRUD com busca)
- Sistema simples de mensagens privadas entre usuários
- Autenticação de usuários (login, logout e registro)
- Uso de CKEditor para conteúdo rico
- Herança de templates com navbar

---

## Instalação e execução

1. Clone o repositório ou descompacte o projeto:

```bash
git clone <URL_DO_REPO>
# ou descompacte o zip
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute as migrações:

```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o admin (opcional, mas recomendado):

```bash
python manage.py createsuperuser
```

6. Inicie o servidor:

```bash
python manage.py runserver
```

7. Acesse no navegador:

```
http://127.0.0.1:8000/
```

---

## Funcionalidades

### Páginas (`pages` app)
- Listagem das páginas com busca por título
- Visualização detalhada da página com conteúdo rico e imagem
- Criar, editar e excluir páginas (requer login)

### Mensagens (`messages_app` app)
- Caixa de entrada para receber mensagens de outros usuários
- Enviar mensagem para qualquer usuário registrado (login obrigatório)

### Autenticação (`accounts` app)
- Login, logout e registro de usuários
- Mensagens de sucesso para registro e envio de mensagens

---

## Estrutura dos diretórios principais

- `MinhaPrimeiraPaginaCamargo/` — Configurações do Django e URLs principais
- `pages/` — App para CRUD de páginas
- `messages_app/` — App para mensagens privadas
- `accounts/` — App para registro de usuários
- `templates/` — Templates base e de autenticação
- `media/` — Arquivos de mídia (imagens de páginas)
- `static/` — Arquivos estáticos (CSS, JS, imagens do site, se houver)

---

## Notas

- O banco de dados SQLite não está incluso no repositório (`db.sqlite3` está no `.gitignore`).
- As imagens enviadas ficam em `media/pages_images/`.
- Use o admin para gerenciar usuários, páginas e mensagens se desejar.
- Para personalizar o tema, edite os templates dentro da pasta `templates`.

---

## Comandos úteis

- Migrar banco: `python manage.py migrate`
- Criar superusuário: `python manage.py createsuperuser`
- Rodar servidor: `python manage.py runserver`
- Coletar estáticos (produção): `python manage.py collectstatic`

---

## Contato

Projeto criado por Paulo Renato de Camargo.  
Qualquer dúvida, entre em contato!
