# from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
#from django.db.models import Q
from contact.forms import ContactForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# from django import forms
# from django.core.exceptions import ValidationError

# MOVIDO PARA O .\CONTACT\FORMS.PY

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = (
#                     'first_name', 'last_name', 'phone',
#                 )
#     # Este método tem acesso aos dados do formulário antes de serem enviados (teremos um dicionário com os dados enviados)
#     # O método clean é usado para validar ou modificar dados de formulários antes de serem salvos ou processados. 
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         print(cleaned_data)

#         # Vamos add um erro
#         # add_error recebe o campo que vamos adicionar o erro. Se não adicionarmos campo, o erro será de formulário
#         #  POdemos ter várias validações no mesmo campo       
#         self.add_error(
#             'first_name', 
#             ValidationError(
#                 'Mensagem de erro',
#                 code = 'invalid' # Estes códigos podem ser criados
#             ) 
#         ) 

#         self.add_error(
#             'first_name', 
#             ValidationError(
#                 'Mensagem de erro 2',
#                 code = 'invalid' # Estes códigos podem ser criados
#             ) 
#         ) 

#         # Vamos adiconar também erros de formulário - nonfiled errors

#         self.add_error(
#             None, 
#             ValidationError(
#                 'Erro de formulário 1 (nonfield errors)',
#                 code = 'form_error' # Estes códigos podem ser criados
#             ) 
#         ) 

#         self.add_error(
#             None, 
#             ValidationError(
#                 'Erro de formulário 1 (nonfield errors)',
#                 code = 'form_error' # Estes códigos podem ser criados
#             ) 
#         ) 

#         # Retornar para a super classe garante que a validação padrão do formulário ainda ocorra
#         return super().clean()


@login_required(login_url='contact:login')
def create(request):
    # Com isso saberemos qual a URL que está acessando esta VIEW
    form_action = reverse('contact:create')

    # if request.method == "POST":
    #     print('--------------------------------------')
    #     print(request.method)
    #     print(request.POST.get('first_name'))
    #     print(request.POST.get('last_name'))
    #     print('--------------------------------------')
    # else:
    #     print('--------------------------------------')
    #     print(request.method)
    #     print('--------------------------------------')

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form' : form,
            'form_action' : form_action,
        }

        # Caso não exista nenhum erro adicionado, o formulário será validado
        if form.is_valid():
            # print('Formulário é valido')
            # form.save()
            # Aqui vamos redirecionar para a contatc:create e abrir o formulário em branco, evitand que possamos clicar diversas vezes em salvar e salvar o contato 
            # diversas vezes. Isso enqunto não criamos a VIEW de edição
            #return redirect('contact:create')

            # Não salva ainda, pois estamos usando commit=False. Coloca o contato recuperado na variável
            contact = form.save(commit=False)
            # Vamos atrelar o CONTATO ao seu dono (ao usuário), registrando o campo OWNER do CONTATO
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id = contact.pk)


        # Se chegar aqui é porque existe erro nos campos e por isso será renderizado nomanete a VIEW CREATE
        return render(
            request,
            'contact/create.html',
            context
        )
    # Else  (NÃO TEMOS NENHUM POST)
    context = {
        'form' : ContactForm(),
        'form_action' : form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def update(request, contact_id):
    # "owner = request.user" como parâmetro de filtro garante que apenas usuários donos deste contato possam atualizar o mesmo
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner = request.user)
    # Com isso saberemos qual a URL que está acessando esta VIEW, porém é preciso pasar os argumentos dinâmicos também
    form_action = reverse('contact:update', args=(contact_id,))


    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES,instance=contact)
        context = {
            'form' : form,
            'form_action' : form_action,
        }


        if form.is_valid():

            contact = form.save()

            return redirect('contact:update', contact_id = contact.pk)



        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form' : ContactForm(instance=contact),
        'form_action' : form_action,
    }

    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    # "owner = request.user" como parâmetro de filtro garante que apenas usuários donos deste contato possam deletar o mesmo
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner = request.user)
    confirmation = request.POST.get('confirmation','no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(
        request,
        'contact/contact.html',
        {
            'contact':contact,
            'confirmation':confirmation
        }
    )
