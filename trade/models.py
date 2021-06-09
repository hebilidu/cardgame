from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    house = models.CharField(max_length=20, null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    ancestry = models.CharField(max_length=20, null=True, blank=True)
    wand_wood = models.CharField(max_length=20, null=True, blank=True)
    wand_core = models.CharField(max_length=20, null=True, blank=True)
    wand_length = models.FloatField(null=True, blank=True)
    patronus = models.CharField(max_length=50, null=True, blank=True)
    is_hogwarts_student = models.BooleanField()
    is_hogwarts_staff = models.BooleanField()
    image = models.URLField(null=True, blank=True)
    rarity = models.SmallIntegerField(default=0)
    price = models.FloatField(default=0.)

    def __str__(self):
        return self.name


class Deck(models.Model):
    """A deck is an even distribution of the cards to a given list of players. A card can appear no more than once in a deck instance. Each card receives a random rarity figure between 1 and 100, that feeds each player XP score"""
    creation_date = models.DateTimeField(auto_now_add=True)
    player = models.ManyToManyField(User)

    @staticmethod
    def create_instance():
        # Ask for number of players and their usernames
        # Calculate how many cards each one will have in his hand
        # Assign each card to a player, in a hand,  and allocate a random rarity score
        pass
    

class Hand(models.Model):
    """A hand is the collection of cards received by one player within a deck"""
    deck = models.ForeignKey(Deck, on_delete = models.CASCADE)
    player = models.ForeignKey(User, on_delete = models.CASCADE)
    card = models.ManyToManyField(Card)










