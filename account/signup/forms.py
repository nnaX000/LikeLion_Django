from django import forms
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "id",
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
