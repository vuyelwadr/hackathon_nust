# Generated by Django 3.2.8 on 2021-10-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0004_alter_courses_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='community_load',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='research_project',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
