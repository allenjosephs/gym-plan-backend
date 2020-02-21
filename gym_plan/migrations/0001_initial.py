# Generated by Django 3.0.3 on 2020-02-20 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img_url', models.TextField(blank=True, null=True)),
                ('icon_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Equipment',
                'verbose_name_plural': 'Equipment',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('primary_equip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='primary_equipment', to='gym_plan.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img_url', models.TextField(blank=True, null=True)),
                ('icon_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'MuscleGroup',
                'verbose_name_plural': 'MuscleGroups',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
                ('set_repeat_count', models.PositiveIntegerField(default=1)),
                ('interval_duration_secs', models.PositiveIntegerField(default=60)),
                ('interval_rest_between', models.BooleanField(default=False)),
                ('interval_rest_duration', models.PositiveIntegerField(default=0)),
                ('exercises', models.ManyToManyField(blank=True, through='gym_plan.ExerciseSet', to='gym_plan.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='SetWorkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('aSet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_plan.Set')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('workout_warmup', models.BooleanField(default=False)),
                ('workout_warmup_duration', models.PositiveIntegerField(default=0)),
                ('workout_cooldown', models.BooleanField(default=False)),
                ('workout_cooldown_duration', models.PositiveIntegerField(default=0)),
                ('set_rest_between', models.BooleanField(default=False)),
                ('set_rest_duration', models.PositiveIntegerField(default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('sets', models.ManyToManyField(blank=True, through='gym_plan.SetWorkout', to='gym_plan.Set')),
                ('users', models.ManyToManyField(blank=True, related_name='shared_with_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='setworkout',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_plan.Workout'),
        ),
        migrations.AddField(
            model_name='exerciseset',
            name='aSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_plan.Set'),
        ),
        migrations.AddField(
            model_name='exerciseset',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_plan.Exercise'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='primary_muscle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='primary_musclegroups', to='gym_plan.MuscleGroup'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='secondary_musclegroup',
            field=models.ManyToManyField(blank=True, related_name='secondary_musclegroups', to='gym_plan.MuscleGroup'),
        ),
    ]
