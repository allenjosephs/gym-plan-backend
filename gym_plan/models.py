from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.TextField(null=True, blank=True)
    icon_url = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"

    def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.TextField(null=True, blank=True)
    icon_url = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "MuscleGroup"
        verbose_name_plural = "MuscleGroups"

    def __str__(self):
        return self.name

class Exercise(models.Model):

    name = models.CharField(max_length=50)

    primary_equip = models.ForeignKey(
        Equipment,
        on_delete=models.PROTECT,
        related_name='primary_equipment',
    )

    primary_muscle = models.ForeignKey(
        MuscleGroup,
        on_delete=models.PROTECT,
        related_name='primary_musclegroups',
    )

    secondary_musclegroup = models.ManyToManyField(
        MuscleGroup,
        related_name='secondary_musclegroups',
        blank=True
    )

    instructions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Set(models.Model):
    label = models.CharField(max_length=50, null=True, blank=True)
    set_repeat_count = models.PositiveIntegerField(default=1)
    interval_duration_secs = models.PositiveIntegerField(default=60)
    interval_rest_between = models.BooleanField(default=False)
    interval_rest_duration = models.PositiveIntegerField(default=0)

    exercises = models.ManyToManyField(
        Exercise,
        through='ExerciseSet',
        blank=True
    )

    workout = models.ForeignKey(
            "Workout",
            on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.label if self.label else str(self.id)

class Workout(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="creator"
    )

    users = models.ManyToManyField(
        User,
        related_name="shared_with_users",
        blank=True
    )

    workout_warmup = models.BooleanField(default=False)
    workout_warmup_duration = models.PositiveIntegerField(default=0)
    workout_cooldown = models.BooleanField(default=False)
    workout_cooldown_duration = models.PositiveIntegerField(default=0)

    set_rest_between = models.BooleanField(default=False)
    set_rest_duration = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class ExerciseSet(models.Model):
    aSet = models.ForeignKey(Set, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.exercise.name

class ExerciseSetInline(admin.TabularInline):
    model = ExerciseSet
    extra = 1

class SetAdmin(admin.ModelAdmin):
    inlines = (ExerciseSetInline, )

class SetInline(admin.TabularInline):
    model = Set
    extra = 1

class EquipmentAdmin(admin.ModelAdmin):
    model = Equipment
    list_display = ('id', 'name', 'img_url', 'icon_url', )
    list_editable = ('name', 'img_url', 'icon_url', )

class MuscleGroupAdmin(admin.ModelAdmin):
    model = MuscleGroup
    list_display = ('id', 'name', 'img_url', 'icon_url', )
    list_editable = ('name', 'img_url', 'icon_url', )

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [
        SetInline,
    ]


