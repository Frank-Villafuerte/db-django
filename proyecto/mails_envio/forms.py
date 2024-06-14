import datetime
from django import forms

class EmailForm(forms.Form):
    asunto = forms.CharField(widget=forms.TextInput)
    contenido = forms.CharField(widget=forms.Textarea)


class InvoiceForm(forms.Form):
    amount = forms.DecimalField(max_digits=5, decimal_places=2)
    customer_name = forms.CharField(max_length=100)
    invoice_number = forms.IntegerField()
