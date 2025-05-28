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


class RegisterForm(forms.Form):
    name = "Cadastro"

    username = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'})
    )

    email = forms.EmailField(
        label="",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    password = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha'})
    )

    confirm_password = forms.CharField(
        label="",
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a senha'})
    )
