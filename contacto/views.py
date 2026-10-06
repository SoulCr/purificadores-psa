from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ConsultaForm


def contacto(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias! Recibimos tu consulta y un asesor se va a comunicar con vos.')
            return redirect('contacto:contacto')
    else:
        form = ConsultaForm()
    return render(request, 'contacto/contacto.html', {'form': form})