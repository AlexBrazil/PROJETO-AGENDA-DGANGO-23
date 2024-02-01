import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
# Aqruivo de configuração de nosso projeto
from django.conf import settings

# Esta proxima linha faz com que o python enxerge as pastas anteriores, indo até o raiz
DJANGO_BASE_DIR = Path(__file__).parent.parent


NUMBER_OF_OBJECTS = 1000

# Aqui fazemos com que o python insira no PATH as pastas desde a RAIZ do projeto
sys.path.append(str(DJANGO_BASE_DIR))

# Como não vamos configurar o DJANGO passando pelo manage.py, precisamos executar esta linha
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

# Estava dando um erro na configuração do Time Zone, por isso desabilitamos
settings.USE_TZ = False

# Iniciamos o SETUP do DJANGO
django.setup()

if __name__ == '__main__':
    # Tem que ser instalado no Ambiente Virtual
    import faker

    # Importa os models
    from contact.models import Category, Contact

    # Cuidado com estes comandos, apagam tudo das tabelas
    Contact.objects.all().delete()
    Category.objects.all().delete()

    fake = faker.Faker('pt_BR')

    # Kista para criar as categorias
    categories = ['Amigos', 'Família', 'Conhecidos']

    # Estamos criando as categorias usando uma List comprehension
    django_categories = [Category(name=name) for name in categories]

    # Como a criação acoma é LAZY, temos que salvar cada uma
    for category in django_categories:
        category.save()

    # Lista para os contatos
    django_contacts = []

    # Aqui criamos os 1000 contatos, usando as informações criadas pelo FAKER
    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        # Como faker fornece um nome único, tivemos que quebrar
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        # Adicionamos o contato na lista (é lazy)
        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    # S de fato formarm criados contatos
    if len(django_contacts) > 0:
        # ...bulk_create -> salva e, uma tacada só todos os contatos. È o mesmo que dar um save() em cada contato, porem sem ter que executar 1000  Query de salvamento na base
        Contact.objects.bulk_create(django_contacts)