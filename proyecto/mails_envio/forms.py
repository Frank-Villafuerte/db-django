from django import forms

class EmailForm(forms.Form):
    asunto = forms.CharField(widget=forms.TextInput)
    contenido = forms.CharField(widget=forms.Textarea)