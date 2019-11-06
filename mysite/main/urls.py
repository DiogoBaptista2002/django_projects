from django.urls import path

from . import views
urlpatterns = [
    path("comida/", views.comidaView, name="comidaView"),
    path("refeicoes/", views.refeicoesView, name="refeicoesView"),
    path("comida/<int:id>/", views.comidaViewComprar, name="comidaViewComprar"),
    path("refeicoes/<int:id>/", views.refeicoesViewComprar, name="refeicoesViewComprar"),
    path("refeicoes/<int:idRefeicao>/<int:idUser>", views.ConfirmarRefeicao, name="refeicoesConfirmarRefeicao"),
    path("comida/<int:idComida>/<int:idUser>", views.ConfirmarComida, name="Confirmar"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("conta/<int:idUser>", views.conta, name="conta"),
    path("conta/", views.conta1, name="conta1"),
    path("delete/12345", views.delete, name="delete"),
    path("conta/<int:f>/comida/<int:id>/", views.QrCodeComida, name="QrCodeComida"),
    path("conta/<int:f>/refeicoes/<int:id>/", views.QrCodeRefeicoes, name="QrCodeRefeicoes"),
    path("qrcode/<int:f>/comida/<int:id>", views.QrCodeComida1, name="QrCodeComida1"),
    path("qrcode/<int:f>/refeicoes/<int:id>", views.QrCodeRefeicoes1, name="QrCodeRefeicoes1"),
    
]
