# Generated by Django 2.0.5 on 2018-10-25 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='preapred',
            new_name='prepared',
        ),
    ]
