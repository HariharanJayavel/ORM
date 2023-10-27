# Generated by Django 4.2.5 on 2023-10-19 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Football_player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
