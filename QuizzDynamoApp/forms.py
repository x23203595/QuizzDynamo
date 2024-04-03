"""Form for Student, Quiz and Admin """
from django import forms
from django.core import validators
from .models import Student, Admin
class StudentSignInForm(forms.Form):
    """Form for SignIn Page """
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
class StudentSignUpForm(forms.ModelForm):
    """Form for Student Sign Up with validations"""
    name_regex = r"\A[a-zA-Z]+\Z"
    username_regex = r"^[a-zA-Z0-9]+$"
    min_length = 2
    max_length = 25
    validation_msg_min = f"Should have at least {min_length} characters"
    validation_msg_max = f"Should have at most {max_length} characters"
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
        validators.RegexValidator(username_regex)])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    DEGREE_CHOICES = (
    ('Bsc','Bsc'),
    ('Msc','Msc'),
    ('PGDiploma','PGDiploma'),
    )
    degree = forms.ChoiceField(choices=DEGREE_CHOICES, widget=forms.Select)
    class Meta:
        """Subclass for Student"""
        model = Student
        fields = ['first_name', 'last_name', 'username', 'password1',
        'password2', 'degree']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
class AdminSignInForm(forms.ModelForm):
    """Form for Admin Page"""
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        """Subclass for Admin"""
        model = Admin
        fields = ['username', 'password']
