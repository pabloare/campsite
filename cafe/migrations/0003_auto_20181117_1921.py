# Generated by Django 2.0.5 on 2018-11-17 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_menu_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cafe',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='item', to='cafe.Cafe'),
        ),
        migrations.AlterField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='item', to='cafe.Menu'),
        ),
    ]
