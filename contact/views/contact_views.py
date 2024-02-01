from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
# from django.http import Http404
from django.db.models import Q

def index(request):
    contacts = Contact.objects \
        .filter(show=True) \
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    print(contacts.query)

    context = { 
        'page_obj' : page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.get(id=contact_id)
    # single_contact = Contact.objects.filter(id=contact_id).first()
    single_contact = get_object_or_404(Contact, id=contact_id, show=True)
    #single_contact = get_object_or_404(Contact.objects.filter(id=contact_id))

    # if single_contact is None:
    #     raise Http404()

    # print(single_contact.query)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    context = { 
        'contact' : single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request):

    search_value = request.GET.get('q', '').strip()
    print(search_value)

    if search_value == "" :
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True) \
        .filter(
            Q(first_name__icontains = search_value) |
            Q(last_name__icontains = search_value) |
            Q(phone__icontains = search_value) |
            Q(email__icontains = search_value)
        ) \
        .order_by('-id') # [0:20]
    
    print(contacts.query)

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = { 
        'page_obj' : page_obj,
        'site_title': 'Procurando - ',
        'search_value' : search_value
    }

    return render(
        request,
        'contact/index.html',
        context
    )
