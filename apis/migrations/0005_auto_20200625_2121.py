# Generated by Django 3.0.7 on 2020-06-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20200623_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='Mumbai , MH', max_length=200),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(default='', upload_to='profilePic'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profession',
            field=models.CharField(default='MD', max_length=50),
        ),
    ]
