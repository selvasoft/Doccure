# Generated by Django 3.0.7 on 2020-06-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_auto_20200625_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]