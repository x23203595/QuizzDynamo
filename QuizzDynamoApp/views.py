import csv, io
from django.shortcuts import render, redirect
from django.template import loader 
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Student, Quiz
from .forms import StudentSignUpForm, StudentSignInForm, AdminSignInForm
import pandas as pd
import io
# Create your views here.

"""Welcome Page for Project. Loads StudentSignUpForm and it's fields in the page"""
def WelcomePageMethod(request):
    context = {'form': StudentSignUpForm()}
    return render(request, 'QuizzDynamoApp/Welcome.html', context)

"""Bringing up the Admin Page for necessary changes"""
def AdminPageMethod(request):
    template_admin = loader.get_template('QuizzDynamoApp/admin.html')
    context = {'template_admin':template_admin}
    return HttpResponse(template_admin.render(context, request))

"""Sign Up Page for Admin"""
def AdminSignInMethod(request):
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('QuizzDynamoApp:AdminSignInPage')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'QuizzDynamoApp/Welcome.html', {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
    return render(request, 'QuizzDynamoApp/AdminSignIn.html', {'form': form})
    
"""Sign Up Page for Admin Modules"""
def AdminSignInModulesMethod(request):
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('QuizzDynamoApp:AdminModulesPage')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'QuizzDynamoApp/AdminSignInModules.html', {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
    return render(request, 'QuizzDynamoApp/AdminSignInModules.html', {'form': form})
    
"""Sign Up Page for Admin Student Sign In"""
def AdminStudentSignInMethod(request):
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('QuizzDynamoApp:AdminStudentSignIn')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'QuizzDynamoApp/Welcome.html', {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
    return render(request, 'QuizzDynamoApp/AdminStudentSignIn.html', {'form': form})

"""Sign Up Page. Responsible for bringing up three different pages for BSc,
MSc and PGDiploma on user submission of the degree"""
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
        
"""Sign In Page. Responsible for bringing up three different pages for BSc,
MSc and PGDiploma on user submission of the degree"""
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

"""Bachelor's Degree Quiz Page and it's respective subjects"""
def StudentBachelorsSignUp(request):
    bsc_degree = Student.objects.get(degree='Bsc')
    return render(request, 'QuizzDynamoApp/Bachelors.html', {'form':bsc_degree})

"""Master's Degree Quiz Page and it's respective subjects"""
def StudentMastersSignUp(request):
    msc_degree = Student.objects.get(degree='Msc')
    return render(request, 'QuizzDynamoApp/Masters.html', {'form':msc_degree})

"""PG Diploma Degree Quiz Page and it's respective subjects"""
def StudentPGDiplomaSignUp(request):
    pgdiploma_degree = Student.objects.get(degree='PGDiploma')
    return render(request, 'QuizzDynamoApp/PGDiploma.html', {'form':pgdiploma_degree})

"""AdminModules Page displaying the csv file to be uploaded"""
def AdminModulesMethod(request):
    context = {}
    return render(request, 'QuizzDynamoApp/AdminModules.html', context)

"""Admin Page for uploading the csv files for the quizzes"""    
def AdminUploadMethod(request):
    template = "QuizzDynamoApp/AdminModules.html"
    data = Quiz.objects.all()
    prompt = {
        'order': 'Order of the CSV should be question_text, option_a, option_b, option_c, option_d',
        'quizzes': data    
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES.get('file')
    if not csv_file:
        messages.error(request, 'No file uploaded! Refresh to upload a file!')
        return render(request, template, prompt)  
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
        return render(request, template, prompt)  
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Quiz.objects.update_or_create(
            question_text=column[0],
            option_a=column[1],
            option_b=column[2],
            option_c=column[3],
            option_d=column[4],
            correct_answer=column[5]
        )
        
    return render(request, template)
    

"""Method for Student List"""
def AdminStudentListMethod(request):
    context = {'AdminStudentList' : Student.objects.all()}
    return render(request, 'QuizzDynamoApp/AdminStudentList.html', context)

"""Method for Student Form"""
def AdminStudentFormMethod(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentSignUpForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentSignUpForm(instance=student)
        return render(request, 'QuizzDynamoApp/AdminStudent.html', {'form': form})
    else:
        if id == 0:
            form = StudentSignUpForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentSignUpForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
        return redirect('QuizzDynamoApp:AdminStudentListPage')
        
"""Method for Student Delete"""
def AdminStudentDelete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('QuizzDynamoApp:AdminStudentListPage')

"""Page for displaying the questions of the quiz for BusinessIntelligence"""    
def BusinessIntelligenceQuizMethod(request):
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()

        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/BusinessIntelligenceQuiz.html', context)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

"""Page for displaying the results of the quiz for BusinessIntelligence"""    
def BusinessIntelligenceSubmissionMethod(request):
    if request.method == 'POST':
        submitted_answers = {}
        for key, value in request.POST.items():
            if key.startswith('option_'): 
                question_id = key.split('_')[1]
                submitted_answers[int(question_id)] = value

        quiz_questions = Quiz.objects.all()

        results = {}
        for question in quiz_questions:
            submitted_answer = submitted_answers.get(question.id)
            if submitted_answer == question.correct_answer:
                results[question.question_text] = 'right'
            else:
                results[question.question_text] = 'wrong'

        return render(request, 'QuizzDynamoApp/BusinessIntelligenceQuizSubmission.html', {'results': results})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

"""Page for displaying the questions of the quiz for Operating Systems"""
def OperatingSystemsQuizMethod(request):
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()

        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/OperatingSystemsQuiz.html', context)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
"""Page for displaying the results of the quiz for Operating Systems"""    
def OperatingSystemsSubmissionMethod(request):
    if request.method == 'POST':
        submitted_answers = {}
        for key, value in request.POST.items():
            if key.startswith('option_'): 
                question_id = key.split('_')[1]
                submitted_answers[int(question_id)] = value

        quiz_questions = Quiz.objects.all()

        results = {}
        for question in quiz_questions:
            submitted_answer = submitted_answers.get(question.id)
            if submitted_answer == question.correct_answer:
                results[question.question_text] = 'right'
            else:
                results[question.question_text] = 'wrong'

        return render(request, 'QuizzDynamoApp/OperatingSystemsQuizSubmission.html', {'results': results})
        
"""Page for displaying the questions of the quiz for Database Management Systems"""
def DatabaseManagementSystemsQuizMethod(request):
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()

        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/DatabaseManagementSystemsQuiz.html', context)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
"""Page for displaying the results of the quiz for Database Management Systems"""    
def DatabaseManagementSystemsSubmissionMethod(request):
    if request.method == 'POST':
        submitted_answers = {}
        for key, value in request.POST.items():
            if key.startswith('option_'): 
                question_id = key.split('_')[1]
                submitted_answers[int(question_id)] = value

        quiz_questions = Quiz.objects.all()

        results = {}
        for question in quiz_questions:
            submitted_answer = submitted_answers.get(question.id)
            if submitted_answer == question.correct_answer:
                results[question.question_text] = 'right'
            else:
                results[question.question_text] = 'wrong'

        return render(request, 'QuizzDynamoApp/DatabaseManagementSystemsQuizSubmission.html', {'results': results})
    
"""Page for displaying the questions of the quiz for Linux"""
def LinuxQuizMethod(request):
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()

        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/LinuxQuiz.html', context)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
"""Page for displaying the results of the quiz for Linux"""    
def LinuxSubmissionMethod(request):
    if request.method == 'POST':
        submitted_answers = {}
        for key, value in request.POST.items():
            if key.startswith('option_'): 
                question_id = key.split('_')[1]
                submitted_answers[int(question_id)] = value

        quiz_questions = Quiz.objects.all()

        results = {}
        for question in quiz_questions:
            submitted_answer = submitted_answers.get(question.id)
            if submitted_answer == question.correct_answer:
                results[question.question_text] = 'right'
            else:
                results[question.question_text] = 'wrong'

        return render(request, 'QuizzDynamoApp/LinuxQuizSubmission.html', {'results': results})
        
"""Page for displaying the questions of the quiz for Java"""
def JavaQuizMethod(request):
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()

        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/JavaQuiz.html', context)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
"""Page for displaying the questions of the quiz for Java"""    
def JavaSubmissionMethod(request):
    if request.method == 'POST':
        submitted_answers = {}
        for key, value in request.POST.items():
            if key.startswith('option_'): 
                question_id = key.split('_')[1]
                submitted_answers[int(question_id)] = value

        quiz_questions = Quiz.objects.all()

        results = {}
        for question in quiz_questions:
            submitted_answer = submitted_answers.get(question.id)
            if submitted_answer == question.correct_answer:
                results[question.question_text] = 'right'
            else:
                results[question.question_text] = 'wrong'

        return render(request, 'QuizzDynamoApp/JavaQuizSubmission.html', {'results': results})
        