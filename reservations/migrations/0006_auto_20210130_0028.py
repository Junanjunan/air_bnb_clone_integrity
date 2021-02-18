# Generated by Django 3.1.4 on 2021-01-29 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20210130_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedday',
            name='day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation'),
        ),
    ]
