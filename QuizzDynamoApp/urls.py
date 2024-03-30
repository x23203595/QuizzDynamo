from django.urls import path
from . import views
from django.shortcuts import get_object_or_404

""""Path Page for different views of QuizzDynamo"""
app_name = 'QuizzDynamoApp'
urlpatterns = [ 
    path('', views.WelcomePageMethod, name='Welcome'),
    path('admin/', views.AdminPageMethod, name = 'Admin'),
    path('QuizzDynamoApp/Home/signup/', views.StudentSignUp, name='SignUp'),
    path('QuizzDynamoApp/Home/signin/', views.StudentSignIn, name='SignIn'),
    path('QuizzDynamoApp/Home/Display/AdminModules/', views.AdminModulesMethod, name = 'AdminModulesDisplayPage'),
    path('QuizzDynamoApp/Home/AdminSignIn/', views.AdminSignInMethod, name = 'AdminSignInPage'),
    path('QuizzDynamoApp/Home/AdminSignInModules/', views.AdminSignInModulesMethod, name = 'AdminSignInModulesPage'),
    path('QuizzDynamoApp/Home/AdminStudentSignIn/', views.AdminStudentSignInMethod, name = 'AdminStudentSignInPage'),
    path('QuizzDynamoApp/Home/Bachelors/', views.StudentBachelorsSignUp, name='BachelorSignUp'),
    path('QuizzDynamoApp/Home/Masters/', views.StudentMastersSignUp, name='MasterSignUp'),
    path('QuizzDynamoApp/Home/PGDiploma/', views.StudentPGDiplomaSignUp, name='PGDiplomaSignUp'),
    path('QuizzDynamoApp/Home/AdminModules/', views.AdminUploadMethod, name = 'AdminUploadPage'),
    path('QuizzDynamoApp/Home/AdminStudent/InsertAdminStudent/',views.AdminStudentFormMethod, name = 'AdminStudentInsertPage'),
    path('QuizzDynamoApp/Home/AdminStudent/AdminStudentList/', views.AdminStudentListMethod, name = 'AdminStudentListPage'),
    path('QuizzDynamoApp/Home/AdminStudent/UpdateAdminStudent/<int:id>/', views.AdminStudentFormMethod, name = 'AdminStudentUpdatePage'),
    path('QuizzDynamoApp/Home/AdminStudent/DeleteAdminStudent/<int:id>/', views.AdminStudentDelete, name = 'AdminStudentDeletePage'),
    path('QuizzDynamoApp/Home/BusinessIntelligenceQuiz/', views.BusinessIntelligenceQuizMethod, name='BusinessIntelligenceQuizPage'),
    path('QuizzDynamoApp/Home/BusinessIntelligenceQuizSubmission/', views.BusinessIntelligenceSubmissionMethod, name='BusinessIntelligenceSubmissionPage'),
    path('QuizzDynamoApp/Home/OperatingSystemsQuiz/', views.OperatingSystemsQuizMethod, name='OperatingSystemsQuizPage'),
    path('QuizzDynamoApp/Home/OperatingSystemsQuizSubmission/', views.OperatingSystemsSubmissionMethod, name='OperatingSystemsSubmissionPage'),
    path('QuizzDynamoApp/Home/DatabaseManagementSystemsQuiz/', views.DatabaseManagementSystemsQuizMethod, name='DatabaseManagementSystemsQuizPage'),
    path('QuizzDynamoApp/Home/DatabaseManagementSystemsQuizSubmission/', views.DatabaseManagementSystemsSubmissionMethod, name='DatabaseManagementSystemsSubmissionPage'),
    path('QuizzDynamoApp/Home/LinuxQuiz/', views.LinuxQuizMethod, name='LinuxQuizPage'),
    path('QuizzDynamoApp/Home/LinuxQuizSubmission/', views.LinuxSubmissionMethod, name='LinuxSubmissionPage'),
    path('QuizzDynamoApp/Home/JavaQuiz/', views.JavaQuizMethod, name='JavaQuizPage'),
    path('QuizzDynamoApp/Home/JavaQuizSubmission/', views.JavaSubmissionMethod, name='JavaSubmissionPage'),
]
