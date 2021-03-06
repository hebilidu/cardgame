# Generated by Django 3.2.3 on 2021-06-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('species', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('house', models.CharField(blank=True, max_length=20, null=True)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('ancestry', models.CharField(blank=True, max_length=20, null=True)),
                ('wand_wood', models.CharField(blank=True, max_length=20, null=True)),
                ('wand_core', models.CharField(blank=True, max_length=20, null=True)),
                ('wand_length', models.FloatField(blank=True, null=True)),
                ('patronus', models.CharField(blank=True, max_length=50, null=True)),
                ('is_hogwarts_student', models.BooleanField()),
                ('is_hogwarts_staff', models.BooleanField()),
                ('image', models.URLField(blank=True, null=True)),
                ('rarity', models.SmallIntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]
