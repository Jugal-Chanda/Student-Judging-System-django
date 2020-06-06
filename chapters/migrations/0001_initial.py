# Generated by Django 3.0.3 on 2020-06-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_title', models.CharField(max_length=20)),
                ('chapter_name', models.CharField(max_length=40)),
                ('rating', models.FloatField(default=0.0)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]