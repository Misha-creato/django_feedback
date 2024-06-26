# Generated by Django 4.2 on 2024-04-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_options_feedback_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='status',
        ),
        migrations.AddField(
            model_name='feedback',
            name='is_resolved',
            field=models.BooleanField(default=False, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='contacts',
            field=models.CharField(max_length=64, verbose_name='Контакты для связи'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='full_name',
            field=models.CharField(max_length=128, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(max_length=256, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
    ]
