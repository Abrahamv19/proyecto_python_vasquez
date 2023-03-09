from django.shortcuts import render
from BlogFinanciero.models import Post_temas
from BlogFinanciero.forms import TemasForm, BloguerosForm, LectoresForm

def index(request):
    return render(request, "BlogFinanciero/index.html")

def blogueros(request):
    context = {
        "form": BloguerosForm(),
    }
    return render(request, "BlogFinanciero/blogueros.html", context)

def temas(request):
    context = {
        "form": TemasForm(),
    }
    return render(request, "BlogFinanciero/temas.html", context)

def lectores(request):
    context = {
        "form": LectoresForm(),
    }
    return render(request, "BlogFinanciero/lectores.html", context)

def agregar_temas(request):
    temas_form = TemasForm(request.POST)
    temas_form.save()
    context = {
        "form": TemasForm(),
        "temas": Post_temas.objects.all(),
    }
    return render(request, "BlogFinanciero/temas.html", context)

def agregar_blogueros(request):
    blogueros_form = BloguerosForm(request.POST)
    blogueros_form.save()
    context = {
        "form": BloguerosForm()
    }
    return render(request, "BlogFinanciero/blogueros.html", context)

def agregar_lectores(request):
    lectores_form = LectoresForm(request.POST)
    lectores_form.save()
    context = {
        "form": LectoresForm()
    }
    return render(request, "BlogFinanciero/Lectores.html", context)

def mostrar_temas(request):
    context = {
        "form": TemasForm(),
        "temas": Post_temas.objects.all(),
    }
    return render(request, "BlogFinanciero/temas.html", context)

def buscar_tema(request):
    criterio = request.GET.get("criterio")
    context = {
        "temas": Post_temas.objects.filter(tema__icontains=criterio).all(),
    }
    return render(request, "BlogFinanciero/index.html", context)




