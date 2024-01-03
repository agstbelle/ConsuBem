from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('cadastro', views.cadastro, name="cadastro"),
    path ('login', views.user_login, name="login"),
    path ('dashboard', views.dashboard_admin, name="dashboard"),
    path ('cadastro_produto', views.cadastro_produto, name="cadastro_produto"),
    path ('cadastro_admin', views.cadastro_admin, name="cadastro_admin"),
    path ('troca_item', views.troca_item, name="troca_item"),
]