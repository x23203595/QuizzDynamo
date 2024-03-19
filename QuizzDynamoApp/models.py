from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email_address = models.EmailField()
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