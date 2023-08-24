# Generated by Django 4.2.4 on 2023-08-14 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('YAC', 'AC'), ('NAC', 'NON-AC'), ('DEL', 'DELUXE'), ('QUE', 'QUEEN'), ('KIN', 'KING')], max_length=50),
        ),
    ]
