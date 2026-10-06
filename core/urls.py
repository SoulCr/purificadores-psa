from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agua-y-salud/', views.agua_y_salud, name='agua_y_salud'),
    path('nuestros-equipos/', views.equipos, name='equipos'),
    path('preguntas-frecuentes/', views.faq, name='faq'),
]