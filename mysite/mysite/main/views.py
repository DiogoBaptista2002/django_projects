from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Refeicoe, Comida, CustomUser
import re
from .forms import CreateNewList
from collections import Counter, OrderedDict


# Create your views here.
def comidaView(request):
    ls = Comida.objects
    return render(request, "main/comida.html", {"ls": ls})


def refeicoesView(request):
    fs = Refeicoe.objects
    return render(request, "main/refeicoes.html", {"fs": fs})

def comidaViewComprar(request, id):
    if request.user.is_authenticated == True:
        lc = Comida.objects.get(id=id)
        return render(request, "main/comidacomprar.html", {"lc": lc})
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/login")

def ConfirmarComida(request, idUser, idComida):
    current_user = request.user.id
    if current_user == idUser:
        utilizador = CustomUser.objects.get(id=idUser)
        custo = Comida.objects.get(id=idComida)
        marcar = [utilizador.marcacoes]
        if custo.comida in utilizador.marcacoes:
            f = "Já Comprou"
            return render(request, "main/jaMarcou.html", {"f": f})
        else:
            marcar.append(custo.comida)
            utilizador.marcacoes = marcar
            saldoAtual = utilizador.balance - custo.preco
            utilizador.balance = saldoAtual
            utilizador.save()
            return render(request, "main/home.html", {"saldoAtual": saldoAtual})
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/login")


def ConfirmarRefeicao(request, idUser, idRefeicao):
    current_user = request.user.id
    if current_user == idUser:
        utilizador = CustomUser.objects.get(id=idUser)
        custo = Refeicoe.objects.get(id=idRefeicao)
        marcar = [utilizador.marcacoes]
        if custo.dia + "- " + custo.prato in utilizador.marcacoes:
            return render(request, "main/jaMarcou.html", {})
        else:
            marcar.append(custo.dia + "- " + custo.prato)
            utilizador.marcacoes = marcar
            saldoAtual = utilizador.balance - custo.preco
            utilizador.balance = saldoAtual
            utilizador.save()
            return render(request, "main/home.html", {"saldoAtual": saldoAtual})
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/login")


def refeicoesViewComprar(request, id):
    if request.user.is_authenticated == True:
        fc = Refeicoe.objects.get(id=id)
        return render(request, "main/comidarefeicoes.html", {"fc": fc})
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/login")

def home(response):
    return render(response, "main/home.html", {})

def conta(request, idUser):
    current_user = request.user.id
    if current_user == idUser:
        if idUser == 1:
            b = True
            marcar = []
            utilizador = CustomUser.objects
            for object in utilizador.all():
                i = object.marcacoes
                s = i.replace('"', '')
                s = s.replace("'", '')
                s = s.replace('[', '')
                s = s.replace(']', '')
                s = s.replace('\\', '')
                s = s.replace(',', '\n')
                h = s.split("\n")
                del h[0]
                h = tuple(h)
                marcar.append(h)

            marcar2 = []
            for x in marcar:
                for y in x:
                    if y != " ":
                        marcar2.append(y)


            u = Counter(marcar2)
            f = str(u.most_common)
            f = f.replace('<bound method Counter.most_common of Counter({', '')
            f = f.replace('})>', '')
            f = f.replace("'", '')
            f = f.replace(',', '\n')
            f = f.replace('<bound method Counter.most_common of Counter()>', 'Nada')
            
            return render(request, "main/conta.html", {"x": f, "b": b})

        else:
            b = False
            utilizador = CustomUser.objects.get(id=idUser)
            i = utilizador.marcacoes
            s = i.replace('"', '')
            s = s.replace("'", '')
            s = s.replace('[', '')
            s = s.replace(']', '')
            s = s.replace('\\', '')
            s = s.replace(',', '\n')
            h = s.split("\n")
            del h[0]
            f = Comida.objects
            u = Refeicoe.objects

            return render(request, "main/conta.html", {"h": h, "f": f, "u": u, "b": b})


def QrCodeComida(response, id, f):
    i = str("http://127.0.0.1:8000/qrcode/"+str(f)+"comida/"+str(id))
    return render(response, "main/qrcode.html", {"i": i})

def QrCodeRefeicoes(response, id, f):
    i = str("http://127.0.0.1:8000/qrcode/"+str(f)+"/refeicoes/"+str(id))
    return render(response, "main/qrcodeRefeicoes.html", {"i": i})

def QrCodeComida1(request, id, f):
    current_user = request.user.id
    if current_user == f:
        i = Comida.objects.get(id=id)
        i = str(i)
        f = CustomUser.objects.get(id=f)
        h = str(f.marcacoes)
        h = h.replace(i, '')
        f.marcacoes = h
        f.save()
        return render(request, "main/qrcodeOK.html", {"i": i})
    return render(request, "main/qrcodeOk.html", {})

def QrCodeRefeicoes1(request, id, f):
    current_user = request.user.id
    print("ola")
    if current_user == f:
        i = Refeicoe.objects.get(id=id)
        i = str(i.dia+"- "+i.prato)
        f = CustomUser.objects.get(id=f)
        h = str(f.marcacoes)
        h = h.replace(i, '')
        f.marcacoes = h
        f.save()
        return render(request, "main/qrcodeOk.html", {"i": i})
    return render(request, "main/qrcodeOk.html", {})

def conta1(request):
    if request.user.is_authenticated == True:
        return render(request, "main/conta.html", {})
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/login")


def delete(response):
    current_user = request.user.id
    if current_user == 1:
        for object in CustomUser.objects.all():
            object.marcacoes = ""
            object.save()
        return render(response, "main/home.html", {})


