from django.shortcuts import render


def inicio(request):
    return render(request, 'core/inicio.html')


def agua_y_salud(request):
    return render(request, 'core/agua_y_salud.html')


def equipos(request):
    return render(request, 'core/equipos.html')


def faq(request):
    return render(request, 'core/faq.html')