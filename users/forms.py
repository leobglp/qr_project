from django import forms
from django.forms import widgets
from localflavor.br.forms import BRCPFField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
            error_messages={'invalid': _('Por favor, insira um endereço de email válido.')}
        )
    cpf = BRCPFField(
            widget=forms.TextInput(
            attrs={'placeholder': '000.000.000-00', 'data-mask': '000.000.000-00'}),
            error_messages={'invalid': _('Por favor, insira um CPF válido.')}
        )
    nome_completo = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': '(99) 99999-9999', 'data-mask': '(00) 00000-0000'}))

    #Adicionar novas informações para o cadastro aqui

    class Meta:
        model = User
        fields = ['nome_completo', 'email', 'cpf', 'telefone', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']