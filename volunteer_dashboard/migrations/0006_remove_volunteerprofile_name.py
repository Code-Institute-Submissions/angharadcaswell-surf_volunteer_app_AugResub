# Generated by Django 3.2.13 on 2022-06-14 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer_dashboard', '0005_auto_20220613_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerprofile',
            name='name',
        ),
    ]