from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm

class MemberForm(UserCreationForm):
    class Meta:
        model=Member
        fields=['username','password1','password2','email','mobile','image']

class LoginForm(forms.ModelForm):
    class Meta:
        model=Member
        fields = ['username','password']

        label = {
            'username' : '사용자이름',
            'password' : '비밀번호'
        }

        widgets = {
            'username' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '사용자이름을 입력하세요'
                }
            ),
            'password' : forms.PasswordInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '사용자비밀번호를 입력하세요.'
                }
            )

        }
