# Generated by Django 2.0.5 on 2018-07-17 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_order', to='user.Order'),
        ),
    ]
