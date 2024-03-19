from django.urls import path
from . import views

app_name = 'QuizzDynamoApp'
urlpatterns = [ 
    path('', views.WelcomePageMethod, name='Welcome'),
    path('admin/', views.AdminPageMethod, name = 'Admin'),
     path('QuizzDynamoApp/Home/signup/', views.StudentSignUp, name='SignUp'),
    path('QuizzDynamoApp/Home/signin/', views.StudentSignIn, name='SignIn'),
    path('QuizzDynamoApp/Home/Bachelors/', views.StudentBachelorsSignUp, name='BachelorSignUp'),
    path('QuizzDynamoApp/Home/Masters/', views.StudentMastersSignUp, name='MasterSignUp'),
    path('QuizzDynamoApp/Home/PGDiploma/', views.StudentPGDiplomaSignUp, name='PGDiplomaSignUp'),
]
