# from collections.abc import Mapping
# from typing import Any
from django import forms
from django.core.exceptions import ValidationError
# from django.core.files.base import File
# from django.db.models.base import Model
# from django.forms.utils import ErrorList
from . import models
# Este é um formulário pronto que já cria usuário
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'acceps': 'image/*'
            }
        ),
        required=False
    )

    #Para ter acesso ao WIDGET dos campos vamor recriar o campo. 
    # Essa é a melhor forma, pois também dá acesso a outras configurações, como mudar o LABEL
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #           'placeholder' : 'Escreva Aqui (veio do forms.CharField())...',
    #           'class' : 'classe-a classe-b'
    #         }
    #     ),
    #     label='Primeiro Nome',
    #     help_text= "Texto de ajuda para seu usuário"
    # )

    # Este é um campo avulso, não vinculado ao MODEL
    # qualquer = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #           'placeholder' : 'Este é um campo avulso...',
    #         }
    #     ),
    #     help_text= "Texto de ajuda para seu usuário"
    # )
    
    # Para ter acesso ao WIDGETs dos campos sem criar um novo temos que usar __init__()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_name'].widget.attrs.update(
        #     {'placeholder' : 'Escreva Aqui (veio do init)...',
        #      'class' : 'classe-a classe-b'
        #     }
        # )

    class Meta:
        model = models.Contact
        fields = (
                    'first_name', 'last_name', 'phone',
                    'email', 'description', 'category',
                    'picture'
        )



        # Isso transforma o campo em password (type = password)
        # widgets = {
        #     'first_name' : forms.PasswordInput()
        # }

      
        # Aqui CRIAMOS o WIDGETS para alterar os atributos dos campos
        # widgets = {
        #     'first_name' : forms.TextInput(
        #         attrs={
        #             'placeholder' : 'Escreva Aqui...',
        #             'class' : 'classe-a classe-b'
        #         }
        #     )
        # }

    # Este método tem acesso aos dados do formulário antes de serem enviados (teremos um dicionário com os dados enviados)
    # O método clean é usado para validar ou modificar dados de formulários antes de serem salvos ou processados. 
    def clean(self):
        
        cleaned_data = self.cleaned_data
        # print(cleaned_data)


        # Vamos validar se os campos first_name e last_name são iguais
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        print("self.cleaned_data: ", self.cleaned_data)
        print("first_name: ", first_name)

        if first_name == last_name:
            msg = ValidationError('O primeiro nome e o segundo n ome não podem ser iguais', code = 'invalid')
            self.add_error('first_name', msg) 
            self.add_error('last_name', msg) 

        # Vamos add um erro
        # add_error recebe o campo que vamos adicionar o erro. Se não adicionarmos campo, o erro será de formulário
        #  POdemos ter várias validações no mesmo campo       
        # self.add_error(
        #     'first_name', 
        #     ValidationError(
        #         'Mensagem de erro',
        #         code = 'invalid' # Estes códigos podem ser criados
        #     ) 
        # ) 

        # self.add_error(
        #     'first_name', 
        #     ValidationError(
        #         'Mensagem de erro 2',
        #         code = 'invalid' # Estes códigos podem ser criados
        #     ) 
        # ) 

        # Vamos adiconar também erros de formulário - nonfiled errors

        # self.add_error(
        #     None, 
        #     ValidationError(
        #         'Erro de formulário 1 (nonfield errors)',
        #         code = 'form_error' # Estes códigos podem ser criados
        #     ) 
        # ) 

        # self.add_error(
        #     None, 
        #     ValidationError(
        #         'Erro de formulário 1 (nonfield errors)',
        #         code = 'form_error' # Estes códigos podem ser criados
        #     ) 
        # ) 

        # Retornar para a super classe garante que a validação padrão do formulário ainda ocorra
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        # print("Passei no clean do first_name - ", first_name)

        if first_name == 'ABC':

            # O Uso de raise lança um erro e pára o código, por isso se tver mais validações eles não serão processados
            # Por isso essa não é a melhor forma, mas sim o uso de self.add_error(...)
            # raise ValidationError(
            #     'Não digite ABC neste campo',
            #     code='invalid'
            # )
        
            self.add_error(
                'first_name', 
                ValidationError(
                    'Não inclua ABC neste campo (veio do self.add_error)',
                    code = 'invalid' # Estes códigos podem ser criados
                ) 
            ) 

        return first_name

class RegisterForm(UserCreationForm):
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

    email = forms.EmailField(
        # Aqui tb podemos validar o email previamente, recriando o campo
    )

    class Meta:
        model = User
        fields = (
              'first_name', 'last_name', 'email',
              'username', 'password1', 'password2',
          )
          
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

class RegisterUpdateForm(forms.ModelForm):

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

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 
        )

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
        
        return user
       

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email_user = self.instance.email
        
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
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )
            

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