from django.urls import path
from . import views

app_name = 'QuizzDynamoApp'
urlpatterns = [ 
    path('', views.WelcomePageMethod, name='Welcome'),
    path('QuizzDynamoApp/Home/signup', views.StudentSignUp, name='SignUp'),
    path('QuizzDynamoApp/Home/signin', views.StudentSignIn, name='SignIn'),
]
