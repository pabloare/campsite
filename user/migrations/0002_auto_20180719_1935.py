# Generated by Django 2.0.5 on 2018-07-19 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joinorder',
            old_name='dish',
            new_name='dishes',
        ),
    ]