# Generated by Django 4.1.4 on 2023-02-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('autho', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('decription', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]