from django import forms
from django.core import validators
from .models import Student, Admin
from django import forms

"""Form for SignIn Page """
class StudentSignInForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
"""Form for Student Sign Up with validations"""
class StudentSignUpForm(forms.ModelForm):
    name_regex = '\A[a-zA-Z]+\Z'
    username_regex = '^[a-zA-Z0-9]+$'
    min_length = 2
    max_length = 25
    validation_msg_min = "Should have at least {} characters".format(min_length)
    validation_msg_max = "Should have at most {} characters".format(max_length)
    first_name = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, validation_msg_min),
        validators.MaxLengthValidator(max_length, validation_msg_max),
        validators.RegexValidator(name_regex)
    ])
    last_name = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, validation_msg_max),
        validators.MaxLengthValidator(max_length, validation_msg_max),
        validators.RegexValidator(name_regex)
    ])
    username = forms.CharField(validators=[
        validators.MinLengthValidator(min_length, validation_msg_min),
        validators.MaxLengthValidator(max_length, validation_msg_max),
        validators.RegexValidator(username_regex), 
    ])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    DEGREE_CHOICES = (
    ('Bsc','Bsc'),
    ('Msc','Msc'),
    ('PGDiploma','PGDiploma'),
    )
    degree = forms.ChoiceField(choices=DEGREE_CHOICES, widget=forms.Select)
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'password1', 
        'password2', 'degree']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        
"""Form for Admin Page"""
class AdminSignInForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    class Meta:
        model = Admin
        fields = ['username', 'password']
