# Generated by Django 5.0.3 on 2024-03-07 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman_bvg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='userLetterChoice',
            field=models.CharField(max_length=1, verbose_name='Choisir une lettre :'),
        ),
    ]
