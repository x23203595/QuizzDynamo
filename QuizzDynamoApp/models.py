from django import forms
from django.db import models

"""model for Student class"""
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    DEGREE_CHOICES = (
    ('Bsc','Bsc'),
    ('Msc','Msc'),
    ('PGDiploma','PGDiploma'),
    )
    degree = models.CharField(max_length=15, choices=DEGREE_CHOICES, default='Bsc')
    
    def __str__(self):
        return self.username
    
"""Model for Quiz class"""
class Quiz(models.Model):
    question_text = models.CharField(max_length=150)
    option_a = models.CharField(max_length=150)
    option_b = models.CharField(max_length=150)
    option_c = models.CharField(max_length=150)
    option_d = models.CharField(max_length=150)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default=('A'))
    
    def __str__(self):
        return self.question_text
