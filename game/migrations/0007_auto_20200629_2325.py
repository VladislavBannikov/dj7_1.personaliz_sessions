# Generated by Django 2.1.15 on 2020-06-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20200629_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='number',
            field=models.IntegerField(default=5),
        ),
    ]
