from django import forms
from . import models
""" from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation 사용 가능 : 비밀번호 인증을 할때, UserCreationForm을 안쓰는 대신에(User 등에 대한 것들이 깨지니까) 쓸 수 있음"""


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error('password', forms.ValidationError('Password is wrong'))
            
        except models.User.DoesNotExist:
            self.add_error('email', forms.ValidationError('User does not exist'))
 

class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'})
        }

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("That email is already taken", code="existing_user")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user.username = email
        user.set_password(password)
        user.save()
    
    # or
    # useername = forms.EmailField(label='Email') --> UserCreationForm을 이용하고 싶으면 username을 어디인가에서 사용해야하기 때문에, 쓸 수 있는 트릭 정도?
    # Meta는 다 지우고 