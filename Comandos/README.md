COMO CONFIGURAR GIT / SSH - https://www.youtube.com/watch?v=SnTBOhYFr28&feature=youtu.be

1) Criar uma pasta para o projeto e abrir no VSCODE;
2) Vamos criar o novo repositório
	git config --global user.name 'Seu nome'
	git config --global user.email 'Seu email'
	git config --global init.defaultBranch main
3) Configure o .gitignore
	Procure na internet "django .gitignore" e copie o conteúdo
	Crie o arquivo .gitignore no raiz do projeto e cole o conteúdo (pois ele verifica pra frente)
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
41) STAFF STATUS - quer dizer que pode acessar a área ADM
42) Para alterar a senha do superusuario usamos -> python manage.py changepassword NOME_DO_USUARIO
43) As baese de dados (tipos: sqlite, MongoDB, etc) são configuradas em ./project/settings.py, na chave DATABASES = {}
44) O DJANGO já tem um ORM que permite comunicar com as tabelas de dados
45) ORM (Object-Relational Mapping) é uma técnica de programação usada no desenvolvimento de software para mapear os objetos de um sistema orientado a objetos para as tabelas de um banco de dados relacional. Ele oferece uma maneira de interagir com bancos de dados relacionais usando objetos e linguagens de programação orientadas a objetos, tornando mais fácil e eficiente o acesso e a manipulação de dados em um banco de dados a partir de um código em linguagem de programação.
46) Documentação (tenha atenção a versão da documentação):
	a) https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices
	b) https://docs.djangoproject.com/pt-br/4.2/topics/db/models/
47) No arquivo ./Nome_do_App/models.py devemos criar uma classe que definirá os campos de nossa base de dados do App
	a) CharField podem ter até 255 caracteres
    b) Se vc quer que um campo não seja obrigatório use blank=True
	c) Campos do tipo 'foreign key' são chaves estrangeiras
	d) O campo ID (chave primária) é criado automaticamente
	e) Existem campos que SERÃO pre enchidos de forma automática pelo sistema e não serão editáveis ao usuário, como exemplo temos o campo
	   'created_date' =  models.DateTimeField(default=timezone.now), onde 'timezone.now' é uma função que fornecerá o valor padrão para o campo
48) Aproveitando, já podemos no .\project\settings.py definir a linguagem e o timezone:
	LANGUAGE_CODE = 'pt-br'
	TIME_ZONE = 'America/Sao_Paulo'
47) Qualquer alteração no MODEL, precisamos reusar os comandos:
	criar -> python manage.py makemigrations / para migrar -> python manage.py migrate
48) Neste momento o histórico de alteraçõs do Model foi criado em contact\migrations\0001_initial.py
	É neste momento que a(s) novas(s) tabela(s) são adicionadas no Banco de Dados
	Atenção, se estiver usando algum visualizador, atualize para notar a nova tabela (feche e abra a conexão)
49) O nome da tabela será a junção do nome do APP + o nome do MODEL
50) Para cada model precisamos registrar este model no Admin
	a) Faça isso no ./nome_do_app/admin.py
	b) Crie uma classe com nome do App+"Admin" -> Ex: ContactAdmin (temos que herdar de admin.ModelAdmin)
	c) Esta classe servirá para configurar o Model da Admin do DJANGO
	d) Existem váris formas de criar essa configuração, uma delas é usar o decorador na classe -> @admin.register()
	e) Registramos cada model neste arquivo, para isso temos que importar o model para ele (use a forma longa (caminho completo), evite a forma relativa)
51) Definimos um método mágico __str__(self) na classe do Model (./nome_do_app/models.py). Isso permite que ao mostrar o nome do objeto na lista de objetos cadatstrados, apareça algo legível para o usuário
52) Entre na URL do admin e adicione alguns registros de teste
	a) Os formulários são criados atomaticamente pelo DJANGO,
	b) Os campos em negrito são os prbigatórios (SEM a propriedade blank=True)
53) Vamos configurar a ADMIN:
	a) Com o código "__str__(self)" na classe do Model resolvemos a questão de aparecer o nome cadastrado, porém podemos ferinar ainda mais o Admin
	Use os comandos para:
	a) list_display = TUPLA ->  para informar os campos que queremos que apareça / Crie uma tupla com os campos que queremos listar. A lista de campos se tornarão ordenáveis com um clique
	b) ordering = TUPLA -> já ordena na tela  -> Crie uma tupla com a lista de campos que servirão para ordenar os registros / Para ser decrescente use o sinal de MENOS "-"
	EXEMPLOS:
		i) Lista crescente
			ordering = 'id',
		ii) Lista decrescente
			ordering = '-id',
	c) lister_filter = 'created_date', -> Crie uma tupla com a lista de campos para filtro -> Para aparecer a opção de filtros (dependendo di tipo de campo opções de filtros diferentes poderão ser adicionadas pelo DJANGO)
	d) serch_fields = TUPLA -> cria aopção de um campo para pesquisa -> Crie uma tupla com os campos que permitirão pesquisa
		Ex: search_fields = 'first_name', 'last_name',
		Atenção: SEM QUAQUER TUPLA, NÃO ESQUEÇA DA VÍRGULA NO FINAL
	e) list_per_page = INT -> define a paginação
	f) list_max_show_all = INT -> define se aparecerá a opção de 'mostrar tudo' se a quantidade for menor que a definida em list_max_show_all = INT
	   CUIDADO: defina este valor para um valor não muito alto, algo emtrono de 200, evitando assim que derrube a base de dados (travar)	
	g) list_editable = TULA -> defina os campos que vc quer permitir a edição na própria ADMIN (cuidado, pois esta configuração pode conflitar com outras, como por exemplo, usar como LINK)
	h) list_display_link = TUPLA -> define os campos que receberão link para abertura do registro. Por padrão o DJANGO coloca o link no primeiro campo mostrado
	   CUDADO: esta opçã é incompatível com 'list_editable'
	i) EXISTEM OUTRAS OPÇÕES PARA CONFIGURAR, CONSULTE A DOCUMENTAÇÃO 
56) No DJANGO podemos trabalhar com um SHELL próprio, com isso podemos manipular o MODEL (a base de dados) pela linha de comando:
	a) Para acessar digite -> python manage.py shell
	b) Este SHELL engloba todos os comandos do do Python e já carrega as configurações do DJANGO (presentes no settings.py) e dá um setup no DJANGO
	c) Para iniciar a manipular o model precisamos dar os comandos de importação -> from contact.models import Contact (o comando é case sensitive) 
	d) Ao digitar o nome da classe Contact receberemos o retorno do objeto -> <class 'contact.models.Contact'>
	e) Podemos criar novos registros na base de dados, mas atenção, as regras de validação da classe não serão usadas, tal como campos obrigatórios (sem  	"blank=True")
	f) Vamos criar um novo contato -> c = Contact(first_name='Guilherme'). Se entrarmos no ADM não vemos o novo contato, pois ele está só na variável
	g) Este tipo de resgistro é chamado de 'LAZY', ou seja, fica só na memória. Para salvar temos que executar -> c.save()
	h) Podemos completar os campos desejados -> c.last_name = "Bastos"; c.save(); c.phone = "123456789"; c.save()
	i) Podemos deleter o contato -> c.delete()
	j) Vamos add ele de novo, pois está na memória -> c.save(). Porém agora ele terá outro ID
	k) Até agora trabalhamos na forma "LAZY", ou seja, na memória. mas podemos trabalhar usando os os objetos de forma direta, o que salva de forma automática
	l) Podemos por exemplo usar o método GET -> c = Contact.objects.get(id=1). Este metodo deverá retonar apenas um valor, menos ou mais gerará um erro
	m) Podemos agora manipular a variável c, que é um registro que possui o ID = 1 ->c.first_name = "Alexandrino"; c.save()
	n) Como o campo ID pode ser alterado seu nome, o DJANGO possui um apelido (que é pk) que sempre retornará o CAMPO PRIMÁRIO -> c = Contact.objects.get(pk=1)
	o) Poderiamos recuperar todos os valores com -> c = Contact.objects.all() - a variável "c" receberá uma QuerySet com todos os registros. c[0] por exemplo imprimiria apenas o primeiro registro;  c[1].phone imprimiria o fone do segundo registro e assim por diante
	p) Podemos também executar um FOR -> for contato in c: contato.first_name
	q) Podemos também executar FILTROS -> c = Contact.objects.filter(first_name = "Guilherme") / c = Contact.objects.filter(first_name__startswith='A')
	r) Podemos também ordenar -> c = Contact.objects.all().order_by('-id') - id em ordem decrescente / c = Contact.objects.all().order_by('id') -  id em ordem crescente
	s) Podemos também criar registros direto na base de dados (cpm gravação automática, sem precisar de save()) -> c = Contact.objects.create(first_name='Maria', last_name='João de Deus')
57) Vamos add um campo Boleano no models.py -> show = models.BooleanField(default=True)
58) Para ter imagens na base de dados, vamos precisar ajustar diversas coisas:
	a) Entenda que a imagem não é salva na base de dados, apenas a URL (link) da imagem
	b) Precisamos alterar o settings.py para adicionar alguns comandos:
		i) Vamos aproveitar e já adicionar a pasta que em produção servirá os arquivos estáticos -> STATIC_ROOT =  BASE_DIR / 'static'
		ii) O comando acima exigirá um comando (que está abaixo) para criar a pasta e coletar os arquivos estaticos do projeto -> collectstatic
		iii) Atenção, esta pasta STATIC deve estar no GITIGNORE pelo fato de que devemos usar o comando "collectstatic" no servidor, ai sim a pasta será criada em produção e os arquivos copiados
		iv) Vamos adicionar uma URL para as imagens que serão enviadas pelos usuários -> MEDIA_URL = 'media/'
		v) Vamos adicionar agora o endereço onde serão salvos  estes arquivos de imagens enviados pelos usuários -> MEDIA_ROOT = BASE_DIR / 'media'
59) No Shell, já execute os comandos de coleta -> python manage.py collectstatic - neste momento a pasta static é criada na RAIZ do projeto e os arquivos estáticos são copiados
60) Não esqueça de adicionar esta pasta no GITIGNORE, pois estes arquivos devem ser coletados originalmente no servidor e não versionados -> static/
61) Adicione tammbém a pasta media no GITIGNORE -> media/
62) Agora sim em models.py vamos adicionar o campo para a imagem -> picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
	a) upload_to por padrão irá usar a pasta ./media, por isso o caminho completo será ./media/picture/2023/11
	b) CUIDADO: ao adicionar um novo campo como orbrigatório, isso causara inconsistência no banco de dados
63) Sempre que alteramos o MODEL, precisamos criar uma nova migração. Para tal execute os comandos no SHELL:
	a) python manage.py makemigrations
	b) Considerando que o Python utiliza o pacote Pillow para manipular imagens, pode ser que gere um erro e precisemos executar -> python -m pip install Pillow
	c) caso necessário execute novamente: python manage.py makemigrations
	d) Execte agora o comando python manage.py migrate (esse comando de fato cria oc campos nas tabelas, o comando "makemigrations" apenas cria os arquivos que permitem essa migração/criação)
	e) Inicie seu servidor com "python manage.py runserver" e verifique nas tabelas se os campos foram criados
	f) Para testes adicione uma imagem a um registro qualquer. O DJANGO previne colisão de nomes de imagens. Caso você escolha uma imagem com um nome já existente na pasta, esta imagem será renomeada
64) Se clicarmos na URL da foto, que possui o endereço "http://127.0.0.1:8000/media/pictures/2023/11/Foto_Alexandre2.jpeg" no formulário de cadastro receberemos um erro (Page not found (404)). Isso ocorre em desenvolvimento, pois o servidor usado de forma local não SERVE nosso sistemas desses arquivos. Para resolver isso temos que configurar a URL de nosso projeto (em PRODUÇÃO isso é desnecessário, pois será o SERVIDOR APACHE/NGINX, etc, que servirá)
	a) Para iserir estas URLs entramos no arquivo do projeto em si - .\project\urls.py e adicionamos as linhas necessárias:
		i) from django.conf.urls.static import static
		ii) from django.conf import settings
		iii) urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
		iv) urlpatterns += static(settings.STATIC_URL, document_root =settings.STATIC_ROOT)
65) Agora temos que criar nossas chaves estrangeiras (foreign key), que é uma relação many-to-one, ou seja, muitos para um.
66) Neste caso muitos contatos em nossa agenda poderá usar uma categoria (amigos, família, trabalho, etc)
67) Existem mais dois tipos de relação:
	a) ManyToManyField: Este campo é usado para definir um relacionamento "muitos-para-muitos" (many-to-many). Utilize-o quando um objeto pode estar associado a muitos objetos de outro modelo, e vice-versa. Por exemplo, se você tiver um modelo Student e um modelo Course, um estudante pode se inscrever em muitos cursos e um curso pode ter muitos estudantes.
	b) OneToOneField: Este é um campo para definir um relacionamento "um-para-um" (one-to-one). Use este campo quando um objeto estiver associado a exatamente um objeto de outro modelo. Por exemplo, se cada usuário do seu site pode ter apenas um perfil, você usaria um OneToOneField para vincular o perfil do usuário ao modelo User
68) Vamos criar um novo model no arquivo .\<NOME_do_APP>\models.py:
	a) Crie a classe -> class Category(models.Model):
	b) Crie o campo -> category = models.ForeignKey(Category, on_delete=models.SET_NULL). "on_delete =" define o que será feito caso a chave estrangeira seja deletada. Por exemplo, se deletarmos a calegoria "amigos" o que aconteceria
	com todos os contatdos da tabela contact que possuem esta categoria:
		i) on_delete = models.CASCADE -> deleta todos os registros da tabela que usa a chave estrangeira e depois detela a chave estrangeira. 
		ii) on_delete = models.SET_NULL -> coloca NULL para todos os registros da tabela que usa a chave estrangeira depois deleta a chave estrangeira
		iii) Temos ainda: 
			PROTECT: Impede a exclusão do objeto referenciado. Ao tentar excluir, um erro ProtectedError será lançado se existirem objetos referenciando-o.

			SET_DEFAULT: Define o valor da ForeignKey para o seu valor padrão quando o objeto referenciado é excluído, que deve ser definido com o parâmetro default na definição do campo.

			SET(): Define o valor da ForeignKey para um valor dado ou uma chamada de função passada para SET(). Por exemplo, on_delete=models.SET(get_sentinel_user) definiria a ForeignKey para o usuário retornado pela função get_sentinel_user quando o objeto referenciado for excluído.

			DO_NOTHING: Literalmente não faz nada. Se a integridade referencial do banco de dados não for definida para "CASCADE", então é responsabilidade do 
			desenvolvedor garantir que as FKs órfãs (foreignKey órfãs) sejam tratadas corretamente.

			IMPORTANTE: É importante escolher a opção que melhor se alinha com a lógica do seu aplicativo e com as regras de negócio. Por exemplo, se você tem um blog com posts e comentários, pode não fazer sentido manter comentários se o post correspondente for excluído (CASCADE), mas se você tem usuários e perfis, talvez você não queira que o perfil do usuário seja excluído automaticamente se o usuário for excluído (talvez SET_NULL ou PROTECT seria mais adequado).
	c) Precisamos incluir mais duas configurações no novo campo "categor", ou seja "blank" e "null" -> category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank = True, null = True). Isso em função de que o campo tem como regra ficar como NULL de sua chave estrangeira for deletada
69) Refaça as migrações executando no SHELL:
	a) python manage.py makemigrations
	b) python manage.py migrate
70) Inicie seu servidor e entre no Admin para conferir (uma boa opção é manter dois TERMINAIS abertos, um com o srvidor ativo e outro no SHELL para executar os comandos)
72) Ao entrar no nosso ADMIN -> http://127.0.0.1:8000/admin -> veremos que a tabela category não aparece. Isso porque ainda precisamos registrar ela em nosso .\contact\admin.py:
	a) Acesse .\contact\admin.py
	b) Crie a classe que registrará no ADMIN a nova tabela category. Você pode copiar e colar a classe que já existe que criamos para contact e mudar os valores (reveja os passos do item 50)
	c) Volte a editar o arquivo .\contatc\models.py e adicione o método __str__ a nova classe criada (class Category)
	d) Por segurança, apenas para verificar se nada foi alterado, execute os comandos de migração novamente (item 69). O resultado deverá ser "No changes detected" e "No migrations to apply." respectivamente. Isso porque a linha da função "__str__" não altera em nada a estrutura do model
71) Agora ao entrar no ADMIN teremos mais uma tabela, a categorys. Isso mesmo, no plural. Isso é adicionado pelo DJANGO, apesar de ser um erro de ortografia. Vamos corrigir em um futuro breve com o uso de CLASSES META.
72) Ao entrar e editar um registro na taleba "contacts" veremos a chave estrangeira category sem opção em seu drop-down, isso porque ainda não inserimos nenhuma categoria. Você pode fazer isso a quqluer momento. Não foi gerado erro porque configuramos o campo category para aceitar NULL e em branco.
73) Faça um teste, entre na tabela CATEGORYS e adicione algumas categorias, depois edite algum contato e no campo de categoria escolha no drop-down uma das categorias previamente adicionadas. O que será adicionado no campo será o ID da categoria. Isso garante a modularidade e consistência de nossa base de dados.
74) Vamos usar Model Meta Options do DJANGO (uma classe dentro de outra classe e não tem nada a ver com MetaClass do Python) para corrigir a conversão ERRADA que o próprio DJANGO faz em alguns casos: por exemplo de category para categorys, sendo que o correto seria categories
	a) https://docs.djangoproject.com/en/4.2/ref/models/options/
	b) Abra .\contact\models.py
	c) Insira uma classe de nome Meta (não são metaclasses) com o conteúdo abaixo:
		class Meta:
			verbose_name = 'Category'
			verbose_name_plural = 'Categories'
	d) Adicionamos alterações no Model, então temos que executar os comandos de:
		i) python manage.py makemigrations
		ii) python manage.py migrate
75) Pode ser que em algum ponto a gente veja algo como: _('Category')
	a) Isso é usado para tradução -> GetText. Não estamos abordando isso aqui, mas tem este vídeo que detalha mais sobre tradução: https://www.youtube.com/watch?v=iIsLwz_vkzA&feature=youtu.be
	b) Existe uma configuração no settings.py que configuramos se a tradução está ativa -> USE_I18N = False - coloque como false, pois não vamos usar tradução automática neste projeto
76) Criando USUÁRIOS pelo SHELL do DJANGO sem STAFF e SUPERUSER (faremos isso posteriormente pelo nosso app, por meio de uma VIEW) - apenas para teste e para aprenmder
	a) O DJANGO já tem um sistema de USER básico, o qual podemos usar
	b) Caso precisassemos de mais campos, podemoe estender USER em um novo módulo
	c) Vamoe usar o SEHL do DJANGO -> python manage.py shell
	d) VAMOS IMPORTAR o modo padrão de Usuários do DJANGO -> from django.contrib.auth.models import User
	e) Usamos o módulo acima para CRIAR, OBTER usuários
	f) Para criar um novo usuário vamos usar o MAGAGER do módulo USER (O MENAGER É O .OBJECTS):
		i) user = User.objects.create_user(username = 'usuario', password='123') -> isso não é LAZY, já cria e grava
		ii)Ao entrar nos usuários do http://127.0.0.1:8000/admin - vemos que o novo usuário está com "STAFF STATUS" como desligado e sem nenhuma prmissão. Este usuário não consegue fazer nada em ADMIN, mas geralmente criamos o usuário para logar em nosso APP e não no ADMIN da aplicação
		iii) Caso quisessemos pelo menos logar na área ADMIN usariamos os comandos -> user.is_staff = True / user.save()
		iv) Conasguimos logar, mas sem nenhuma permisão. Isso foi só um teste, pois vamos usar os usuáios em nosso APP e não na ADMIN, neste caso
		v) Vamos então excluir nosso usuários -> user.delete
		vi) Vamos sair do SHELL -> quit()
77) Vamos agora criar um novo campo FOREIGNKEY (chave estrangeira), que será ligado a tabela USER. Este campo será o OWNER (dono do contato)
	a) Entre no .\contact\models.py e importe -> from django.contrib.auth.models import User
	b) Adicone o novo campo -> owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null = True)
	c) Não podemos esquecer de atualizar o Model:
		i) python manage.py makemigrations
		ii) python manage.py migrate
	d) Agora ao adicionar ou editar um contato podemos definir um dono (owner)
78) Para poder testar nossos sistema vamos usar o pacote FAKER para criar dados falsos em nossa base de dados
	a) Primeiro instale o pacote FAKER com o ambiente virtual ativo -> pip install faker
	b) Crie o arquivo .\utils\create_contacts.py
	c) Copie e cole seu conteúdo de -> https://github.com/luizomf/projeto-agenda-django-23/blob/09aa1170f5fa107f4e336d58ae0b05d6fe68dc1a/utils/create_contacts.py
	d) Execute no terminal o arquivo create_contacts.py -> python utils\create_contacts.py
	OBS: não precisa executar python manage.py create_contacts.py, pois as configrações já serão executadas dentro do create_contacts.py
79) Um problema que vamos contornar agora é a necessidade de ter configurações distintas no settings.py para a fase de desenvolvimento e a de produção, pois temos que configurar coisas diferentes em cada caso, como por exemplo para "SECRET_KEY = 'sua_senha' e 'DEBUG = True' para desenvolvimento e 'DEBUG = False' para produção, entre outras coisas:
	a) Na mesma pasta do settings.py crie um outro, que pode ter o nome de local_settings.py. Este novo arquivo não deve ser vesrionado pelo GIT;
	b) Adicione este araquivo no .gitignore -> project/local_settings.py (atenção, após salvar o .gitignone o aarquivo local_settings.py deverá ficar na cor cinza na lista)
	c) ATENÇÃO, futuramente no servidor, como ele não está no GIT, você precisará criar ele manualmente no SERVIDOR e mudar suas configurações para a fase de PRODUÇÃO, tal como DEBUG = False;
	d) Agora vem a mágica: em seu settings.py adicione na última linha (não pode ter nada depois destes comandos) comandos para importar o local_settings.py. As variáveis que existirem de forma repitida dentro do local_settings.py serão sobrescritas no settings.py:
		try:
			from project.local_settings.py import *
		except ImportError:
			...
	e) Abra agora o local_settings.py e sobresceva as variáveis necessárias para o contexto onde vc está, no meu caso atual o contexto de desenvolvimento local e no futuro, quando subir para o servidor, o contetxo do SERVIDOR:
		PARA LOCAL USE:
			SECRET_KEY = 'django-insecure-zscbvu)3pd+cc$nlpnpmf8f^4%hf%tyx18gd70xr@pt%h%6zgp'
			Debug = True
			ALLOWED_HOSTS = [] (deixe em branco a lista)

		PARA O SERVIDOR USE:
			SECRET_KEY = 'sua nova senha para produção / Algo bem seguro e complexo'
			Debug = False
			ALLOWED_HOSTS = [insira aqui  URL de seu HOST]
			(POSSIVELMENTE TB VAMOS ALTERAR O TIPO DE BASE DE DADOS, DE SQLITE PARA OUTRA)
80) Uma das coisas que podemos melhorar na estrutura do projeto, é NÃO colocar todas as VIEWS em um único arquivo, pois ele ficará muito extenso:
	a) Para não sair do padrão criado pelo próprio DJANGO, vamos enganar ele uando PACKAGE Python;
	b) No Python, um pacote (ou package) é uma maneira de organizar módulos relacionados em uma estrutura de diretórios hierárquica. Basicamente, um pacote é um diretório que contém um arquivo especial chamado __init__.py (que pode estar vazio) e outros módulos ou subpacotes. Os pacotes permitem que você estruture seu código Python de forma mais organizada e modular;
	c) Em .\contact\ vamos criar um PACKAGE como o mesmo nome do arquivo .\contact\views.py, para tal crie uma pasta dentro de .\contatc com o nome de views. Esse será nosso PACKAGE;
	d) Dentro desta pasta crie um arquivo __init__.py, o que indicará ao Python que isso é um package. Ao importar esse pacote, este arquivo será a primeira coisa a ser executada;
	e) Precisamos simular que o pacote .\contact\views (que é uma pasta) é .\contact\views.py.
	g) Como temos diversas views para serem criadas vamos organiza-las em módulos na pasta .\contact\views;
	h) Crie dentro do pacote .\contact\views os novos arquivos de view: contact_views.py
	i) Copie o conteúdo do arquivo .\contact.views.py para o .\contact\views\contact_views.py
	j) DELETE (com muito cuidado) o arquivo .\contact.views.py, caso contrário teremos conflitos;
	k) Neste momento nosso projeto para de funcionar quando acessamos no browser. Caso continue acessando é  CACHE. Pare e inicie o servidor se necessário e neste momento teremos um erro de "ImportError" from contact import views.
	m)  Estamos tentando importar em .\templates\urls.py o arquivo views.py que apagamos . Na linha "from contact import views" estamos tentando importar algo que não existe mais;
	n) Teremos que importar agora é um package e não tem definido o método index dentro dele. Isso agora está no arquivo .\contact\views\contact_views.py;
	o) Para resolver isso vamos usar o arquivo .\contact\views\__init__.py e adicionar a linha -> from .contatc_views import *
	p) Estamos usando acima o caminho relativo, mas poderiamos usar o caminho completo
	q) ATENÇÃO, TODA VEZ QUE CRIAR UMA NOVA VIEW, NÃO ESQUEÇA DE IMPORTAR ELA EM .\contact\views\__init__.py
82) Abra o CSS em .\base_static\global\css\style.css e copie o conteúdo de https://github.com/luizomf/projeto-agenda-django-23/blob/c205c5dc9c4c1acce70f060add67c68749f6d296/base_static/global/css/style.css
83) Em nosso CSS (o que foi copiado) tem um local onde definimos o CSS de .content{...}. Este css modelará o conteúdo base de todo o site, que está em ..\base_templates\global\base.html
84) Neste arquivo base.html vamos usar uma tag <main class="content">...</main> e dentro dela um block de DJANGO. 
Lembre-se: o comando block é utilizado no sistema de templates para definir áreas que podem ser substituídas ou estendidas por outros templates. Isso faz parte da funcionalidade de herança de templates, que é um recurso poderoso para reutilização de código e manutenção de uma estrutura consistente em aplicações web.
85) Precisamos agora usar este mesmo block em .\templates\contact\index.html, considerando que este arquivo index.html recebe a extensão do template base e pode usar tudo que está nele -> {% block content %} ... {% endblock content %}
86) Agora dentro do bloco em index.html do app CONTACT podemos inserir nosso conteúdo -> Ex: <h1>TESTE</h1>
87) Precisamos agora de fato injetar os contatos dentro do bloco. Para tal, em nossa VIEW (que agora está no PACKAGE) vamos usar o MODEL para buscar os dados dos contatos:
	a) Abra .\contact\views\contact_views.py e importe o MODEL -> from contact.models import Contact
	b) Vamos carregar os contatos em uma variável -> contacts = Contact.objects.all()
	c) o contexto tem que ser passado para a função render em forma de dicionário, então criamos outra variável com este contexto -> context = {'contacts' : contacts}
	d) Passamos então a variável context para a função render -> return render(request, 'contact/index.html', context)
	e) Neste momento ao atualizar a página nada muda, pois ainda temos que usar este contexto no INDEX.HTML do APP (./contact/templates/contact/index.html)
	f) Dentro do bloco vamos inserir um FOR que fará um loop por todos os registros do MODEL recebido da VIEW dentro do contexto -> {% block content %}...{% endblock content %}
	g) Por meio de um loop acessamos os registros:
		{% for contact in contacts %}
        	{{contact.first_name}} <br>
    	{% endfor %}
88) Um problema que geralmente ocorre quando usamos tabelas com muitas colunas, o que é o caso de nossos contatos, em algum momento a largura da tela não será suficiente. Uma tática que usamos em nosso CSS é a classe .responsive-table:
	.responsive-table {
   		width: 100%;
    	overflow-x: auto;
  	}
89) Vamos agora ciar de fato a tabela:
	a) Dentro do block no ./contact/templates/contact/index.html vamos criar uma DIV ->  <div class="responsive-table"> ... </div>, udando a classe "responsive-table", o que garante que a tabela não irá estrapolar o tamanho do conteúdo, que tem um tamanho mínimo na variável (--table-min-widtth)
	b) Vamos criar a tabela com a classe "contacts-table" ->  <table class="contacts-table">...</table>
	c) Camos criar um título geral para a tabela -> <caption class="table-caption "> Contacts </caption>
	d) Vamos inserir os cabeçalhos na tabela:
		thead>
			<tr class="table-row table-row-header">
				<th class="table-header">ID</th>
				<th class="table-header">First Name</th>
				<th class="table-header">Last Name</th>
				<th class="table-header">Phone</th>
				<th class="table-header">E-mail</th>
			</tr>
        </thead> 
	e) Agora é hora de criar o FOR para dar um loop nos registros do MODEL e inserir nas células da tabela. Este for estará no <tbody> de nossa tabela:
		<tbody>
        {% for contact in contacts %}
          <tr class="table-row">
            <td class="table-cel">
              <a class="table-link" href="#">
                {{ contact.id }}
              </a>
            </td>
            <td class="table-cel">
              {{ contact.first_name }}
            </td>
            <td class="table-cel">
              {{ contact.last_name }}
            </td>
            <td class="table-cel">
              {{ contact.phone }}
            </td>
            <td class="table-cel">
              {{ contact.email }}
            </td>
          </tr>
        {% endfor %}
      </tbody>
90) Vamos usar agora as QuerySets do DJANGO
	a) Na nossa VIEW, esta linha "contacts = Contact.objects.all()" não é muito usada, pois por exemplo, não exclui os registros que possuem o campo "Show = False";
	b) Vamos corrigir tabém a ordem dos registros -> contacts = Contact.objects.all().order_by('-id') -> agora está por ID Decrescente
	c) Para criar um filtro usamos ->  contacts = Contact.objects.filter(show=True).order_by('-id')
	d) Para testar entre no priomeiro registro no ADMIN e desmarque o campo SHOW. Atualize a home e veja que o primeiro contato some
	e) Para facilitar nossos testes, poodemos definir o campo SHOW como editável no arquivo .\contact\admin.py -> list_editable = 'first_name', 'last_name', 'show'
	f) Porém para editar temos que antes permitir a exibição -> list_display = 'id', 'first_name', 'last_name', 'phone','show',
	g) Com isso o campo "Show" e exibido sem ter que entrar no registro e sua edição no formulário é permitida
	h) Podemos fatiar os registros APENAS COMO TESTE, pois vamos no futuro próximo criar uma paginação ->  contacts = Contact.objects.filter(show=True).order_by('-id')[0:20] - mostraremos os vinte primeiros registros apenas
	i) Para ver a Query SQL que está sendo usada basta imprimir el no console com -> print(contacts.query)
91) Vamos construir a solução para visualizar os contatos de forma individual:
	a) Vamos precisar de uma nova URL, um novo TEMPLATE e uma nova VIEW para poder separar esse contato único;
	b) A primeira coisa que criamos é o novo TEMPLATE, pois a VIEW renderiza o TEMPLATE e a URL depende da VIEW;
	c) Vamos em .\contact\templates\contact e criamos contact.html
		i) Vamos extender o template GLOBAL -> {% extends 'global/base.html' %}
		ii) Vamos criar o bloco content ->{% block content %}...{% endblock content %}
		iii) Definimos a classe CSS que irá moldar o contato -> <div class="single-contact">...</div>
		iii) Inserimos o conteúdo que desejamos. Observe que estamos esperando receber um único contato (isso tem quer vir assim da VIEW):
			<h1 class="single-contact-name">
				{{ contact.first_name }} {{ contact.last_name }}
			</h1>
			<p><b>ID:</b> {{ contact.id }}</p>
			<p><b>E-mail:</b> {{ contact.email }}</p>
			<p><b>Phone:</b> {{ contact.phone }}</p>
			<p><b>Created Date:</b> {{ contact.created_date }}</p>
			<p><b>Description:</b> {{ contact.description }}</p>
			<p><b>Category:</b> {{ contact.category.name }}</p>
		iv) Se para a Categoria usassemos "contact.category" retornaria o __str__ do model
	d) Vamos agora criar a nossa nova VIEW:
		i) Abra .\contact\view\contact_views.py
		ii) Para facilitar copie e cole a viwe do index
		iii) Mude o nome para 'contact'
		iv) Vamos criar a variável que receberá o contato do MODEL -> single_contact = Contact.objects.get(id=contact_id)
			a) Temos que cuidar ao usar GET para que um único valor seja retornado, senão teremos um erro
			b) Para que um ínico valor deja retornado vamos receber o ID na VIEW -> def contact(request, contact_id):
			c) Criamos então a variável para o contexto -> context = {'contact': single_contact,} 
			d) Atualizamos o RETURN ->  return render(request, 'contact/contact.html', context)
	e) Precisamos criar a nova URL, abra então .\contact\url.py:
		i) Crie o path -> path('<int:contact_id>:', views.contact, name='contact'), /
		ii) Esta variável int:contact_id deve ter o mesmo nome que está na VIEW
		iii) Sempre deixe uma "/" no final
		iv) Coloque a URL mais específica para cima, sempre, isso evita de dar metch na URL errada
			1a) MAIS ESPECÍFICA -> path('<int:contact_id>/', views.contact, name='contact'),
    		2a) MENOS ESPECÍFICA -> path('', views.index, name='index'),
    f) A idéia agora é colocar links  no ID dos contatos para abrir detalhes do contato:
		i) No .\template\contact\index.html, no <a class="table-link" href="#">, vamos inserir a URL
		ii) A url é o app_name que é 'contact' mais dois pontos mais no nome do path, que tab´´em é contact, teremos então -> 'contact:contact'
		iii) Porém a url tem que receber também o id que estamos clicando, para isso temos que passar o parâmetro -> 'contact:contact' contact.id
		iv) Em DJango para tornar isso didâmico temos que usar {% url ... %} -> {% url 'contact:contact' contact.id %}
		v) Ficando então -> href="{% url 'contact:contact' contact.id %}"
	g) Temos um problema para resolver, se digitarmos no navegador uma URL com um ID de contato que não existe a linha "single_contact = Contact.objects.get(id=contact_id)" retornará um erro. O mesmo poderá ocorrer se o GET retornar mais de um valor para a pesquisa (o que não seria comum, pois estamos usando o ID)
		i) Uma forma de resolver o problema (principalmente o de digitar o ID no navegador) é usar o FILTER, no lugar do GET -> single_contact = Contact.objects.filter(id=contact_id).last() ou single_contact = Contact.objects.filter(id=contact_id).firts()
		ii) Usamos last() ou firts() porque o filter retorna uma QUERYSET (um conjunto de registros). Mesmo que exista apenas um n filtro, ainda assim é uma QUERYSET, por isso usamos last() ou first(), pois assim teremos apenas um registro
		iii) Se vc testar agora e digitar na linha de endereço do Browse um ID que não existe NÃO teremos um erro, porém os campso virão em branco
		iv) Uma solução é levantar uma exceção na contatc_views.py:
			from django.http import Http404
			em def contact -> if single_contact is None: / raise Http404()
		v) Uma outra forma mais direta é usar uma função do DJANGO criada para isso, que é:
			IMPORTE O RECURSO -> from django.shortcuts import render, get_object_or_404
			single_contact = get_object_or_404(MODEL, Chave(S) de pesquisa) -> single_contact = get_object_or_404(Contact, id=contact_id)
		vi) Se precisar de algo mais complexo podemos ainda passar o o MANAGER 'objects' do MODEL e usar um FILTER
			single_contact = get_object_or_404(Contact.objects.flter(id=contact_id))
		vii) Como não vamos precisar de um filtro mais complexo, vamos usar a forma mais simples e aproveitar para inserir mais um parâmetro para o GER:
			single_contact = get_object_or_404(Contact, id=contact_id, show=True)
		viii) Isso evita que possamos inserir o ID na linha de endereõ do browse a visulizar um registro que tem o registro com "show = False"
		IMPORTANTE: neste comando "single_contact = get_object_or_404(Contact, id=contact_id, show=True)" a chaves de filtro são concatenadas com AND, ou seja, com ID tal e Show = TRUE, mas dá para ser OR -> single_contact = get_object_or_404(Contact, Q(id=contact_id) | Q(show=True))
92) Vamos começar a construir nosso cabeçalho da página (o topo). Vamos começar a fazer isso no BASE_TEMPLATE, mas depois vamos separar em um PARTIAL:
	a) No base.html, dentro do <body> vamos criar uma header -> <header class="header"> ...  </header>
	b) Vamos colocar um <h1> ->  <h1 class="header-heading"> Agenda </h1>
	c) Vamos inserir um link no <h1> do texto AGENDA. Este link irá apontar para a URL da home (index.html)
		<h1 class="header-heading">
      		<a href="{% url 'contact:index' %}" class="header-link">
        		Agenda
      		</a>
    	</h1>
	d) Teremos um Menu (por enquanto sem link):
		<nav class="menu">
			<ul class="menu-list">
				<li class="menu-item">
					<a href="" class="menu-link">
						Link 1
					</a>
				</li>
				<li class="menu-item">
					<a href="" class="menu-link">
						Link 2
					</a>
				</li>
			</ul>
		</nav>
	e) Teremos agora um campo de pesquisa SEARCH:
		i) Vamos adicionar este campo em uma <div> -> <div class="search">...</div> -> <div class="search"> ... </div>
		ii) Vamos ter um FORMULÁRIO que terá uma AÇÃO (ACTION) para a URL de procura (que ainda não existe) ->
		iii) Vamos usar um método GET no html (em um FORM de um arquivo HTML podemos usar apenas o método GET ou POSTO). OBS: Em uma API teremos outros métodos. IMPORTANTE:  o método GET envia dados para o servidor via URL. O nome/valor digitádo no formulário é adicionado a URL e enviado. 			Tem limitação de tamanho e SEGURANÇA ZERO, pois estará exposto.

			<div class="search">
				<form action="" method="GET">
					<input type="search" class="search-input" placeholder="Search" id="search" name="q">
				</form>
    		</div> 

			Exemplo: Ao digitar "Alexandre" no campo de pesquisa e dar ENTER a URL ficará -> http://127.0.0.1:8000/?q=Alexandre

			IMPORTANTE: como ACTION="" a URL acionada é a RAIZ

93) Vamos analisar se é interessante separar/dividor nossos arquivos HTML em parciais. A separação dependerá de uma análise prévia e só valerá a pena de permitir uma maior legibilidade e organização, pois realizar muitas separações pode comprometer a performance:
	a) Do ..\global\base.html vamos separar a tag <header>. Recorte toda a TAG;
	b) Em ..\glogal crie uma pasta partials e dentro crie o _header.html. No DJANGO existe a convenção de usar um UNDERLINE no nome quando é um PARTIAL;
	c) Agora apenas cole o <header> no novo arquivo;
	d) Volte no ..\global\base.html e insira {% include 'global/partials/_header.html' %}
	e) IMPORTANTE: use ARQUIVOS PARCIAAIS quando vc perceber que algum código se repete muito dentro da estrutura do HTML
	f) Vamos também separar <head> no base.html. Abra e recorte este bloco;
	g) Crei na pasta ..\partial o arquivo _head.html e coke o conteúdo;
	h) Precisamos fazer um pequeno ajuste, pois onde temos {% static 'global/css/style.css' %} precisamos ter {% load static %}. Então abrrimos o base.html, recortamos "{% load static %}" e colamos em header.html. Lembre-se que "{% load static %}" deve ser o primeiro comando de um arquivo HTML;
	i) Realize agora o include no base.html -> {% include "global\partials\_head.html" %}
94) No base.html ajuste para PT-BR -> <html lang="pt-BR">
95) Vamos personalizar o título:
	a) Em ..\partials\head.htm vamos inserir uma variável no título ->  <title>{{ site_title }}Agenda</title>
	b) Lembre-se, onde temos VIEW podemos usar estas variáveis e dar valores às variáveis no CONTEXTO;
	c) No arquivo ..\view\contact_view.py, no INDEX isnira um valor para 'site_title' no contexto -> 'site_title': 'Contatos - '
	d) Para a VIEW Contact também vamos dar um valor a variável. Primeiro:
		i) Primeiro cramos ma variável juntando os nomes -> site_title = f'{single_contact.first_name} {single_contact.last_name} - '
		ii) Depois adicionamos a variável ao contexto -> 'site_title': site_title
96) Vamos construir a pesquisa (searche). Basicamente até o momento a nossa pesquisa retorna a VIEW da Home, ou seja, do index, pois o action do form está vazio e não possui uma URL
	a) Vamos começar construindo uma VIEW para SEARCHE:
		i) Vamos usar como base a VIEW do INDEX, pois o que vai mudar é apenas o filtro. Copie, cole a altere no nome do "def" para searche;
		ii) Temos que usar o REQUEST recebido para extrair o "q", que é o nome do campo (input) do template parcial contido em _header.html. Neste que teremos o nome digitado para a pesquisa e poderemos filtrar nosso QUERYSET;

		MAS AFINAL, O QUE RECEBEMOS EM UM REQUEST?

		Método HTTP: Pode ser 'GET', 'POST', 'PUT', 'DELETE', etc., indicando o tipo de operação que o cliente deseja realizar. Para um FORM de HTML os método possíveis são apenas GET e POST.

	    Parâmetros da URL: Se a URL inclui parâmetros (por exemplo, em uma URL como /minha-pagina?parametro=valor), eles são acessíveis através do objeto request.

    	Dados do Formulário: Se o método HTTP for 'POST' ou 'PUT', e o cliente enviar dados de um formulário, estes dados serão acessíveis através do objeto request.

    	Cabeçalhos HTTP: Inclui informações como o tipo de navegador (user agent), o idioma preferido, cookies, entre outros. Estes são acessíveis através do objeto request.

    	Informações do Usuário: Se o seu site utiliza autenticação, informações sobre o usuário que fez a solicitação (como se está logado e seus detalhes) podem ser acessíveis através do objeto request.

    	Outras Informações: Como o endereço IP do cliente, informações sobre a sessão (se a aplicação usar sessões), entre outros.

		iii) Como no action do form está direcionando para a HOME (index.html), vamos precisar criar uma nova URL para ele. Para tal abra ..\contact\urls.py
		e adicione novo path ->  path('search/', views.search, name='search'),

		iv) No action do FORM atleter para a nova URL -> action="{% url "contact:search" %}" 

		IMPORTANTE: não teremos parâmetros com o que estamos digitando para a pesquisa porque o GET e entregua para a VIEW por meio do parâmetro REQUEST a linha completa do que está na barra de endereço do browse: Ex: http://127.0.0.1:8000/?q=Alexandre


		IMPORTANTE: para nossa nova VIEW não criaremos um novo template, vamos usar o mesmo usado para a HOME, ou seja, index.html

		v) Voltando na view, altere a variável 'site_title': 'Serach - '

		vi) Para mudar o filtro precisamos pegar o valor digitado do REQUEST:
			a) O request é basicamente um DICIONÁRIO. Para pegar o 'q' vamos usar a linha de comando e criar uma variável com este valor -> search_value = request.GET['q']

		vii) Temos que corrigir um erro que pode ser gerado se digitarmos a URL de forma arbitrária no navegador (sem o valor de pesquisa do campo 'q'), algo tipo -> http://127.0.0.1:8000/search/
			a) Para a crreção, vamos usar o método .get no DICIONÁRIO -> search_value = request.GET.get('q', '')
			b) Basicamente procuramos a chave 'q' no dicionário, se não achar retorna uma STRING vazia
		viii) Para retirar os espaços vazios do inicio e do fim do valor de pesquisa usamos -> search_value = request.GET.get('q', '').strip()
		ix) Vamos agora criar um filtro, além de evitar que seja envidado um valor vazio. Sendo vazio vamos redirecionar para o INDEX.HTML
			a) Vamos usar um recurso do DJANGO que é o redirect -> from django.shortcuts import render, get_object_or_404, redirect
			b) Vamos checar o valor e redirecionar se for o caso:
				if search_value = "":
					retur redirect('contact:index')
			c) Para criar o filtro vamos usar o recurso DJANGO de Field lookups, que é um recurso que permite pesquisa de diversas maneiras -> https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
			d) vamos usar o 'icontains' - busca os campos que contém de alguma forma o texto digitado na pesquisa, independente de maiusculo ou minusculo (case "i"nsensitive)
			e) Como usamos um Field lookups -> nome_do_campo__Field lookups = "termo da pesauisa" -> .filter(first_name__icontains = search_value) \
			f) Para que funcione e mostre o resultado, não devemos suar OFFSET junto com um filtro dessa forma, então retiramos -> [0:20]
		x) Vamos agora criar um filtro mas usando mais de um campo:

			.filter(
				first_name__icontains = search_value,
				last_name__icontains = search_value,
        	) \ 

			IMPORTANTE: toda pesquisa que separa os campos só por virgula, por padrão usa o operador AND, ou seja, tem que existir a ocorrência nos dois campos

		xi) Para usar OR, devemos adicionar um recurso do DJANGO -> Q
			
			from django.db.models import Q

		xii) O "Q" permite usar OR (que é o |)

			.filter(
				Q(first_name__icontains = search_value) |
				Q(last_name__icontains = search_value)
        	) \
		xiii) Vamos completar os campos da pesquisa:
			
			.filter(
				Q(first_name__icontains = search_value) |
				Q(last_name__icontains = search_value) |
				Q(phone__icontains = search_value) |
				Q(email__icontains = search_value)
        	) \

		ATENÇÃO -> DÁ PARA MELHORAR -> EX: Esta pesquisa não encontra o termo de pesquisa "Nicole Moura".
		Apesar de existir uma Nicole Moura, pois esta sendo procurado "Nicole Moura" no first_name e demais campos. e essa ocorrência neste campo não existe.

		IMPORTANTE: Podemos tentar itegrar O PODER da pesauisa do Google em nosso projeto:
		    a) Instale ->  pip install --upgrade google-api-python-client.
			b) Crie uma função em seu projeto Django que use a chave da API e o ID do CSE para fazer chamadas à API do Google Custom Search e recuperar os resultados da busca.
		xiv) Precisamos agora fazer com que o valor da pesquisa de sustente no campo e não seja apagado:
			a) Poderiamos usar SECTION, mas vamos usar o valor pego em da REQUEST em -> search_value = request.GET.get('q', '').strip()
			b) Rde volta no CONTEXTO -> 'search_value' : search_value
			c) Agora no FORM em ..\partials\_header.html usamos este valor
			d) Uma outra forma é usar o próprio 'request.GET', pois não só na VIEW temos acesso ao REQUEST, mas também no TEMPLATE, pois enviamos da VIEW ao TEMPLATE pelo método RENDER.
			e) Então lá no TEMPLATE usamos direto o REQUEST -> value="{{ request.GET.q }}"
			f) O problema é que agora perdemos oa retirada dos espaços com o método STRIP(). Algumas funções que não exigem argumentos podemos chamar direto no TEMPLATE (faça isso com moderação, para não colocar lógica no TEMPLATE) -> value="{{ request.GET.q.strip }}"
		xv) Vamos agora retirar o cabeçalho para quando não existir retorno de um contato e colocar uma mensagem
			a) No ..\templates\contact\index.html vamos usar um IF para renderizar ou não a tabela toda. Para tal sabemos que recebemos na VIEW uma variável com os contatos, que 'contacts'
				{% if contacts %}
      				<div class="responsive-table">
					...
				{endif}
97) Agora vamos implementar um sistema de paginação:
	a) O DJANGO possui um sistema de paginação próprio. Veja detalhes em https://docs.djangoproject.com/en/4.2/topics/pagination/
	b) Na verdade o que vamos fazer é usar PAGINATOR para manipular o querysets e entregar para o TEMPLATE via a VIEW um conjunto menor de registros e diversas outras informações, tais como: 

		    Lista de Itens da Página Atual: A principal informação fornecida pelo Paginator é a lista de itens na página atual. Você pode acessar esses itens iterando sobre o objeto Page.

			Número da Página Atual: Você pode obter o número da página atual usando page_obj.number.

			Total de Páginas: paginator.num_pages fornece o número total de páginas.

			Lista de Números de Página: Para criar uma navegação de paginação, você pode querer mostrar uma lista de números de página. Você pode gerar isso manualmente ou usar paginator.page_range para obter um iterável de números de página.

			Verificação de Página Anterior/Próxima: page_obj.has_previous(), page_obj.has_next(), page_obj.has_other_pages() são métodos úteis para verificar se existem páginas anteriores ou seguintes.

			Números de Páginas Anterior e Próxima: Se existirem páginas anteriores ou seguintes, você pode obter seus números com page_obj.previous_page_number() e page_obj.next_page_number().

			Informações sobre o Estado dos Objetos: page_obj.start_index() e page_obj.end_index() fornecem os índices dos primeiros e últimos objetos na página, respectivamente. Isso pode ser útil para mostrar algo como "exibindo itens 10 a 20 de 100".

			Total de Objetos: paginator.count retorna o número total de objetos em todas as páginas.
	c) Vamos então alterar a VIEW index para entregar a paginação:
		i) Retire o fatiamento "[0:20]"
		ii) Importe o Paginator -> from django.core.paginator import Paginator
		iii) O que vamos repassar agora não serão mais todos os contatos, por isso após receber do MODEL os contatos em "contacts = Contact.objects.filter(show=True).order_by('-id')" vamos usar um paginator:

			paginator = Paginator(contacts, 10)
			# Isso vem lá da URL que está na linha de endereço do browse
			page_number = request.GET.get("page")
			page_obj = paginator.get_page(page_number)
		iv) No CONTEXTO substitua contacts por page_obj (vamos também alterar o nome do indice) -> 'page_obj' : page_obj,
		v) No tempalte index.html substitua as ocorrências de "contacts" por "page_obj". No momento temos 10 registros ao acessar a HOME, mas ainda sem a opção de navegar entre as páginas, bem como o SEARCH a agora retorna "Nenhum registro encontrado" pelo fato de que no contetxo ainda está enviando "contacts" e não "page_obj"
		vi)	Vamos agora criar um template parcial para a paginação. Na pasta ..\base_templates\global crie _pagination.html
		vii) No endereço de help (https://docs.djangoproject.com/en/4.2/topics/pagination/) copie e cole o trecho da <<div class="pagination">. OBS: o css já está no arquivo style.css
		viii) Como e não quero exibir a paginação se não tivermos nada em page_obj, vamos envolver as Tag's for um IF
			{% if page_obj %}
   				<div class="pagination">
					...
				</div>
			{% endif %}
		ix) Temos que dar um include do partial em no template principal, no caso no base.html -> {% include "global/partials/_pagination.html" %}
		x) Os termos de navegação vem em inglês. É possivel traduzir -> pergunte ao CAHT GPT "o Pagination do DJANGO usa "first, previous,  Page, next e last", que são termos em inglês. Existe alguma forma de traduzir para português?"
		xi) Vamos criar esta mesma paginação na VIEW para o search (são os mesmos passos usados para index)
		xii) Quando navegamos nas paginas o DJANGO adiciona a URL um termo "page = nr", tipo>: http://127.0.0.1:8000/?page=5. Porém para o SEARCH vamos tem que completar esta URL, pois ao realizar uma paginação apos a realização de uma pesquisa perdemos a URL
			1) Ao fazr uma pesquisa temos a URL -> http://127.0.0.1:8000/search/?q=nico
			2) Caso venhamos a paginar perdemos o filtro da pesquisa, ocorrendo uma anomalia onde a próxima página ão contém registros com a ocorrência do termo pesquisado
		xiii) Abra o template parcial "_pagination.html" e faça uma contatenação para completar a URL onde houver a TAG <href>:

			<a href="?page=1&q={{ request.GET.q.strip}}">&laquo; first</a>
            <a href="?page={{ page_obj.previous_page_number }}&q={{ request.GET.q.strip}}">previous</a>
			<a href="?page={{ page_obj.next_page_number }}&q={{ request.GET.q.strip}}">next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}&q={{ request.GET.q.strip}}">last &raquo;</a>

			Agora, ao realizar uma pesquisa nossa URL será -> http://127.0.0.1:8000/search/?q=a
			Após ao clicar nos botões da paginação será -> http://127.0.0.1:8000/search/?page=2&q=a
98) Vamos começar a entender a padronização das URLs, ou seja, dos paths:
	a) Quando tivermos um conjunto de URLs relacionadas, usaremos um padrão que descreve de forma mais detalhada o PATH. Por exemplo, para a URL do CRUD dos contatos usaremos:
		i) Ao invés de usar -> path('<int:contact_id>/', views.contact, name='contact'),
		ii) Usaremos -> path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
		iii) A URL gerada e contida no request será -> http://127.0.0.1:8000/contact/1004/detail/

		Um CRUD completo poderia ser:

		# Contact CRUD
		path('contact/create/', views.contact, name='contact'),
		path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
		path('contact/<int:contact_id>/update/', views.contact, name='contact'),
		path('contact/<int:contact_id>/delete/', views.contact, name='contact'),

		# User CRUD
		path('user/create/', views.contact, name='contact'),
		path('user/<int:uder_id>/detail/', views.user, name='user'),
		path('user/<int:uder_id>/update/', views.user, name='user'),
		path('user/<int:uder_id>/delete/', views.user, name='user'),

		VEJA QUE SEGUE UM PADRÃO
99) Vamos agora começar a criar toda a estrutura do CREATE contatos:
	a) Em .\contact\templates\contact crie create.html e insira os códigos básicos
		{% extends 'global/base.html' %}
		{% block content %}
			<h1>CRIANDO CONTATOS</h1> 
		{% endblock content %}
	
		Após criar o TEMPLATE precisamos criar a VIEW que alimentará o TEMPLATE
	b) Vamos criar a VIEW
		i) Na pasta .\contact\views crie contact_forms.py e insira o básico desta viwe:

			def create(request):
				context = {}
				return render(
					request,
					'contact/create.html',
					context
				)
		ii) NÃO ESQUEÇA de adicionar o módulo no .\contact\views\__init__.py -> from .contact_forms import *
			CUIDADO ao usar "import *" em todos os módulos, pois se existirem "def" com o mesmo nome, um substituirá o outro
		iii) Vamos agora adicionar nossa url ->   path('contact/create/', views.create, name='create'),
			Já temos um namesapace, que é "app_name = 'contact'", por isso nossa path será "contact:create"
		iv) Para acessar o endereço será -> http://127.0.0.1:8000/contact/create/
	c) Vamos completar o create.html (conteúdo oferecido pelo professor do curso e não digitado) -> https://github.com/luizomf/projeto-agenda-django-23/commit/45a54d34127db9edd289bb3554d6e68eed9b1374
		i) Vamos usar um CSS/HTML que permira o formulário em uma única coluna
		ii) Ainda não temos Action, isso será detalhado depois e será de forma dinâmica;
		iii) O método é POST (diferente do GET que preenche a URL) é usado para informações sensíveis que não odem aparecer na URL. Outro motivo é que vamos ter que encaminhar uma imagem, que só o POST é capaz de enviar arquivos.
		iv) O DJANGO tem um mecanismo de segurança para o método POST, que coloca um código oculto no formulário para prevenir ataque de CSRF (Falsificação de solicitação entre sites). Vamos ter que usar um CSRF Token no futuro;
		v) Precisamos também do enctype="multipart/form-data", que é requerido em formulários que enviam arquivos
		vi) O DJANGO permite que criemos formulário e trabalhemos com campos dindâmicos

		SE TENTARMOS POSTAR O FORMULÁRIO CREATE VAMOS TER UM ERRO, QUE NA VERDADE É UMA PROTEÇÃO -> CSRF verification failed. Request aborted.
		Refere-se sobre a solicitação de um toquem que garante que os dados que postamos por meio do formulário para dentro da VIEW / MODEL vem de fato do formulário do sistema

		vii) Nosso settings.py já possui esta proteção ativa na linha -> 'django.middleware.csrf.CsrfViewMiddleware',
		viii) Para enviar o token, entramos no FORM (tem que ser do tipo POST) e adicionamos. Entre em create.html e adicione -> {% csrf_token %}

		De forma oculta o Token será incluso na página:
		<input type="hidden" name="csrfmiddlewaretoken" value="BILe1dQOVenB2yH26Zn8pY4uvqpRxgXsyPlW14bB8uZcygsS0PxZ9vC5EoYim1jl">
	d) Para fins de teste vamos completar o ACTION do formulário no arquivo create.html -> action="{% url "contact:create" %}"
	e) Todos os INPUTs dos formulários possuem um NAME e ID. O NAME é usado para acessar seu conteúdo no REQUEST enviado. Este Nomes e IDs devem ser únicos na página.
	f) Para fins de teste, na VIEW contact_forms.py insira -> print(request.POST.get('firts_name'))
	g) temos como saber o método utilzado, se POST ou GET -> print(request.method)
	
		OBSERVAÇÃO IMPORTANTE: quando acessamos a URL sem enviar nada o método é GET, pois apenas estamos lendo o formulário. Mas ao enviar algo o método é POST, que é para salvar, criar ou deletar algo.
	h) Usamos então esta informação (se é GET ou POST)
		if request.method == "POST":
			print('--------------------------------------')
			print(request.method)
			print(request.POST.get('first_name'))
			print(request.POST.get('last_name'))
			print('--------------------------------------')
		else:
			print('--------------------------------------')
			print(request.method)
			print('--------------------------------------')
100) Criando o formulário baseado no MODEL:
	a) Importe o model from django -> import forms
	b) Para criar um formulário usamos uma classe que deriva de forms.ModelForm. Essa derivação garante que vamos usar os campos do Model na construção do formulário -> class ContactForm(forms.ModelForm):
	c) Para definir os campos que vamos usar precisamos de uma MetaClass de nome "Meta". Essa metaclass recebe o nome do model  dos campos (em forma de Tupla)
		class Meta:
			model = Contact
			fields = (
				'first_name', 'last_name', 'phone',
			)
	d) Precisamos passar o formulario para o CONTEXTO para que possa ser usado no TEMPLATE:
		context = {
        	'form' : ContactForm()
    	}
	e) Precisamos usar o FORM no TEMPLATE:
		i) No TEMPLATE create.html vamos deixar apenas uma <DIV> para um dos campos

		<div class="form-content">
			<div class="form-group">
				<label for="id_first_name">first_name</label>
				<input type="text" name="first_name" maxlength="255" id="id_first_name">
			</div>
      	</div>

		ii) Vamos usar um FOR para construir todos os campos recebido pelo CONTEXTO da VIEW

			{% for field in form %}
				<div class="form-group">
					<label for="{{ field.id_for_label}}">{{ field.label}}</label>
					{{ field }}
				</div>
			{% endfor %}

			IMPORTANTE -> observe que o input todo (<input type="text" name="first_name" maxlength="255" id="id_first_name">) é substituído por {% endfor %}
		
		iii) Considerando que a VIEW tera um request tipo GET (ao carregar o formulário vazio) e o request do tipo POST ao enviar dados para cadastro/alteração, precisamos identificar isso no código da VIEW, além de que para o POST temos que ter um parâmetro para tramitar estes dados
		
			 if request.method == "POST":
				context = {
					'form' : ContactForm(request.POST)
				}

				return render(
					request,
					'contact/create.html',
					context
				)
101) Começando a validar o formulário	
	a) Para emitir mensagens de ERRO de forma automática abaixo do campo usamos -> {{ field.errors }}
	b) Para simular um erro e até mesmo aprender a acessar os dados do formulário dentro da classe que cosntroi o formulário, usaremos um método chamado -> def clean(self)

		# Este método tem acesso aos dados do formulário antes de serem enviados (teremos um dicionário com os dados enviados)
		# O método clean é usado para validar ou modificar dados de formulários antes de serem salvos ou processados. 
		def clean(self):
			cleaned_data = self.cleaned_data
			print(cleaned_data)
			# Retornar para a super classe garante que a validação padrão do formulário ainda ocorra
			return super().clean()
	c) Vamos agora de fato adicionar um erro na classe clean() para ver o resultado do uso de -> {{ field.errors }}
		i) Importa e classe de erro -> from django.core.exceptions import ValidationError
		ii) Vamos alterar a classe clean para inserir o erro:
			
			# add_error recebe o campo que vamos adicionar o erro. Se não adicionarmos campo, o erro será de formulário
			self.add_error(
				'first_name', 
				ValidationError(
					'Mensagem de erro',
					code = 'invalid' # Estes códigos podem ser criados
				) 
			) 

			OBS: podemos ter mais de um self.add_error para cada campo, ous eja, várias validações
		iii) Se editarmos o codigo fonte o que teremos é uma lista com os erros

			<ul class="errorlist"><li>Mensagem de erro</li><li>Mensagem de erro 2</li></ul>  

		iv) Já temos em nosso CSS a classe para o erro:

		 .errorlist {
			list-style: none;
			font-size: var(--smaller-font-size);
			color: tomato;
		}
	d) Temos também os erros do tipo nonfield errors. Erros que não são dos campos e sim do formulário
		i) Para exibir estes erros vamos criar uma nova <div> abaixo do formulário e usar uma prpriedade dor forms (recebida na classe -> class ContactForm(forms.ModelForm)), a propriedade "non_field_errors"

			{% if form.non_field_errors %}
				<div class="form-content">
					<div class="form-group">
						<div class="message error">
						{{ form.non_field_errors }}
						</div>
					</div>
				</div>
			{% endif %}
		ii) Para de fato testarmos, temos que adicionar non_field_errors no formulário
102) É comum no DJango ter um arquivo só para os Forms, tirando ele do arquivo das VIEWs.
	a) Em .\contact crie forms.py
	b) Mova a classe ContatcForm para o novo arquivo
	c) Mova também os importações necessárias:
		from django import forms
		from django.core.exceptions import ValidationError
	d) Importe o model para o arquivo forms.py -> from . import models
	e) Altere a criação da variável que cria a variável model -> model = models.Contact (antes era apenas model = Contact)
	f) Temos que agora levar o FORM de volta para a VIEW
		i) Em .\contact\views\contact_forms.py importe o FORM -> from contact.forms import ContactForm
103) Caso queiramos mudar o Label do campo, usamos  um VERBOSE_NAME no Model  -> Ex: phone = models.CharField(max_length=50, verbose_name="Fone"). Porém se usarmos os WIDGETs do Django para configurar os campos, esse verbose_name não funciona
104) Podemos configurar os campos usando WIDGETS, que é na verdade um dicionário usado na classe META que cria o FORM. Este dicionário pode conter todas as configurações do campo:
	a) Por exemplo, vamos mudar no "First Name" de text para password:
		widgets = {
            'first_name' : forms.PasswordInput()
        }
	b) Vamos voltar o campo para text área e configurar algumas coisas do campo. Vamos configurar alguns atributos do campo, para isso configuramos uma chave chamada "attrs", que é também um dicionário com várias configurações, uma delas é o "placeholder". POdemos também definir classes para o campo

		=> AQUI VAMOS CRIAR O WIDGET

		widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Escreva Aqui...',
                    'class' : 'classe-a classe-b'
                }
            )
        }

		VEJA O RESULTADO EM HTML NA PÁGINA:

		<div class="form-group">
            <label for="id_first_name">First name</label>
            <input type="text" name="first_name" placeholder="Escreva Aqui..." class="classe-a classe-b" maxlength="50" required id="id_first_name">
            <ul class="errorlist"><li>This field is required.</li><li>Mensagem de erro</li><li>Mensagem de erro 2</li></ul>  
        </div>

		=> AQUI VAMOS ALTERAR O WIDGET

		a) Precisamos ter acesso ao INIT da classe do FORM, assim temos acesso ao "self.fields", que é um dicionário com os campos. cada campo

			def __init__(self, *args, **kwargs):
				super().__init__(*args, **kwargs)
				self.fields['first_name'].widget.attrs.update(
					{'placeholder' : 'Escreva Aqui (veio do init)...',
					'class' : 'classe-a classe-b'
					}
				)
		
		ATENÇÃO: Para usar os WIDGETs de campos, ou criamos ou acessamos pelo __init__(). Nunca use os dois métodos

		=> EXISTE UMA TERCEIRA FORMA QUE É RECRIAR O CAMPO:
		a) Os campso são criados no MODEL, mas podem ser recriados no FORM, quando então teremos acesso a diveras configurações do campo

			first_name = forms.CharField(
				widget=forms.TextInput(
					attrs={
					'placeholder' : 'Escreva Aqui (veio do forms.CharField())...',
					'class' : 'classe-a classe-b'
					}
				),
				label='Primeiro Nome'
			)
105) Vamos aproveitar que podemos recriar os campos e usar novas configurações (first_name = forms.CharField(...)) para colocar textos de ajuda nos campos. 	
	a) Configure o texto de ajuda ->  help_text= "Texto de ajuda para seu usuário"
	b) Precisamos agora passar este texto de ajuda para o template create.html
		
		{% if field.help_text %}
            <p class="help_text"> {{ field.help_text }} </p>
        {% endif %}

106) Até agora usamos os campos criados no MODEL, mas poderiamos criar um campo avulso no formulário, não vinculado a base de dados

	qualquer = forms.CharField(
        widget=forms.TextInput(
            attrs={
              'placeholder' : 'Este é um campo avulso...',
            }
        ),
        help_text= "Texto de ajuda para seu usuário"
    )
107) Vamos começar a validação dos campos.Sabemos que o método "def clean(self)" tem acesso a todos os valores de campos antes dele ser inserido no MODEL (na base de dados)	 
	a) O m´´etodo "def clean(self)" tem acesso á todos os campos e é útil quando queremos trabalhar com a validação de mais de um campo ao mesmo tempo, como por exemplo, quando queremos verificar se o first_name não é igual ao last_name
	b) Mas quando queremos validar diretamente um campo, podemos usar um formato mais específico do método CLEAN, o que adiciona o nome do campo
		i) Lembre-se que  "self.cleaned_data" é um dicionário que possui todos os campos
		ii) Por isso podemos pegar o campo direto assim -> first_name = self.cleaned_data.get('first_name')

		def clean_first_name(self):
			first_name = self.cleaned_data.get('first_name')
			print("Passei no clean do first_name - ", first_name)
			return first_name
	c) Vamos inserir uma validação. Vamos dizer que não queremos que seja digitado em firts_name "ABC"

			# O Uso de raise lança um erro e pára o código, por isso se tver mais validações eles não serão processados
            # Por isso essa não é a melhor forma, mas sim o uso de self.add_error(...)

            raise ValidationError(
                'Não digite ABC neste campo',
                code='invalid'
            )
	d) Vamos então alterar para o uso de self.add_error()
			self.add_error(
                'first_name', 
                ValidationError(
                    'Não inclua ABC neste campo',
                    code = 'invalid' # Estes códigos podem ser criados
                ) 
            ) 
	e) Vamos dar um exemplo de validação onde um campo depende do valor de outro campo. Neste caso, como já sabemos, teremos que usar "def clean(self)", pois neste método temos acesso à todos os campos antes de registrar no Model
		
		first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError('O primeiro nome e o segundo n ome não podem ser iguais', code = 'invalid')
            self.add_error('first_name', msg) 
            self.add_error('last_name', msg) 


		IMPORTANTE: não sei o motivo, mas se o código acima estiver na função CLEAN depois de alguns outros "self.add_error", parece que o valor de "self.cleaned_data" sofre alterações e ocorrem anomalias nas validações

		AQUI ESTÁ A EXPLICAÇÃO:

		1) Na estrutura do Django, quando você utiliza a função clean(self) em um formulário, o objetivo principal é realizar validações adicionais que não são cobertas pelas validações padrão de cada campo. Aqui está o que acontece em relação a self.cleaned_data:

		2) Antes de clean(self) ser chamada: Quando um formulário é submetido, o Django primeiro chama o método is_valid(), que por sua vez chama full_clean(). Durante este processo, cada campo do formulário é validado individualmente e os dados limpos são armazenados em self.cleaned_data.

		3) Durante a execução de clean(self): Neste ponto, self.cleaned_data já contém os dados que passaram pelas validações de campo individuais. Você pode acessar e modificar esses dados em clean(self). Por exemplo, você pode adicionar, remover ou alterar os dados em self.cleaned_data.

		4) Após clean(self): Se clean(self) for concluída com sucesso (ou seja, sem levantar uma exceção de validação), self.cleaned_data conterá quaisquer modificações feitas durante clean(self). Se uma exceção de validação for levantada, o formulário será considerado inválido e self.cleaned_data pode não conter todos os dados do formulário, apenas os dados que passaram nas validações anteriores.

		5) Importante sobre exceções: Se você levantar ValidationError em clean(self), o Django não incluirá o campo que causou o erro em self.cleaned_data. Isso é importante para se lembrar, pois significa que você deve tratar self.cleaned_data como potencialmente incompleto.

		6) Resumindo, clean(self) é um lugar para você realizar validações que dependem de múltiplos campos ou lógicas mais complexas que não são facilmente cobertas pelas validações de campo padrão do Django. Alterações feitas em self.cleaned_data dentro deste método são refletidas após a execução do método, desde que não ocorram exceções de validação
108) vamos colocar o restante dos campos do MODEL no formulário. Em forms.py aicionamos os campos:

	 	class Meta:
			model = models.Contact
			fields = (
						'first_name', 'last_name', 'phone',
						'email', 'description', 'category',
			)

		O:S os campos "created_date" e "show" não estarão acessíveis de forma direta ao usuário e o campo "picture" será manipulado no futuro

109) Após a validação dos campos podemos de fato registrar os dados na Base de Dados:
	a) Dentro da VIEW contatc_forms.py, vamos precisar de uma variável com o formulário, antes de passar para o TEMPLATE>

	ERA ASSIM: 

	if request.method == "POST":
        context = {
            'form' : ContactForm(request.POST)
        }
	...

	FICOU ASSIM:

	if request.method == "POST":
        form = ContactForm(request.POST)
        context = {
            'form' : form
        }
	...

	b) Vamos agora verificar se o formulário é válido. Caso não exista erro, form.is_valid() retorna TRUE (obs: campos e-mail possui validação própria do DJANGO)

		if form.is_valid():
			print('Formulário é valido') 

	c) Para salvar o FORM tem um método SAVE():
		
		if form.is_valid():
			print('Formulário é valido')
			form.save()

	d) O método SAVE() recebe um COMMIT, com isso podemos adiar o salvamento na base de dados para a execução de alguma ação:
				
		if form.is_valid():
            print('Formulário é valido')
            # O padrão do commit é TRUE
            contact = form.save(commit=False)
            contact.show = False
            contact.save()
	
	e) Para fins de continuidade, vamos voltar a apenas salvar. Futuramente vamos usar o COMMIT = FALSE, para atrelar o dono do contato ao contato
		if form.is_valid():
			print('Formulário é valido')
			form.save()

	f) Após enviarmos os dados do contato e salvar na base de dados, o correto seria limpar o FORM ou enviar para uma edição, evitando assim a possibilidade de erro do usuário clicar diversas vezes em SEND/ENVIAR (ou mesmo atualizar a página que também cadastra novo registro) e cadastrar diversas vezes o mesmo contato. Como a gente ainda não tem uma outra VIEW para editar os dados do contato, vamos só redirecionar novamente para contatc/create

		i) Vamos precisar importar redirect -> from django.shortcuts import render, redirect
		ii) Vamos redirecionar:
		
			if form.is_valid():
				print('Formulário é valido')
				form.save()
				# Aqui vamos redirecionar para a contatc:create e abrir o formulário em branco, evitand que possamos clicar diversas vezes em salvar e salvar o contato 
				# diversas vezes. Isso enqunto não criamos a VIEW de edição
				return redirect('contatc:create')
110) Agora que o formulário foi validado e o registro foi salvo na base de dados, vamos criar uma forma de direcionar para uma nova VIEW e URL de UPDATE, evitando que ocorra a possibilidade de diversos cadastros do mesmo registro
	a) Vamos primeiro colocar um link na HOME para a URL de CREATE, isso em .\partials\_header.html

		<a href="{% url "contact:create" %}" class="menu-link">
        	Cadastrar
        </a>
	b) Temos que transformar o ACTION do TEMPLATE create.html em dinâmico. Atualmente ele está arbitrário e abrindo a URL de CREATE -> action="{% url "contact:create" %}"
	c) Para fazer isso então, temos que ter acesso da URL na VIEW e para tal usamos o recurso de REVERSE (permite que você obtenha a URL de uma determinada view baseando-se no seu nome ou no namespace)
		i) Primeiro importamos o pacote -> from django.urls import reverse
		ii) Com o vamos usar uma VIEW para criar o contato e outra para atualizar o contato, porém usando o mesmo TEMPLATE, no lugar da URL no ACTION do TEMPLATE create.html, teremos que ter uma VARIÁVEL. Em .\templates\contact\create.html injete a variável:

			No lugar de -> action="{% url "contact:create" %}"
			Use -> action="{{ form_action}}"
		iii) Esta variável será criada na VIEW CREATE e receverá o REVERSE da URL que está sendo usada

			def create(request):
				# Com isso saberemos qual a URL que está acessando esta VIEW
				form_action = reverse('contact:create')
				...
		iv) Vamos adicionar esta variável ao CONTEXTO

			if request.method == "POST":
				form = ContactForm(request.POST)
				context = {
					'form' : form,
					'form_action' : form_action
				}
		v) Se os FORM for validado por completo, os dados são salvos e depois não deve mais ser retornado para o CREATE, mas sim agora para o View UPDATE (que ainda será criada)

			ERA ASSIM:
			
			if form.is_valid():
                form.save()
                return redirect('contact:create')

			FICOU ASSIM:
			
			if form.is_valid():
                contact = form.save()
                return redirect('contact:update', contact_id = contact.pk)
		vi) O PATH 'contact:update' ainda não existe, temos então que criar. Abra urls.py e adicione:
			 
			 path('contact/<int:contact_id>/update', views.update, name='update')

			 LEMBRE-SE: o ID do contato é informado la na VIEW, na linha -> return redirect('contact:update', contact_id = contact.pk)

		vii) Precisamos alterar também o contexto para quando não existe POSTO (o formulário está VAZIO)
			
			# Else  (NÃO TEMOS NENHUM POST)
			context = {
				'form' : ContactForm(),
				'form_action' : form_action,
			}
		viii) É hora de criar a nova VIEW Update	
			a) Duplique a VIEW create e alere o nome para update
			b) Nesta VIEW precisamos receber dinamicamente o ID -> def update(request, contact_id):
			c) Com isso saberemos qual a URL que está acessando esta VIEW, porém é preciso pasar os argumentos dinâmicos também
    			
				form_action = reverse('contact:update', args=(contact_id,))
			d) Como UPDATE atualiza um contato, precisamos ter este contato para atualizar. Em forms.py criamos o formulário que herda "forms do django, importado em -> from django import forms". No super dest classe teremos acesso ao instance, que é uma instância do Model, pois criamos o formulário baseado em um MODEL já existente. Relembre abaixo:

			class ContactForm(forms.ModelForm):
				...
				class Meta:
        			model = models.Contact
					...
			e) Então quando salvamos o formulário, na verdade estamos atualizando esta instância

			f) Para ter acesso a este contato vamos usar um módulo que já usamos, o "get_object_or_404". Adicione este módulo -> from django.shortcuts import render, redirect, get_object_or_404

			g) Porém antes temos que importar o Model para a VIEW contact_forms.py -> from contact.models import Contact 

			h) Aí sim capturamos o contato dentro do Model (caso não exista teremos um erro 404):

				def update(request, contact_id):
					contact = get_object_or_404(Contact, pk=contact_id, show=True)
					# Com isso saberemos qual a URL que está acessando esta VIEW, porém é preciso pasar os argumentos dinâmicos também
					form_action = reverse('contact:update', args=(contact_id,))
					...
			i) Agora basta atualizar o INSTANCE que já existe do MODEL com os dados recebidos do POST (request.POST)

			 	if request.method == "POST":
        			form = ContactForm(request.POST, instance=contact)
					...
111) Vamos criar alguns links para UPDATE e DELETE, porém faremos isso na tela dos dados do contato
	a) Primeiro vamos completar o CSS que vamos precisar. Adicionada as classes .contact-links {...}, .btn-link {...} e .btn-delete {...}
	   Acesse em -> https://github.com/luizomf/projeto-agenda-django-23/commit/b3c0bec4101458535e3a97c89d8132c8d607155d#diff-0a64893e3aa3d5648fedfc901a706c794a71449700739ba966a0803e6b7319a2

	 b) No template do contatc.html vamos criar uma <DIV> para os botões/links de ATUALIZAR e DELETAR  
	 	<div class="contact-links">
			...
    	</div>
	c) Vamos primeiro adicionar o link para UPDATE. Este link abrirá o formulário para atualização. Todo link em uma página HTML é do tipo GET (não confunda com a ação de atualizar o formulário, que seria a próxima etapa, esse sim seria do tipo POST)
		<div class="contact-links">
			<a href= {% url 'contact:update' contact.id %}>ATUALIZAR</a>
    </div>
    	</div>
	
	d) Vamos adiconar as classes para formatar o botõo de Update -> <a class="btn btn-link" href= {% url 'contact:update' contact.id %}>ATUALIZAR</a>
    </div>

	e) Já o DELETE vai alterar algo na base de dados, por isso ele terá que ser dentro de um <form>, pois é um botão de fato e possuirá o METODH = POST e um ACTION, por enquanto vazio
		<form action="" method="POST">
        	<button class="btn btn-link btn-delete" type"submit">APAGAR</button>
        </form>

	ATENÇÂO - neste momento se clicarmos no botão de APAGAR teremos um erro -> Forbidden /"POST /contact/1011/? HTTP/1.1" 403 2506
	É o método POST no DJANGO exige um CRSF TOKEN

		<form action="" method="POST">
			{% csrf_token %}
			<button class="btn btn-link btn-delete" type"submit">APAGAR</button>
     	 </form>
		
	f) Vamos iniciar a criar nossa VIEW de DELEÇÃO. Inicialmente vamos criar uma forma de deletar sem pedir confirmação antes de deletar:
		1) Primeiro crie a nova VIEW

			def delete(request, contact_id):
				contact = get_object_or_404(Contact, pk=contact_id, show=True)
				contact.delete()
				return redirect('contact:index')
		2) Crie o PATH ->  path('contact/<int:contact_id>/delete', views.delete, name='delete'),
		3) Coloque agora no ACTION do FORM a URL (Path) -> <form action="{% url 'contact:delete' contact.id %}" method="POST">
		4) Agora se clicarmos em um contato e depois em APAGAR, o contato será deletado sem conirmação e seremos resirecionados para contact:index e não teremos mais aquele contato que foi deletado

	g) Porém não vamos deletar o contato de forma direta ao acessar a VIEW (contact.delete()). Vamos é mudar a mensagem do botão para "CONFIRMA" e o usuário terá de clicar de novo 
		1) Quando a pessoa clica no botão APAGAR o ACTION do FORM abre a VIEW de DELEÇÂO (action="{% url 'contact:delete' contact.id %}")
		2) Na VIEW "delete" não vamos deleter nem redirecionar de imediato. Vamos é renderizar a mesma página de CONTATO novamente, porém não esqueça de passar os dados do contato no contexto

			# contact.delete()
			# return redirect('contact:index')
			return render(
				request,
				'contact/contact.html',
				{
					'contact':contact
				}
			)
		3) Agora se clicarmos em APAGAR apenas é renderizado novamente os dados do mesmo contato (nada acontece de diferente)
	h) Temos agora que mudar o botão para CONFIRMA. Como temos como assessar os dados de POST.
	i) Vamos forçar para que exista um INPUT com o nome 'confirmation' vindo do TEMPLATE para dentro da VIEW, mas por padrão se não vier nenhum valor ele assumirá 'no'
		
		def delete(request, contact_id):
			contact = get_object_or_404(Contact, pk=contact_id, show=True)
			confirmation = request.POST.get('confirmation', 'no')
	j) Na VIEW, se for confirmado (confirmation == 'yes'), aí sim deleta e redireciona
		if confirmation == 'yes':
			contact.delete()
			return redirect('contact:index')
	l) Mas precisamos de mudar o TEMPLATE para renderizar APAGAR ou CONFIRMA?. Ao clicar em APAGAR, por padrão a variável 'confirmation' ESTARÁ COMO 'no' e com isso o botão mudará para "CONFIRMA?"

		 <form action="{% url 'contact:delete' contact.id %}" method="POST">
			{% csrf_token %}
			{% if confirmation == 'no' %}
				<button class="btn btn-link btn-delete" type"submit">CONFIRMA?</button> 
			{% else %}
				<button class="btn btn-link btn-delete" type"submit">APAGAR?</button> 
			{% endif %}
		</form>
	m) Porém se clicarmos no botão APAGAR o texto não muda ainda para CONFIRMA?. Isso ocorre porque a VIEW ainda não está passando a variável para o TEMPLATE por meio do CONTEXTO.
		{
            'contact':contact,
            'confirmation':confirmation
        }
	n) Agora ao entrarmos em um contato e clicarmos em APAGAR, o texto do botão muda para CONFIRMA?, mas o registro ainda não é deletado. 
	o) Para entender de forma completa todo o fluxo veja abaixo a squencia:
		1) Ao entrarmos no link de um registro e clicarmos no ID de um registro a URL ( href="{% url 'contact:contact' contact.id %} ) é encontrada no arquivo urls.py. Ao ser encoytrada a VIEW correspondente é acionada;
		2) A VIEW correspondete em urls.py é encontrada -> path('contact/<int:contact_id>/', views.contact, name='contact')
		3) A VIEW (views.contact) então é renderizada, enviando o request, qual TEMPLATE será renderizado ()'contact/contact.html') e o contexto com todas as variáveis trabalhadas na VIEW;
		4) Neste momento então o TEMPLATE contact.html é renderizado. Os dados do registro são mostrados e no fim os botões de ATUALIZAR e APAGAR? serão mostrados.
		5) Mas como o template decide se irá renderizar ATUALIZAR ou APAGAR? A resposta é por meio da variável "confirmation".
		6) Neste primeiro momento ela ainda não existe, então é NULL. Sendo assim no código do TEMPLATE ela cairá no ELSE e renderizará APAGAR

			{% if confirmation == 'no' %}
				<input type="hidden" name="confirmation" value="yes">
				<button class="btn btn-link btn-delete" type"submit">CONFIRMA?</button> 
			{% else %}
				<button class="btn btn-link btn-delete" type"submit">APAGAR?</button> 
			{% endif %}

		7) O botão APAGAR?/CONFIRMA? é na verdade um FORM. Neste primeiro momento seu texto é "APAGAR"

			<form action="{% url 'contact:delete' contact.id %}" method="POST">

		8) Ao ser clicado acionará e renderizará a VIEW contact:delete e enviará o INPUT HIDEN com a variável confirmation com o valor = "yes":

			<input type"hidden" name="confirmation" value="yes">

		9) Ao entrar na VIEW a variável "confirmation" é buscada na linha "confirmation = request.POST.get('confirmation','no')". Como agora o valor é "yes" o registro é deletado e a página redirecionada para o index:

			if confirmation == 'yes':
				contact.delete()
				return redirect('contact:index')
112) Vamos começar a trabalhar com o envio de imagens e usar o campo ImageField.
	a) Para testar, primeiramente adicione uma imagem a um registro (que esteja show) usando o admin
	b) Como já estamos recebendo o contato inteiro na VIEW contact_views.py, no TEMPLATE contact.html podemos mostrar a imagem

		<p>
			<img src="{{ contact.picture.url}}" alt="{{ contact.first_name }} {{ contact.last_name }}">
		</p>

	c) Se clicarmos em um contato sem imge cadastrada, teremos um ERRO: ValueError at /contact/998/ - The 'picture' attribute has no file associated with it.
	Isso ocorrre porque não temos um arquivo lincado em {{ contact.picture.url}}.
	d) Vamos precisar confirmar se a URL existe:

		{% if contact.picture %}
			<p>
				<img src="{{ contact.picture.url}}" alt="{{ contact.first_name }} {{ contact.last_name }}">
			</p>
		{% endif %}
	e) Agora quando clicamos em ATUALIZAR e abrirmos href= {% url 'contact:update' contact.id %}, também vamos precisar adicionar o campo de imagem. Fazemos isso editando e adicionando o campo no forms.py, em sua classe META

		class Meta:
			model = models.Contact
			fields = (
						'first_name', 'last_name', 'phone',
						'email', 'description', 'category',
						'picture'
			)
		
	f) O DJango já adiciona campos de edição da imagem no FORM, em um formato simplificado e padrão dele, apenas expondo a URL da imagem e um botão para alterar ou adicionar uma imagem. Mas vamos exibir a imagem e não a URL e manter o botão.
	g) Para alterar o formato do campo PICTURE vamos precisar mudar seu WidGet:

		 picture = forms.ImageField(
			widget=forms.FileInput(
				attrs={
					'acceps': 'image/*'
				}
			)
		)
	h) Porém com esta mudança, quando já temos uma imagem ela NÃO está sendo mostrada. Para resolver isso vamos alterar o TEMPLATE create.html, que é onde o formulário é rederizado: -> Se o campo for o Picture e existir um valor na URL da imagem

		{% if field.name == 'picture' and field.value.url %}
            <div class="form-group">
              <img src="{{ field.value.url }}" alt="">
            </div>
        {% endif %}

	i) Se tentarmos mudar a imagem pelo formulário (e não pelo admin), escolhendo uma nova imagem e clicando no botão enviar, nada acontecerá. Isso ocorre pelo fato de que no contexto da VIEW contact_forms.py não estamos entregando os Arquivo, apenas o POST. Mas corrigiremos isso:

		 form = ContactForm(request.POST, request.FILES)
			context = {
				'form' : form,
				'form_action' : form_action,
			}

	j) Em todo lugar no código que estivermos entregando POST devemos entregar FILES:

		if request.method == "POST":
        	form = ContactForm(request.POST, request.FILES,instance=contact)
			...


	k) Não esqueça que para que tudo funcione, é necessário que no TEMPLATE, neste caso no create.html, tenhamos "enctype="multipart/form-data""

		<form 
			action="{{ form_action }}"
			method="POST"
			enctype="multipart/form-data"
		>
	
	l) Agora ao enviar um novo arquivo ele será trocado no formulário.
	m) OBSRVAÇÃO - por padrão ao deletar um registro que possui imagem, o arquivo da imagem não é de fato excluído do servidor, da pasta Media/pictures/...
	
		Algumas abordagens caso queira a exclusão:

		
		1) Sobrescrever o método delete do modelo: Você pode sobrescrever o método delete do seu modelo para excluir fisicamente o arquivo do sistema de arquivos quando o registro for excluído. Isso garantiria que, sempre que um objeto desse modelo for excluído, sua imagem associada também seja excluída.

		2) Sinal post_delete: Django fornece sinais que podem ser usados para executar ações após certos eventos, como a exclusão de um registro. Você pode conectar um sinal post_delete ao seu modelo, que acionaria uma função para excluir o arquivo de imagem após o registro ser excluído do banco de dados.

		3) Tarefas agendadas para limpeza: Em alguns casos, pode ser útil manter as imagens por um certo tempo após a exclusão do registro (por exemplo, para permitir recuperação ou por razões de cache). Neste caso, você pode implementar uma tarefa agendada que periodicamente verifica e exclui arquivos de imagem que não estão mais associados a nenhum registro ativo no banco de dados.

113) Agora vamos começar a construir o formulário de cadastro de usuários, que serão os donos dos contatos (owner)
	a) O OWNER será um usuário logado em nosso site, porém antes temos que permitir que este usuário seja criado, para depois logar e usar.
	b) No arquivo dos dormulários (forms.py) vamos usar formulário que o DJango já possui especificamente para criar usuários.
	c) Primeiramente vamos importar o módulo necessário:

		# Este é um formulário pronto que já cria usuário
		from django.contrib.auth.forms import UserCreationForm
	
	d) Vamos criar o formulário (se não quisermos muitos detalhes e alterações no usuário, isso já seria o suficiente para criar um usuário)

		class RegisterForm(UserCreationForm)
			...
	
	e) Para renderizar o FORM vamos precisar de um TEMPLATE. Vamos usar como modelo o TEMPLATE create.html. Duplique o arquivo e renomeie para register.html

		OBS: poderiamos usar o estratégia de PARTIAL e usar {% include %} no Template final

	f) Faça as alterações necessáris:
		1) Mude o nome para Registro de Usuário
		2) Retire enctype="multipart/form-data", pois não vamos trabalhar com envio de arquivos
		3) Retire a parte que mostra a imagem:

			{% comment %} Caso tenhamos uma imagem cadastrada para o contato ela será mostrada {% endcomment %}
			{% if field.name == 'picture' and field.value.url %}
				<div class="form-group">
				<img src="{{ field.value.url }}" alt="">
				</div>
			{% endif %}

		4) 
	g) Precisaremos de uma VIEW para renderizar o TEMPLATE
		1) Em .\views vamos criar user_forms.py
		2) NÂO ESQUEÇA de adicinar esta VIEW em __init__.py
		3) Escreva o código da nova VIEW:

			from django.shortcuts import render
			def register(request):
				return render(
					request,
					'contact/register.html'
				)
		4) Adicione o PATH na URL em urls.py:

			# USER (avos ter create, update e delete)
    		path('user/create/', views.register, name='register'),

		5) Podemos abrir agora a URL no navegador e teremos algo básico (apenas título e botão) -> http://127.0.0.1:8000/user/create/

		6) Ainda não temos de fato um formulário porque a VIEW não está criando e passando este formulário. Vamos fazer isso então:

			from django.shortcuts import render
			from contact.forms import RegisterForm

			def register(request):
				
				form = RegisterForm()

				return render(
					request,
					'contact/register.html',
					{
						'form':form
					}
				)

		7) Neste momento ao atualizar com F5 teremos um formulário de cadastro de usuário. Está tudo em INGLES. Para passar para PT-BR vá em .\project\settings.py e ative USE_I18N = True

		8) Agora, antes de fato de cadastrar um novo usuário precisamos usar IS_VALID para valodar e salvar o usuário

			if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				form.save()

		9) Este usuário terá apenas nome e senha. Vamos querer forçar o preenchimento de primeiro e último nome e e-mail. Ele estará ativo mas não será um membro de equipe e não terá um status de superusuário
114) Vamos validar os campos de cadastro de usuário:
	a) Vamos adicionar primeiro nome, último nome e endereço de e-mail no form de cadastro de usuário:
	b) Tudo está sendo criado meio que automático usando a herança de UserCreationForm, pois lá temos a classe Meta;
	c) Se criarmos a classe Meta em nosso código, teriamos que redefinir tudo "na unha". Receberemos um erro "ModelForm has no model class specified."
		1) Precisamos informar qual o MODEL. Em forms.py adicione:

			from django.contrib.auth.models import User 
		
		2) Na classe Meta precisamos informar o MODEL e os FIELDS (que é uma Tupla):

			class Meta:
				model = User
				fields = (
					'first_name', 'last_name', 'email',
					'username', 'password1', 'password2'
				)
		3) O DJANGO controla por padrão a duplicidade apenas de USERNAME. Para o email é permitida a duplicidade, mas vamos mudar isso:

			# garante que o e-mail será preenchido
			if not email:
				self.add_error(
					'email',
					ValidationError('O email não pode ser vazio', code='invalid')
				)
			
			
			# Isso retornará um TRUE se o email existir e for digitado algo no campo
			if User.objects.filter(email=email).exists() and email:
				self.add_error(
					'email',
					ValidationError('Já existe este e-mail', code='invalid')
				)
			return email

		4) Vamos garantir também que first_name e last_name sejam preenchidos:
		
			first_name = forms.CharField(
				required=True,
				min_length=3,

				# Podemos mudar as mensagens de erro:
				# error_messages={
				#     'required':"erro bla bla"
				# }
			)

			last_name = forms.CharField(
				required=True,
				min_length=3,
			)
115) O DJANGO possui um sistema de FLASH Messages (mensagens rápidas). São mensagens que enviamos de onde quisermos, geralmente de uma VIEW. Esta mensagem ficará em uma sessão e só deixará de existir quando for exibida em um TEMPLATE.
	a) Vamos adicionar uma FLASH Message na VIEW user_forms.py de teste;
	b) Primiro precisamos importar o módulo:

		from django.contrib import messages

	c) Vamos enviar a mensagem da VIEW  user_forms.py:

		 messages.info(request, 'Um texto qualquer')

	d) Porém agora se rodarmos o programa e mansegam ainda não aparece. Isso ocorre porque não capturamos e mensagem em nenhum lugar. Vamos fazer isso.
	e) Como vamos usar mensagens em diversos lugares, vamos criar um TEMPLATE PARTIAL:
		1) Crie o arquivo _messages.html na pasta ..\partials\
		2) Entre com o código:

			{% if messages %}
				{% for message in messages %}
				{% comment %} message.tags são as classes CSS que vem por padrão com as mesagens (temos para error, info, succes, warning e debug) {% endcomment %}
					<div class="message {{ message.tags}}">
						{{ message}}
					</div>
				{% endfor %}
			{% endif %}
		3) Adicione o partials nao base.html com INCLUDE:

			{% include "global/partials/_messages.html" %}
		
		4) Agora quando o usarmos a view user_forms.py e enviarmos uma mensagem, quando qualquer template for renderizado, amensagem será mostrada e deletada da lista de mensagems a serem exibidas

		5) Precisamos apenas de adicionar o CSS para message.info no arquivo:

			 .message.info {
				background: rgba(0, 0, 255, 0.3);
				border: 1px solid rgba(0, 0, 255, 0.3);
			} 
		6) Vamos colocar a mensagem em um local de fato útil, informando que salvamos os dados com sucesso:

			if form.is_valid():
				form.save()
				messages.success(request, 'Usuário registrado com sucesso!')

		7) Porém ao salvar vamos renderizar a VIEW contact:index. Para tal vamos importar REDIRECT:

			from django.shortcuts import render, redirect

			if form.is_valid():
				form.save()
				messages.success(request, 'Usuário registrado com sucesso!')
				return redirect('contact:index')

		ATENÇÂO: a mesagem aparecverá no primero template renderizado, neste caso no INDEX
116) Criando um sistema de LOGIN/ LOGOUT autenticado pelo DJANGO
	a) Antes vamos tornar o TEMPLATE register.html em um PARTIAL:
		1) Em .\templates\contact\ crie uma pasta "partials"
		2) Nesta pasta crie um template parcial de nome "_user-form.html"
		3) Retorne o template registre.html e recorte o <form> por completo, deixando apenas:

			{% extends 'global/base.html' %}
			{% block content %}
			<div class="form-wrapper">

				<h2>Registro de Usuário</h2>

				
			</div>
			{% endblock content %}
		4) Cole o código recortado em ..\partial\_user-form.html
		6) Em register.html realize o include para retonar a ter o código completo:

			{% extends 'global/base.html' %}
			{% block content %}
			<div class="form-wrapper">

				<h2>Registro de Usuário</h2>
				 {% include "contact/partials/_user-form.html" %}
				
			</div>
			{% endblock content %}

		7) Acesso o formulário para testar se está tudo ok -> http://127.0.0.1:8000/user/create/
	b) Vamos agora criar a url de loguin -> http://127.0.0.1:8000/user/login/, a qual ainda não existe
		1) Vamos duplicar "register.html" e renomear para login.html
		2) Apenas altere o <h2> para "Login de Usuário"
	c) Precisamos de uma VIEW para esse login:
		1) Em ..\views\user_forms.py defna um novo método para essa view

			def login_form(request):
				return render(
					request,
					'contact/login.html',
					{
						'form':form
					}
				)
		2) Vamos precisar definir este "form" para enviar ao template. O DJango já possui um formulário de autenticação pronto:
			a) Importe este form na view ->  from django.contrib.auth.forms import AuthenticationForm
			b) Vamos criar o form, sabendo que neste caso o primeiro parãmetro não é data e sim request

				form = AuthenticationForm(request)

			c) Vamos validar o form:

				if request.method == 'POST':
					form =  AuthenticationForm(request, data=request.POST)
					if form.is_valid():
						...
			d) Se o form for válido pegamos o usuário. Atenção, ainda não está ocorrendo o login e a autenticação

					if form.is_valid():
            			user = form.get_user()
						print(user)
					else:
            			messages.error(request, 'Login inválido')

		3) Antes de fazer um primeiro teste precisamos criar a URL
		4) Podemos agora testar o formulário de login -> http://127.0.0.1:8000/user/login/
		5) Vamos agora de fato fazer a autenticação para realizar o login do uruário:
			a) Vamos precisar importar "auth". Neste pacote temos tudo relacionado a autenticação e login -> from django.contrib import messages, auth 
			b) Agora de fato executamos o login

		5) Considerando que no template login.html temos acesso ao USER que está logado na página ou se não existe login, podemos criar uam condicional

			{% if user.is_authenticated %}
				<p>
					Você está logado como {{ user.username }}.
					Clique <a href="">aqui</a>
					para sair.
				</p>
			{% else %}
				{% include "contact/partials/_user-form.html" %}
			{% endif %}

			#Agora se estivermos logado renderiza informando o login e dará um link para LOGOUT, caso contrário renderiza o formulário de login
		6) Vamos criar uma URL de logout =>  path('user/logout/', views.logout_view, name='logout'),
		7) vamos criar a VIEW de logout em user_forms.py:

			def logout_view(request):
				auth.logout(request)
				return redirect('contact:login') 
		8) vamos agora inserir a URL do href do template login.html:

			<p>
				Você está logado como {{ user.username }}.
				Clique <a href="{% url 'contact:logout' %}">aqui</a>
				para sair.
			</p>
		9) Vamos dar uma alterada na view "login_view" para redirecionar para o index em caso de sucesso no login e dar uma mensagem

			if form.is_valid():
				user = form.get_user()
				auth.login(request, user)
				messages.success(request, "Logado com sucesso!")
				return redirect('contact:index')
			messages.error(request, 'Login inválido')

			OBS:
			1) O else foi retirado porque se entrar no if dá o retorno e muda o fluxo, não passando por messages.error(...)
			2) Agora de acessarmos http://127.0.0.1:8000/user/login/ teremos a informação de "Você está logado como NOME DO USUÁRIO. Clique aqui para sair", ou para a página de login se não logado.
117) Vamos agora permitir que os dados de USUÁRIO sejam editados:

	IMPORTANTE: para que possamos editar os dados de USUÁRIO, vamos ter que garantir que estejamos logado

	a) Primeiramente vamos criar um novo FORM e não vamos usar o mesmo da criação do usuário, até mesmo para fazer alguma alteração caso queiramos:

		class RegisterUpdateForm(forms.ModelForm):
			class Meta:
				model = User
				fields = (
					'first_name', 'last_name', 'email',
					'username', 
				)
			
		OBS: não iremos recuperar os PASSWORDs, até mesmo porque eles estão salvos e pictografados
	
	b) Vamos criar o path para o UPDATE de USUÁRIO

		# Veja que para atualização não estamos recebendo nenhum dado dinâmico, 
		# pois vamos depender do usuário que já deve estar logado
    	path('user/update/', views.user_update, name='user_update'),

	c) Vamos criar a VIEW "user_update" em user_forms.py

		def user_update(request):
			return render(
				request,
				'contact/register.html',
				{
					
				}
			)
	d) Essa VIEW precisa enviar para o TEMPLATE o nosso formulário para ser renderizado, o RegisterUpdateForm:
		1) Importe o formulário -> from contact.forms import RegisterForm, RegisterUpdateForm
		2) Crie o form e envie no render:

			def user_update(request):
				form = RegisterUpdateForm()
				return render(
					request,
					'contact/register.html',
					{
						'form':form
					}
				) 
	e) Tente acessar a URL para testar -> http://127.0.0.1:8000/user/update/
	
	f) Veja que o formulário está vazio, precisamos passar junto com o formulário a instância do usuário logado

		form = RegisterUpdateForm(instance=request.user)

		IMPORTANTE - CASO NÃO ESTEJAMOS LOGADOS TEREMOS UM ERRO -> 'AnonymousUser' object has no attribute '_meta'
	g) Ok, usamos então os dados do usuário já existente. Mas na mesma VIEW vamos ter que testar se novos dados estão sendo enviados. Vamos fazer uma verificação de POST de forma invertida.
		1) Se apenas passamos os dados do usuário que está logado, ou seja, a instância, sem nenhuma alteração:

			if request.method != 'POST':
				return render(
					request,
					'contact/register.html',
					{
						'form':form
					}
				)
		2) Porém se o método for POST, colcamos o POST dentro de DATA e criamos o formulário

			form = RegisterUpdateForm(data=request.POST, instance=request.user)
		
		3) Vamos agora validar os dados antes de salvar, porém também de forma inversa:

			# Retorna sem salvar
			if not form.is_valid():
				return render(
					request,
					'contact/register.html',
					{
						'form':form
					}
				)

			# Salva e retorna
			form.save()

		4) Na classe que cria o formulário RegisterUpdateForm vamos recriar os campos, porém agora com as regras de validação:

			first_name = forms.CharField(
				min_length=2,
				max_length=30,
				required=True,
				help_text='Required.',
				error_messages={
					'min_length': 'Please, add more than 2 letters.'
				}
			)
			last_name = forms.CharField(
				min_length=2,
				max_length=30,
				required=True,
				help_text='Required.'
			)

			password1 = forms.CharField(
				label="Password",
				strip=False,
				widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
				help_text=password_validation.password_validators_help_text_html(),
				required=False,
			)

			password2 = forms.CharField(
				label="Password 2",
				strip=False,
				widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
				help_text='Use the same password as before.',
				required=False,
			)
		5) Teremos um erro em password_validation porque temos que importar um pacote. 

			from django.contrib.auth import password_validation

			Este recurso é que validará as regras de password:

			Sua senha não pode ser muito parecida com o resto das suas informações pessoais.
			Sua senha precisa conter pelo menos 8 caracteres.
			Sua senha não pode ser uma senha comumente utilizada.
			Sua senha não pode ser inteiramente numérica.

		6) Vamos copiar o método de validação do e-mail usado anteriormente:

			def clean_email(self):
				email = self.cleaned_data.get('email')
				
				# garante que o e-mail será preenchido
				if not email:
					self.add_error(
						'email',
						ValidationError('O email não pode ser vazio', code='invalid')
					)
				
				
				# Isso retornará um TRUE se o email existir e for digitado algo no campo
				if User.objects.filter(email=email).exists() and email:
					self.add_error(
						'email',
						ValidationError('Já existe este e-mail', code='invalid')
					)
				return email

			--------------------------------------------------------------------------------
			Porém se analisarmos o código, saberemos que teremos um problema, pois o email que está sendo enviado já existe na base de dados
			e por isso não passará na validação
			--------------------------------------------------------------------------------
		7) Para resolver este problema o usuário tem que estar logado. Como na VIEW estamos passando a instância de user, teremos como comparar o email de quem está logado com o que está enviado no campo
			a) Primeiro capturamos o e-mail atual de USER:
				current_email_user = self.instance.email
			b) Se o email de USER for diferente do email enviado, aí sim verifica se este e-mail pertence a outro usuário. Se for igual não faz nada

				if current_email_user != email:
					# garante que o e-mail será preenchido
					if not email:
						self.add_error(
							'email',
							ValidationError('O email não pode ser vazio', code='invalid')
						)
					
					
					# Isso retornará um TRUE se o email existir e for digitado algo no campo
					if User.objects.filter(email=email).exists() and email:
						self.add_error(
							'email',
							ValidationError('Já existe este e-mail', code='invalid')
					)
				return email

				--------------------------------------------------------------------------------------
				RESULTADO:
				1) Se enviarmos o e-mail que já é do usuário, não faz nada
				2) Se enviarmos o e-mail que já é de outro usuário, dá uma mensagem de erro "Já exist este email"
				3) Se enviarmos o e-mail que não existe na base de dados e diferente do email atual do usuário, salva.
			
			7) Para as senhas a lógica é a mesma usada anteriormente. Temos que validar uma delas (obviamente elas sendo iguais)
				a) Se nenhum password for enviado é porque  não se quer alterar, assim não fazemos nada, mas se for enviado validamos com o pacote que importamos (from django.contrib.auth import password_validation)

				def clean_password1(self):
					password1 =  self.cleaned_data.get('password1')

					# Se não estiver vazio
					if password1:
						try:
							password_validation.validate_password(password1)
						except ValidationError as errors:
							self.add_error(
								'password1',
								ValidationError(errors)
							)
					return password1	
				b) Para o caso das senhas password1 e password2 forem diferentes, vamos implementar o método clean:

					def clean(self):
						password1 = self.cleaned_data.get('password1')
						password2 = self.cleaned_data.get('password2')

						if password1 or password2:
							if password1 != password2:
								self.add_error(
									'password2',
									ValidationError('Senhas não batem')
								)

					LEMBRE:
					    Use clean_<fieldname> para validações que são específicas para um campo individual.
    					Use clean para validações que dependem da relação entre dois ou mais campos, ou para validações gerais que não estão ligadas a um campo específico.

				c) Até então as senhas não estão dendo salvas. Até então estamos só validando as senhas. Agora é que vamos sobrescrever o método save(self):

					def save(self, commit = True):
						cleaned_data = self.cleaned_data
						# Esta linha chama o método save da superclasse (geralmente a classe do formulário ou do modelo) com commit=False. 
						# Isso cria um objeto de modelo (neste caso, um objeto user) com os dados do formulário, mas ainda não salva no banco de dados.
						user = super().save(commit = False)
						password = cleaned_data.get('password1')

						if password:
							# Aqui a senha é criptografada
							user.set_password(password)
						
						# Se estiver definido o commit como TRUE (def save(self, commit = True)), salva a nova senha já criptografada
						if commit:
							user.save()
				d) Agora ao salvar vamos sair do form de atualização do usuário. Fazemos esta alteração na VIEW user_forms.py:

					ANTES:

						# Salva e retorna
						form.save()
						return render(
							request,
							'contact/register.html',
							{
								'form':form
							}
						)
					
					DEPOIS:

						# Salva e retorna
						form.save()
						return redirect('contact:user_update')
			8) Vamos dar uma pequena alterada no template atualmente usado, que é o register.html:
				a) Vamos cuplicar o register.html e nomear para user_update.html
				b) Altere o H2 para -> <h2>Atualização de Usuário</h2>
				c) Vá para a VIEW e nos métodos de update altere o render de 'contact/register.html' para 'contact/user_update.html'
			09) Uma pequena correção. Na função de salvar do form.py da classe RegisterUpdateForm(forms.ModelForm) temps que retornar o usuário, para o caso de precisar deste usuário na VIEW

				 def save(self, commit = True):
					...
					if commit:
						user.save()
					return user


				PARA PEGAR O USER NA VIEW USURIAMOS ALGO COMO:
				user = form.save()
118) Para evitar anomalias na execução da aplicação, temos que garantir que antes de acessar alguns recursos estejamos logados. Veja o resuo abaixo:

	PRECISA ESTAR LOGADO PARA ACESSAR:
	# Contact CRUD
    path('contact/create/', views.create, name='create'),
	# Precisa também ser dona do contato
	path('contact/<int:contact_id>/update', views.update, name='update'),
	path('contact/<int:contact_id>/delete', views.delete, name='delete'),
	# USER (avos ter create, update e delete) / Precisa também ser dona do contato
    path('user/update/', views.user_update, name='user_update'),
	path('user/logout/', views.logout_view, name='logout'),


	NÃO PRECISA ESTAR LOGADO PARA ACESSAR:
	path('', views.index, name='index'),
    path('search/', views.search, name='search'),
	# Contact CRUD
    path('contact/<int:contact_id>/', views.contact, name='contact'),
	# USER (avos ter create, update e delete)
    path('user/create/', views.register, name='register'),
	path('user/login/', views.login_view, name='login'),
	

	a) Vamos ajustar o template parcial _header.html para exibir os links de forma coondicional conforme a situação de estar ou não logado:

		{% if user.is_authenticated %}
            <li class="menu-item">
              <a href="{% url "contact:create" %}" class="menu-link">Cadastrar</a>
            </li>
            <li class="menu-item">
              <a href="{% url "contact:user_update" %}" class="menu-link">Profile</a>
            </li>
            <li class="menu-item">
              <a href="{% url "contact:logout" %}" class="menu-link">Logout</a>
            </li>
        {% else %}
            <li class="menu-item">
              <a href="{% url "contact:login" %}" class="menu-link">Login</a>
            </li>
            <li class="menu-item">
              <a href="{% url "contact:register" %}" class="menu-link">Registrar</a>
            </li>
        {% endif %}
	b) Temos um problema para solucionar. Se alterarmos a senha o DJANGO automaticamente irá deslogar e como estamos redirecionando para 'contact/user_update.html' teremos o erro "AnonymousUser' object has no attribute '_meta", pois assumimos que temos um usuário em "form = RegisterUpdateForm(instance=request.user)", o que não é mais verdade.
	c) Vamos resolver isso com um decorator, mas antes vamos logar de novo (não esqueça que possivelmente vc mudou a senha para o teste)
		1) Poderiamos usar o request.user existente na VIEW para obrigar que o usuário esteja logado para acessar certas VIEW, mas vamos optar pelo uso do DECORATOR para forçar que o usuário esteja logado;
		2) Primeiramente vamos importar o pacote -> from django.contrib.auth.decorators import login_required
		3) Vamos então decorar os métodos das VIEWs que só podem ser acessadas existindo um usuário logado e definir uma url para o direcionamento caso o usuário NÃO esteja logado:

			@login_required(login_url='contact:login')
			def user_update(request):
				...

			@login_required(login_url='contact:login')
			def logout_view(request):
				...

		4) Agora se altearmos a senha, o que vai forçar o LOGOUT, iremos automaticamente ser redirecionados para -> path('user/login/', views.login_view"," name='login'), mesmo que na VIEW "def user_update(request):" estejamos sendo redirecionados para 'contact:user_update'. Isso ocorre porque esta VIEW possui um DECORATOR que exige que o usuário esteja logado e caso não esteja, direciona para 'user:login'

		5) Vamos corrigir outra anomalia, pois não queremos deixar um usuário NÃO LOGADO ter acesso a criação de um novo contato, considerando que cada contato deverá ter um dono. Vamos então usar -> @login_required(login_url='contact:login')  em contact_forms.py:
			a) Primeiro add o pacote -> from django.contrib.auth.decorators import login_required
			b) Depois decore o métodos -> @login_required(login_url='contact:login'):

				@login_required(login_url='contact:login')
				def create(request):
					...

				@login_required(login_url='contact:login')
				def update(request, contact_id):
					...
				
				@login_required(login_url='contact:login')
				def delete(request, contact_id):
					...

			Agora para criar, deletar ou atualizar um contato será preciso estar logado.
		 6) Vamos corrigir outra anomalia, pois para deletar ou atualizar um contato não basta estar logado, mas sim ser o DONO (Owner) deste contato
		 	a) Quando salvarmos um contato vamos atrelar o campo usuário ao campo OWNER (será usada a chave estrangeira)
			b) No arquivo contact_form.py, dentro da VIEW "def create(request)", quando validamos o contato e salvamos, antes de salvar vamos jogar o contato que está sendo salvo na variável "contact":

				# Não salva ainda, pois estamos usando commit=False. Coloca o contato recuperado na variável
            	contact = form.save(commit=False)
			
			c) Vamos atrelar o campo owner do contato ao usuário (como chave estrangeira)

				# Vamos atrelar o CONTATO ao seu dono (ao usuário), registrando o campo OWNER do CONTATO
            	contact.owner = request.user
				contact.save()

			d) Ok, adicionamos o usuário dono do contato, mas um usuário ainda está alterando ou deltando contatos de qualqyer usuário. Isso será feito na View de Update "def update(request, contact_id)". 
			
			e) Nesta View recebemos dados para filtrar o contato que queremos editar.

				contact = get_object_or_404(Contact, pk=contact_id, show=True)

				Inicialmente estamos filtrando apenas pelo "contact_id"

			f) Vamos adicionar mais um filtro, onde o owner dele deverá ser igual ao usuário logado:

				contact = get_object_or_404(Contact, pk=contact_id, show=True, owner = request.user)

			g) Caso na View estiver logado com um usuário que não é dono de um contato tentarmos atualizar um contato, um erro 404 será levantado
				
				-> Page not found (404)

			h) Vamos agora colocar esta mesma regra na View de deleção -> def delete(request, contact_id)

			i) Vamos melhorar um pouco. Nao vamos mostrar os botãoes de atualizar e deletar quando o usuário não for dono do contato. Neste momento se isso ocorrer será gerado um erro 404, o que não é legal. Faremos isso no TEMPLATE "contact.html" onde exibimos o contato.

			j) Iremmos apenas envolver a DIV "<div class="contact-links">" com um IF

				{% if user == contact.owner %}
					<div class="contact-links">
						<a class="btn btn-link" href= {% url 'contact:update' contact.id %}>ATUALIZAR</a>
						<form action="{% url 'contact:delete' contact.id %}" method="POST">
						{% csrf_token %}
						{% if confirmation == 'no' %}
							<input type="hidden" name="confirmation" value="yes">
							<button class="btn btn-link btn-delete" type"submit">CONFIRMA?</button> 
						{% else %}
							<button class="btn btn-link btn-delete" type"submit">APAGAR?</button> 
						{% endif %}
						
						</form>
					</div>
				{% endif %}

119) Vamos agora apenas corrigir a situação que é exigida uma imagem para cadastrar um novo usuário, pois pode ser que queiramos cadastrar um sem uma imagem. Corrigiremos isso com required=False para o campo ImageField:

	picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'acceps': 'image/*'
            }
        ),
        required=False
    )



				









	

   
    
    
     
    


	






	





		
		 












		





\








		 


	
































   











