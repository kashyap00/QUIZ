# Generated by Django 4.0.6 on 2022-07-20 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_candidate_address1_candidate_address2_candidate_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionmaker',
            old_name='zip',
            new_name='zipc',
        ),
    ]
