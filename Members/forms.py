from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': ''}))
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': ''}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': ''}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = 'Логин'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Почта'
        
        self.fields['username'].widget.attrs = {'class': 'login'}
        self.fields['first_name'].widget.attrs = {'class': 'login'}
        self.fields['last_name'].widget.attrs = {'class': 'login'}
        self.fields['email'].widget.attrs = {'class': 'login'}
        self.fields['password1'].widget.attrs = {'class': 'password passwordInput'}
        self.fields['password2'].widget.attrs = {'class': 'password passwordInput'}