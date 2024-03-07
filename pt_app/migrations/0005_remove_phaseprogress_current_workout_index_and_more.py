# Generated by Django 4.2.7 on 2024-03-06 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pt_app', '0004_remove_exerciselog_reps_per_set_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phaseprogress',
            name='current_workout_index',
        ),
        migrations.AddField(
            model_name='phaseprogress',
            name='current_workout_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_progress', to='pt_app.workout'),
        ),
        migrations.AlterField(
            model_name='exerciseset',
            name='exercise_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercise_sets', to='pt_app.exerciselog'),
        ),
    ]
