# Generated by Django 2.2.10 on 2020-06-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20200629_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='number',
            field=models.IntegerField(blank=True),
        ),
    ]