# Generated by Django 3.2.3 on 2021-06-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='house',
            field=models.CharField(choices=[('GRYFFINDOR', 'Gryffindor'), ('HUFFLEPUFF', 'Hufflepuff'), ('RAVENCLAW', 'Ravenclaw'), ('SLYTHERIN', 'Slytherin'), ('UNDEFINED', 'undefined')], default='UNDEFINED', max_length=40),
        ),
    ]