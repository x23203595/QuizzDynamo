"""View for QuizzDynamo"""
import csv
import io
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from .models import Student, Quiz, Admin
from .forms import StudentSignUpForm, StudentSignInForm, AdminSignInForm

@require_http_methods(["GET", "POST"])
def WelcomePageMethod(request):
    """Welcome Page for QuizzDynamo. Loads StudentSignUpForm and it's fields in 
    the page"""
    context = {'form': StudentSignUpForm()}
    return render(request, 'QuizzDynamoApp/Welcome.html', context)

def AboutPageMethod(request):
    """About Page for QuizzDynamo"""
    template_about = loader.get_template('QuizzDynamoApp/About.html')
    context = {'template_about':template_about}
    return HttpResponse(template_about.render(context, request))

def AdminAboutPageMethod(request):
    """Admin About Page for QuizzDynamo"""
    template_adminabout = loader.get_template('QuizzDynamoApp/AdminAbout.html')
    context = {'template_adminabout':template_adminabout}
    return HttpResponse(template_adminabout.render(context, request))

def AdminSignOutPageMethod(request):
    """Admin Sign Out Page for QuizzDynamo"""
    template_adminsignout = loader.get_template('QuizzDynamoApp/AdminSignOut.html')
    context = {'template_adminsignout':template_adminsignout}
    return HttpResponse(template_adminsignout.render(context, request))

def AdminPageMethod(request):
    """Bringing up the Admin Page for necessary changes"""
    admin_page = Admin.objects.all(username=username)# pylint: disable=E0602
    return render(request, 'QuizzDynamoApp/Admin.html', {'form': admin_page})

def AdminSignInMethod(request):
    """Sign Up Page for Admin"""
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admincheck = Admin.objects.get(username=username)
            except ObjectDoesNotExist:
                error_message = "User does not exist. Please check your username."
                return render(request, "QuizzDynamoApp/AdminSignIn.html",
                {'form': form, 'error_message': error_message})
            if  admincheck:
                if admincheck.password == password:
                    return redirect('QuizzDynamoApp:Admin')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'QuizzDynamoApp/AdminSignIn.html',
                {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
    return render(request, 'QuizzDynamoApp/AdminSignIn.html', {'form': form})

def AdminSignInModulesMethod(request):
    """Sign Up Page for Admin Modules"""
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admincheck = Admin.objects.get(username=username)
            except ObjectDoesNotExist:
                error_message = "User does not exist. Please check your username."""
                return render(request, "QuizzDynamoApp/AdminSignInModules.html",
                {'form': form, 'error_message': error_message})
            if  admincheck:
                if admincheck.password == password:
                    return redirect('QuizzDynamoApp:AdminUploadPage')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'QuizzDynamoApp/AdminSignInModules.html',
                {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
        return render(request, 'QuizzDynamoApp/AdminSignInModules.html',
        {'form': form})

def AdminStudentSignInMethod(request):
    """Sign Up Page for Admin Modules"""
    if request.method == 'POST':
        form = AdminSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                admincheck = Admin.objects.get(username=username)
            except ObjectDoesNotExist:
                error_message = "User does not exist. Please check your username."""
                return render(request, "QuizzDynamoApp/AdminStudentSignIn.html",
                {'form': form, 'error_message': error_message})
            if  admincheck:
                if admincheck.password == password:
                    return redirect('QuizzDynamoApp:AdminStudentInsertPage')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'QuizzDynamoApp/AdminStudentSignIn.html',
                {'form': form, 'error_message': error_message})
    else:
        form = AdminSignInForm()
    return render(request, 'QuizzDynamoApp/AdminStudentSignIn.html',
    {'form': form})

def StudentSignUp(request):
    """Sign Up Page. Responsible for bringing up three different pages for BSc,
    MSc and PGDiploma on user submission of the degree"""
    if request.method == "POST":
        try:
            studentsignupform = StudentSignUpForm(request.POST)
            if studentsignupform.is_valid():
                student = studentsignupform.save()
                studentsignupformusername = student.username
                messages.success(request,
                f"Account created for {studentsignupformusername}")
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
        except Exception as e:# pylint: disable=W0718
            messages.error(request,
            "There was an error creating your account", e)
            return redirect('QuizzDynamoApp:Welcome')
    elif request.method == "GET":
        studentsignupform = StudentSignUpForm()
        return render(request, "QuizzDynamoApp/Welcome.html",
        {'form': studentsignupform})

def StudentSignIn(request):
    """Sign In Page. Responsible for bringing up three different pages for BSc, 
    MSc and PGDiploma on user submission of the degree"""
    if request.method == "POST":
        studentsigninform = StudentSignInForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            studentcheck = Student.objects.get(username=username)
        except ObjectDoesNotExist:
            error_message = "User does not exist. Please check your username."
            return render(request, "QuizzDynamoApp/SignIn.html",
            {'form': studentsigninform, 'error_message': error_message})
        if studentcheck.password1 == password:
            if studentcheck.degree == 'Bsc':
                return redirect('QuizzDynamoApp:BachelorSignUp')
            elif studentcheck.degree == 'Msc':
                return redirect('QuizzDynamoApp:MasterSignUp')
            elif studentcheck.degree == 'PGDiploma':
                return redirect('QuizzDynamoApp:PGDiplomaSignUp')
        error_message = "Invalid username or password."
        return render(request, "QuizzDynamoApp/SignIn.html",
        {'form': studentsigninform, 'error_message': error_message})
    studentsigninform = StudentSignInForm()
    return render(request, "QuizzDynamoApp/SignIn.html",
    {'form': studentsigninform})

def StudentSignOut(request):
    """User Sign Out for QuizzDynamo"""
    template_usersignout = loader.get_template('QuizzDynamoApp/SignOut.html')
    context = {'template_usersignout':template_usersignout}
    return HttpResponse(template_usersignout.render(context, request))

def StudentBachelorsSignUp(request):
    """Bachelor's Degree Quiz Page and it's respective subjects"""
    bsc_degree = Student.objects.get(degree='Bsc')
    return render(request, 'QuizzDynamoApp/Bachelors.html', {'form':bsc_degree})

def StudentMastersSignUp(request):
    """Master's Degree Quiz Page and it's respective subjects"""
    msc_degree = Student.objects.get(degree='Msc')
    return render(request, 'QuizzDynamoApp/Masters.html', {'form':msc_degree})

def StudentPGDiplomaSignUp(request):
    """PG Diploma Degree Quiz Page and it's respective subjects"""
    pgdiploma_degree = Student.objects.get(degree='PGDiploma')
    return render(request, 'QuizzDynamoApp/PGDiploma.html',
    {'form':pgdiploma_degree})

def AdminUploadMethod(request):
    """Admin Page for uploading the csv files for the quizzes"""    
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
        _, created = Quiz.objects.update_or_create(# pylint: disable=W0612
            question_text=column[0],
            option_a=column[1],
            option_b=column[2],
            option_c=column[3],
            option_d=column[4],
            correct_answer=column[5]
        )
    return render(request, template)

def AdminStudentListMethod(request):
    """Method for Student List"""
    context = {'AdminStudentList' : Student.objects.all()}
    return render(request, 'QuizzDynamoApp/AdminStudentList.html', context)

def AdminStudentFormMethod(request, newid=0):
    """Method for Student Form"""
    if request.method == "GET":
        if newid == 0:
            form = StudentSignUpForm()
        else:
            student = Student.objects.get(pk=newid)
            form = StudentSignUpForm(instance=student)
        return render(request, 'QuizzDynamoApp/AdminStudent.html',
        {'form': form})
    else:
        if newid == 0:
            form = StudentSignUpForm(request.POST)
        else:
            student = Student.objects.get(pk=newid)
            form = StudentSignUpForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
        return redirect('QuizzDynamoApp:AdminStudentListPage')

def AdminStudentDelete(newid):
    """Method for Student Delete"""
    student = Student.objects.get(pk=newid)
    student.delete()
    return redirect('QuizzDynamoApp:AdminStudentListPage')

def BusinessIntelligenceQuizMethod(request):
    """Page for displaying the questions of the quiz for BusinessIntelligence""" 
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/BusinessIntelligenceQuiz.html',
        context)
    else:
        return JsonResponse({'status': 'error', 'message':
            'Invalid request method'})

def BusinessIntelligenceSubmissionMethod(request):
    """Page for displaying the results of the quiz for BusinessIntelligence"""
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
        return render(request,
        'QuizzDynamoApp/BusinessIntelligenceQuizSubmission.html',
        {'results': results})
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def OperatingSystemsQuizMethod(request):
    """Page for displaying the questions of the quiz for Operating Systems"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request,
        'QuizzDynamoApp/OperatingSystemsQuiz.html',context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def OperatingSystemsSubmissionMethod(request):
    """Page for displaying the results of the quiz for Operating Systems"""   
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
        return render(request,
        'QuizzDynamoApp/OperatingSystemsQuizSubmission.html',
        {'results': results})

def DatabaseManagementSystemsQuizMethod(request):
    """Page for displaying the questions of the quiz for Database 
    Management Systems"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request,
        'QuizzDynamoApp/DatabaseManagementSystemsQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def DatabaseManagementSystemsSubmissionMethod(request):
    """Page for displaying the results of the quiz for Database Management 
    Systems"""
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
        return render(request,
        'QuizzDynamoApp/DatabaseManagementSystemsQuizSubmission.html',
        {'results': results})

def LinuxQuizMethod(request):
    """Page for displaying the questions of the quiz for Linux"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/LinuxQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def LinuxSubmissionMethod(request):
    """Page for displaying the results of the quiz for Linux"""
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
        return render(request,'QuizzDynamoApp/LinuxQuizSubmission.html',
        {'results': results})

def JavaQuizMethod(request):
    """Page for displaying the questions of the quiz for Java"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/JavaQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def JavaSubmissionMethod(request):
    """Page for displaying the results of the quiz for Java"""    
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
        return render(request,
        'QuizzDynamoApp/JavaQuizSubmission.html',{'results': results})

def NetworkingConceptsQuizMethod(request):
    """Page for displaying the questions of the quiz for Networking Concepts"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request,
        'QuizzDynamoApp/NetworkingConceptsQuiz.html',context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def NetworkingConceptsSubmissionMethod(request):
    """Page for displaying the results of the quiz for Networking Concepts"""
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
        return render(request,
        'QuizzDynamoApp/NetworkingConceptsQuizSubmission.html',
        {'results': results})
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def SocialNetworkAnalysisQuizMethod(request):
    """Page for displaying the questions of the quiz for Social Network Analysis"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request,
        'QuizzDynamoApp/SocialNetworkAnalysisQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def SocialNetworkAnalysisSubmissionMethod(request):
    """Page for displaying the results of the quiz for Social Network Analysis"""
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
        return render(request,
        'QuizzDynamoApp/SocialNetworkAnalysisQuizSubmission.html',
        {'results': results})
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def AlgorithmsQuizMethod(request):
    """Page for displaying the questions of the quiz for Algorithms"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/AlgorithmsQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def AlgorithmsSubmissionMethod(request):
    """Page for displaying the results of the quiz for Algorithms"""
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
        return render(request,
        'QuizzDynamoApp/AlgorithmsQuizSubmission.html',{'results': results})

def WebDesignAppQuizMethod(request):
    """Page for displaying the questions of the quiz for Web Design & App"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request, 'QuizzDynamoApp/WebDesign&AppQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def WebDesignAppSubmissionMethod(request):
    """Page for displaying the results of the quiz for Web Design & App"""
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
        return render(request,
        'QuizzDynamoApp/WenDesign&AppQuizSubmission.html', {'results': results})
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def InternetworkingQuizMethod(request):
    """Page for displaying the questions of the quiz for Internetworking"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request,
        'QuizzDynamoApp/InternetworkingQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def InternetworkingSubmissionMethod(request):
    """Page for displaying the results of the quiz for Internetworking"""
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
        return render(request,
        'QuizzDynamoApp/InternetworkingQuizSubmission.html',
        {'results': results})
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def MobileDevelopmentQuizMethod(request):
    """Page for displaying the questions of the quiz for Mobile Development"""
    if request.method == 'GET':
        quiz_questions = Quiz.objects.all()
        context = {'quiz_questions': quiz_questions}
        return render(request,
        'QuizzDynamoApp/MobileDevelopmentQuiz.html', context)
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})

def MobileDevelopmentSubmissionMethod(request):
    """Page for displaying the results of the quiz for Mobile Development"""
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
        return render(request,
        'QuizzDynamoApp/MobileDevelopmentQuizSubmission.html',
        {'results': results})
    else:
        return JsonResponse({'status': 'error',
        'message': 'Invalid request method'})
        