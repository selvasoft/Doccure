# Generated by Django 3.0.7 on 2020-06-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restroapp', '0010_auto_20200628_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('UNREVIEWED', 'Not Reviewed'), ('ACCEPTED', 'Accept'), ('DECLINED', 'Reject')], default='Unreviewed', max_length=20),
        ),
    ]