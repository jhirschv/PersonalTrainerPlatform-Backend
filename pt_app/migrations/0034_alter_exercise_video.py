# Generated by Django 4.2.7 on 2024-05-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pt_app', '0033_alter_exercise_name_alter_workout_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='video',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]