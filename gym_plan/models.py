from django.db import models
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

class Exercise(models.Model):
    name = models.CharField(max_length=50)

    primary_equip_id = models.OneToOneField(
        Equipment,
        on_delete=models.PROTECT,
        primary_key=True
    )

    instructions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Set(models.Model):

    duration = models.PositiveIntegerField(0)
    repeat_count = models.PositiveIntegerField(0)

    exercises = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Workout(models.Model):
        name = models.CharField(max_length=50)
        description = models.TextField()

        creator_id = models.OneToOneField(
            User,
            on_delete=models.PROTECT,
            primary_key=True
        )

        users = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="shared_with_users"
        )

        sets = models.ForeignKey(
            Set,
            on_delete=models.CASCADE,
            related_name="sets"
        )



