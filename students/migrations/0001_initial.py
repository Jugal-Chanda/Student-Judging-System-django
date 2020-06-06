# Generated by Django 3.0.3 on 2020-06-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=150, upload_to='student_image', width_field=150)),
                ('fullname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=40, unique=True)),
            ],
        ),
    ]