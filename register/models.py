from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    HOUSE_CHOICES = (
        ('G', 'Gryffindor'),
        ('H', 'Hufflepuff'),
        ('R', 'Ravenclaw'),
        ('S', 'Slytherin'),
        ('U', 'undefined')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    house = models.CharField(max_length=40, choices=HOUSE_CHOICES, default = 'U')
    XP = models.SmallIntegerField(default = 0)

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)