from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # Esta variável int:contact_id deve ter o mesmo nome que está na VIEW.
    # Sempre deixe uma "/" no final

    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Contact CRUD
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update', views.update, name='update'),
    path('contact/<int:contact_id>/delete', views.delete, name='delete'),
     
    # USER (avos ter create, update e delete)
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    # Veja que para atualização não estamos recebendo nenhum dado dinâmico, pois vamos depender do usuário que já deve estar logado
    path('user/update/', views.user_update, name='user_update'),
    
]
