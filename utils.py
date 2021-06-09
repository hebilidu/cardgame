import os
import django
import random
import requests
from datetime import datetime
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cardgame_project.settings')
django.setup()

from trade.models import Card

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
        rarity = random.randint(1, 100)
        price = 0.
        if c['dateOfBirth'] == '':
            dt = None
        else:
            dt = datetime.strptime(c['dateOfBirth'], "%d-%m-%Y")
        wand_length = c['wand']['length']
        if  wand_length == '':
            wand_length = None
        Card.objects.create(
            name = c['name'],
            species = c['species'],
            gender =c['gender'],
            house = c['house'],
            date_birth = dt,
            ancestry = c['ancestry'],
            wand_wood = c['wand']['wood'],
            wand_core = c['wand']['core'],
            wand_length = wand_length,
            patronus = c['patronus'],
            is_hogwarts_student = c['hogwartsStudent'],
            is_hogwarts_staff = c['hogwartsStaff'],
            image = c['image'],
            rarity = rarity,
            price = price
        )

# fillup_card_table()