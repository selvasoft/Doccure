# Generated by Django 3.0.7 on 2020-06-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroapp', '0002_auto_20200623_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointmentId',
            field=models.CharField(default='00', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctorMail',
            field=models.EmailField(default='doc@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patientMail',
            field=models.EmailField(default='patient@gmail.com', max_length=100),
        ),
    ]
