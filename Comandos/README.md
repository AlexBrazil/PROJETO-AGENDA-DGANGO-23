COMO CONFIGURAR GIT / SSH - https://www.youtube.com/watch?v=SnTBOhYFr28&feature=youtu.be

1) Criar uma pasta para o projeto e abrir no VSCODE;
2) Vamos criar o novo repositório
	git config --global user.name 'Seu nome'
	git config --global user.email 'Seu email'
	git config --global init.defaultBranch main
3) Configure o .gitignore
	Procure na internet "django .gitignore" e copie o conteúdo
	Crie o arquivo .gitignone no raiz do projeto e cole o conteúdo (pois ele verifica pra frente)
4) Inicie o Git
	git init (antes não esqueça do .gitignore)
5) Criar nesta pasta uma outra de nome .vscode;
6) Copiar e colar as pré-configurações para o VSCODE;
	Criar um arquivo de nome settings.json
	Entar em https://github.com/luizomf/projeto-agenda-django-23/tree/5defd86e31a2f6db22718dc310fa9b6c1e3a0c9a/.vscode
	Copiar o conteúdo
	Reduza os valores para as fontes e zoom em:
	"window.zoomLevel": 0,
    "editor.fontSize": 15,
    "terminal.integrated.fontSize": 15,
7) Criar o ambiente virtual (python -m venv venv);
8) Ative o ambiente virtual (.\venv\Scripts\activate)
9) Instale o DJANGO (pip install django)
10) Se necessário atualize o PIP (python.exe -m pip install --upgrade pip)
11) Execute "pip freeze" para conferir os pacotes ativos
	asgiref==3.7.2
	Django==4.2.6
	sqlparse==0.4.4
	tzdata==2023.3
12) vamos criar o projeto DJANGO (django-admin startproject project .)
	project é a pasta CORE, ou seja, a pasta de configuração de todo o projeto
	usamos o "." para indicar que queremos criar esta pasta na RAIZ do projeto (a pasta criada no passo 1)
13) Inicialize o servidor do DJANGO (python manage.py runserver)
14) Abra a URL http://127.0.0.1:8000/ para ver se o servidor foi iniciado
15) Crie seu(s) App(s) com python manage.py startapp <NOME DO APP>
16) Adicione o nome do app (todos eles) no .\project\settings.py, na chave INSTALLED_APPS = [ ... ] e adicione o nome do
    app entre aspas simples. O nome do App é o mesmo que está na pasta do App, no arquivo apps.py




