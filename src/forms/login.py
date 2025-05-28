from django import forms


class LoginForm(forms.Form):
    name = "Login"

    username = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))

    password = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
