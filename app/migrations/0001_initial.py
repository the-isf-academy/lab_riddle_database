# Generated by Django 4.1.1 on 2022-09-15 00:52

import banjo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', banjo.models.StringField(default='')),
                ('answer', banjo.models.StringField(default='')),
                ('guesses', banjo.models.IntegerField(default=0)),
                ('correct', banjo.models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
