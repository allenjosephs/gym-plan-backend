from django.contrib import admin
from .models import Equipment, EquipmentAdmin, Exercise, Set, SetAdmin, Workout, WorkoutAdmin, MuscleGroup, MuscleGroupAdmin, ExerciseSet

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Exercise)
admin.site.register(Set, SetAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(MuscleGroup, MuscleGroupAdmin)
