from logging import PlaceHolder
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "İstifadəçi Adı")
    password = forms.CharField(label = "Parol",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "İstifadəçi Adı")
    password = forms.CharField(max_length=20,label = "Parol",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Parolu Təsdiqlə",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parollar Uyğunlaşmır")

        values = {
            "username" : username,
            "password" : password
        }
        return values