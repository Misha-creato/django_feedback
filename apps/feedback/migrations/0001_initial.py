# Generated by Django 4.2 on 2024-04-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=256)),
                ('full_name', models.CharField(max_length=128)),
                ('contacts', models.CharField(max_length=64)),
            ],
        ),
    ]
