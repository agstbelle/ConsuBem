from django.urls import path
from . import views 

app_name = "usuarios_app"

urlpatterns = [
    path("", views.index, name="index"),
    path ("cadastrese", views.cadastro, name="cadastre-se"),
    path ("login", views.login, name="login"),

]