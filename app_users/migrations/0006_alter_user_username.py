# Generated by Django 5.0.4 on 2024-05-01 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_hobby_book_student_hobbies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
