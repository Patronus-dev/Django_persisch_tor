# Generated by Django 5.0.7 on 2025-03-19 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0019_alter_place_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='website',
        ),
    ]
