# Generated by Django 4.0.3 on 2022-03-31 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211102_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
