from django.shortcuts import render, redirect
from django.template import loader 
from django.http import HttpResponse
from .forms import StudentSignUpForm, StudentSignInForm
from .models import Student
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

def WelcomePageMethod(request):
    context = {'form': StudentSignUpForm()}
    return render(request, 'QuizzDynamoApp/Welcome.html', context)

def AdminPageMethod(request):
    template_admin = loader.get_template('QuizzDynamoApp/admin.html')
    context = {'template_admin':template_admin}
    return HttpResponse(template_admin.render(context, request))

def StudentSignUp(request):
    if request.method == "POST":
        try:
            studentsignupform = StudentSignUpForm(request.POST)
            if studentsignupform.is_valid():
                student = studentsignupform.save()
                studentsignupformusername = student.username
                messages.success(request, "Account created for {}".format(studentsignupformusername))
                degree = student.degree
                if(degree == 'Bsc'):
                    return redirect('QuizzDynamoApp:BachelorSignUp')
                elif(degree == 'Msc'):
                    return redirect('QuizzDynamoApp:MasterSignUp')
                elif(degree == 'PGDiploma'):
                    return redirect('QuizzDynamoApp:PGDiplomaSignUp')
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
            if (studentcheck.degree == 'Bsc'):
                 return redirect('QuizzDynamoApp:BachelorSignUp')
            elif (studentcheck.degree == 'Msc'):
                 return redirect('QuizzDynamoApp:MasterSignUp')
            elif (studentcheck.degree == 'PGDiploma'):
                 return redirect('QuizzDynamoApp:PGDiplomaSignUp')
    studentsigninform = StudentSignInForm()
    return render(request, "QuizzDynamoApp/SignIn.html", {'form':studentsigninform}) 
    
def StudentBachelorsSignUp(request):
    bsc_degree = Student.objects.get(degree='Bsc')
    return render(request, 'QuizzDynamoApp/Bachelors.html', {'form':bsc_degree})

def StudentMastersSignUp(request):
    msc_degree = Student.objects.get(degree='Msc')
    return render(request, 'QuizzDynamoApp/Masters.html', {'form':msc_degree})
    
def StudentPGDiplomaSignUp(request):
    pgdiploma_degree = Student.objects.get(degree='PGDiploma')
    return render(request, 'QuizzDynamoApp/PGDiploma.html', {'form':pgdiploma_degree})
