# Generated by Django 3.0.7 on 2020-06-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroapp', '0004_appointment_patientname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Date of Appointment',
            new_name='dateOfAppointment',
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
