# Generated by Django 3.2.8 on 2021-10-17 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0005_auto_20211017_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_load',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='research_project',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
