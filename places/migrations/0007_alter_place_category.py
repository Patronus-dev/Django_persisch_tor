# Generated by Django 5.0.7 on 2025-03-14 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(choices=[('food & drink', 'Food & Drink'), ('medical services', 'Medical services'), ('technical services', 'Technical services'), ('store', 'Store'), ('entertainment', 'Entertainment'), ('other', 'Other')], help_text='Select the category of the place.', max_length=100, verbose_name='Category'),
        ),
    ]
