# Generated by Django 4.2.3 on 2023-07-15 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.CharField(max_length=20),
        ),
    ]
