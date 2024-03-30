"""Base Classes for Student, Question, Answer, Quiz, QuizResult and Subject """

from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Quiz)
# # admin.site.register(Degree)
# admin.site.register(AdminForStudent)