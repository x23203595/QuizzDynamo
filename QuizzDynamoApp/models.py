"""Model for Student, Quiz and Admin"""
from django.db import models
class Student(models.Model):
    """model for Student class"""
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
    degree = models.CharField(max_length=15, choices=DEGREE_CHOICES,
    default='Bsc')
    def __str__(self):
        return str(self.username)
class Quiz(models.Model):
    """Model for Quiz class"""
    question_text = models.CharField(max_length=150)
    option_a = models.CharField(max_length=150)
    option_b = models.CharField(max_length=150)
    option_c = models.CharField(max_length=150)
    option_d = models.CharField(max_length=150)
    correct_answer = models.CharField(max_length=1,
    choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default=('A'))
    def __str__(self):
        return str(self.question_text)
class Admin(models.Model):
    """Model for Admin class"""
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return str(self.username)
        