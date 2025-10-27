# To-do List Backend (Django + DRF)  
Repositório backend do projeto de lista de tarefas desenvolvido com Django + Django REST framework.

## Pré-requisitos  
- Python ≥ 3.x instalado  
- pip ou algum gerenciador de pacotes Python (ex: pipenv, poetry)  
- Aambiente virtual para isolar dependências  
- Git instalado (para clonar o repositório)  

## Instalação e execução  
Siga estes passos no terminal (cmd ou PowerShell no Windows, ou terminal no macOS/Linux):

````bash
# 1. Clone este repositório
git clone https://github.com/WendelRafael/To-do_backend_django.git
cd To-do_backend_django

# 2. Crie e ative um ambiente virtual
# - No Windows:
python -m venv venv
venv\Scripts\activate

# - No macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute as migrations
python manage.py migrate

# 5. Crie um super-usuário (administrador)
python manage.py createsuperuser

# 7. Execute o servidor de desenvolvimento
python manage.py runserver


