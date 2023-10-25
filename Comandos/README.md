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
17) Não esqueça de a cada mudança atualizar seu repositório com GIT.
18) Configure a pasta base de TEMPLATES e STATICS
	a) Para "coisas" que precisam de consistência, crie em uma pastas BASE_TEMPLATE e BASE_STATIC
	b) Para "coisas" exclusivas do APP, crie na pasta do APP (item 25 abaixo)
	c) Crie em cada pasta uma outra de nome GLOBAL, que será o namespace (permitirá maior organização e facilidade, bem 
	   como nomes duplicados. Ex: index.html para diversos app's)
19) Crie o arquivo base.html na pasta global
20) Na ./base_static/global crie as subpastas (css, image, js, ...)
21) Na pasta CSS crie o arquivo style.css
22) Toda a estrutura de pastas criada acima não é padrão (pode variar por projeto), por isso temos que informar  ao DJANGO
    tudo no arquivo ./project/settings.py
23) Na seçao TEMPLATES informa o caminho para os TEMPLATES
    'DIRS' : [ ...
		BASE_DIR / 'base_templates'
	]
24) A seção de arquivos estáticos no settings.py tem que ser criada
	STATICFILES_DIRS = (
    	BASE_DIR / 'base_static',
	)
25) Crie uma pasta 'templates' na pasta do APP. Esta pasta não precisa ser configurada no Settings.py, pois isso já é
    padrão para o DJANGO
26) Nesta pasta "templates" criada, crie uma outra de mesmo nome do APP. Ela servirá de NAMESPACE
27) Crie a HOME de seu APP, no caso index.html (mude a linguagem de programação para django html)
28) Use {extends} para extender o arquivo base.html em todos os arquivos html (iniciando pelo index.html) 
29) Edit o arquivo views.py do APP e crie a função de retorno da renderização
30) Crie o arquivo urls.py na pasta de cada APP e adicione a url/path de cada APP. Para permitir que o nome da URL seja igual
    ao de outro APP, adicionamos um namespace ap PATH do APP (app_name = 'contact'). Geralmente como namespace usamos o nome do
	próprio APP.
31) Agora é hora de abir o arquivo urls.py principal, ou seja, o que está na pasta ./project/urls.py e dar um include teste path
    path('', )
	a) Import include (from django import include)
	b) path('', include('contact.urls'))
32) Para usar os arquivos estáticos nos .html use {% load static %}. Temos que fazer isso no base.html
	OBS: para que o comando seja autocompletado não esqueça de mudar a linguagem pada 'django html'
33) Adicione o tag de link para o CSS no arquivo base.html (ou onde for necessário), e não esueça de apontar para o arquivo estático
	que será carregado
	 <link rel="stylesheet" href="style.css">
34) Comece a configurar seu CSS. Faça alguma mudança no body apenas para teste.
	body{
    	background: red;
	}
35) Precisamos iniciar a configuração da área administrativa do DJANGO
	a) O pythom trabalha com MIGRATIONS (que registra toda alteração nos MODELs - Base de Dados)
	b) Com as MIGRATIONS podemos fazer e desfazer alterações na base de dados
36) Se tentarmos acessar a ADMIN do DJANGO (a URL que está em ./project/url.py, configurada na linha "path('admin/', admin.site.urls)")
	não vamos conseguir provavelmente.
	a) Temos que criar as MIGRAÇÔES, ou seja, as tabelas do ADMIN no MODEL, que por darão está usando SQLITE
	b) Os comandos são: para criar -> python manage.py makemigrations / para migrar -> python manage.py migrate
37) A principio as tabelas já estão criadas, então executamos apenas python manage.py migrate. Atenção, sempre que mudar o MODEL
	temos que executar os dois comandos acima.
38) Neste momento, ao executar o servidor, aquelas mensagens em VERMELHO não aparecem mais;
39) Temos que criar um SUPER-USUÁRIO
	A) Execute o comando -> python manage.py createsuperuser
40) Entre na URL de Administrador: http://127.0.0.1:8000/admin/
41) Senhas fracas serão validadas pelas regras existentes em ./project/settings.py, na chave AUTH_PASSWORD_VALIDATORS = []
41) STAFF STATUS - 











   











