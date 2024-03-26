from django import forms
from .models import CustomUser


class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "name",
            "email",
            "major",
            "nickname",
            "password",
            "phone_number",
        )  # Use 'fields' instead of 'field'
        widgets = {
            "password": forms.PasswordInput(),
        }
