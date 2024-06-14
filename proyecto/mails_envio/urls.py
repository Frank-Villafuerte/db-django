from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('enviar_mail', views.email,name='enviar_mail'),
    path('pdf', views.pdf_view,name='pdf'),
    #path('', views.index,name='index'),
    #path('', views.index,name='index'),
]