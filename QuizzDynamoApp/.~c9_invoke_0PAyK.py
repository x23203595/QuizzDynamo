from django.urls import path
from . import views

app_name = 'QuizzDynamoApp'
urlpatterns = [ 
    path('', views.WelcomePageMethod, name='Welcome'),
    path('admin/', views.AdminPageMethod, name = 'Admin'),
    path('QuizzDynamoApp/Home/signup', views.StudentSignUp, name='SignUp'),
    path('QuizzDynamoApp/Home/signin', views.StudentSignIn, name='SignIn'),
    path('QuizzDynamoApp/Bachelors', views.BachelorsSignUpForm, name = 'Bachelors'),
    path('QuizzDynamoApp/Masters', views.MastersSignUpForm, name = 'Masters'),
    path('QuizzDynamoApp/PGDiploma', views.PGDiplomaSignUpForm, name = 'PGDiploma'),
    path('QuizzDynamoApp/')
]
