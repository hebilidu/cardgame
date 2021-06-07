from django.db import models


# Create your models here.
class Card(models.Model):
    name = models.CharField()
    species = models.CharField()
    gender = models.CharField()
    house = models.CharField(null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    ancestry = models.CharField(null=True, blank=True)
    wand_wood = models.CharField(null=True, blank=True)
    wand_core = models.CharField(null=True, blank=True)
    wand_length = models.FloatField(null=True, blank=True)
    patronus = models.CharField(null=True, blank=True)
    is_hogwarts_student = models.BooleanField()
    is_hogwarts_staff = models.BooleanField()
    image = models.URLField(null=True, blank=True)
    rarity = models.smallIntegerField(default=0)
    price = models.FloatField(default=0.)

    def __str__(self):
        return self.name
