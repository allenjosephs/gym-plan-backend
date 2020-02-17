from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.TextField(null=True)
    icon_url = models.TextField(null=True)

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=250)

    primary_equip_id = models.OneToOneField(
        Equipment,
        on_delete=models.PROTECT,
        primary_key=True
    )

    def __str__(self):
        return self.name

