# Generated by Django 4.2.7 on 2024-03-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pt_app', '0012_workout_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
