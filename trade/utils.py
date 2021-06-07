import os
import django
import random
import requests
import json
from .models import Card

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cardgame_project.settings')
django.setup()

def get_characters():
    """returns a list of dictionaries"""
    url_source = "http://hp-api.herokuapp.com/api/characters"
    data = requests.get(url_source)
    data = data.json()
    return data


def fillup_card_table():
    """fills up the Card table"""
    characters = get_characters()
    for c in characters:
        rarity = 0
        price = 0.
        Card.objects.create(
            name = c['name'],
            species = c['species'],
            gender =c['gender'],
            house = c['house'],
            date_birth = c['dateOfBirth'],
            ancestry = c['ancestry'],
            wand_wood = c['wand']['wood'],
            wand_core = c['wand']['core'],
            wand_length = c['wand']['length'],
            patronus = c['patronus'],
            is_hogwarts_student = c['hogwartsStudent'],
            is_hogwarts_staff = c['hogwartsStaff'],
            image = c['image'],
            rarity = rarity,
            price = price
        )
