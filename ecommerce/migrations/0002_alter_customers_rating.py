# Generated by Django 3.2.7 on 2021-09-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Select'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
