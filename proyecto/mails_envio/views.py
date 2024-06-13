from django.shortcuts import render
from django.core.mail import send_mail
def index(request):
    send_mail(
    "Mensaje Django",
    "El mensaje se ha enviado exitosamente.",
    "prositofrank@gmail.com",
    ["fvillafuerte@unsa.edu.pe"],
    fail_silently=False,
)
    return render(request, 'mails_envio/index.html')
