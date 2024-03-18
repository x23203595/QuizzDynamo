from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentSignUpForm, StudentSignInForm
from .models import Student
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def WelcomePageMethod(request):
    context = {'form': StudentSignUpForm()}
    return render(request, 'QuizzDynamoApp/Welcome.html', context)

def StudentSignUp(request):
    if request.method == "POST":
        try:
            studentsignupform = StudentSignUpForm(request.POST)
            print(studentsignupform)
            if studentsignupform.is_valid():
                student = studentsignupform.save()
                studentsignupformusername = student.username
                messages.success(request, "Account created for {}".format(studentsignupformusername))
                degree = student  
                return render(request, 'QuizzDynamoApp/Home.html', {'form': degree})
            else:
                messages.error(request, "There was an error signing up")
                return redirect('QuizzDynamoApp:Welcome')
        except Exception as e:
            messages.error(request, "There was an error creating your account", e)
            return redirect('QuizzDynamoApp:Welcome')
    elif request.method == "GET":
        studentsignupform = StudentSignUpForm()
        return render(request, "QuizzDynamoApp/Welcome.html", {'form': studentsignupform})

def StudentSignIn(request):
    if request.method == "POST":
        studentsigninform = StudentSignInForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        studentcheck = Student.objects.get(username=username)
        if (studentcheck.password1 == password):
            return render(request, 'QuizzDynamoApp/Home.html', {'form':studentcheck})
    studentsigninform = StudentSignInForm()
    return render(request, "QuizzDynamoApp/SignIn.html", {'form':studentsigninform}) 
   
           
