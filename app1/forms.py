from django import forms

class Formulario(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())


