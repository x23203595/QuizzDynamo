"""Base Classes for Student, Question, Answer, Quiz, QuizResult and Subject """
from django.contrib import admin
from .models import Student, Quiz, Admin
admin.site.register(Student)
admin.site.register(Quiz)
admin.site.register(Admin)
