# Generated by Django 3.0.3 on 2020-06-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200606_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]