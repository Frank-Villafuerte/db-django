import datetime
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

from django.http import Http404

from . import renderers
def index(request):
    return render(request, 'mails_envio/index.html')

'''def email(request):
    send_mail(
    "Mensaje Django",
    "El mensaje se ha enviado exitosamente.",
    "prositofrank@gmail.com",
    ["fvillafuerte@unsa.edu.pe"],
    fail_silently=False,
    )
    return render(request, 'mails_envio/enviar_mail.html')'''

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            asunto=form.cleaned_data['asunto']
            send_mail(
                asunto,
                contenido,
                'prositoelmo@gmail.com',
                ['fvillafuerte@unsa.edu.pe'],
            )
            return render(request, 'mails_envio/enviar_mail.html')
    else:
        form = EmailForm()
    return render(request, 'mails_envio/enviar_mail.html', {'form': form})

def pdf_view(request, *args, **kwargs):
    data = {
        'date': datetime.date.today(), 
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'invoice_number': 1233434,
    }
    return renderers.render_to_pdf('mails_envio/invoice.html', data)
