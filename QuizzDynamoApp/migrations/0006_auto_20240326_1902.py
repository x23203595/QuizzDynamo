# Generated by Django 2.1.15 on 2024-03-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizzDynamoApp', '0005_auto_20240326_1825'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuizResult',
        ),
        migrations.AddField(
            model_name='quiz',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='default_value', max_length=1),
        ),
    ]
