# Generated by Django 3.0.7 on 2020-06-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroapp', '0003_auto_20200623_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patientName',
            field=models.CharField(default='patient 1', max_length=100),
        ),
    ]