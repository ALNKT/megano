# Generated by Django 4.1.7 on 2023-03-26 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'профиль', 'verbose_name_plural': 'профили'},
        ),
    ]
