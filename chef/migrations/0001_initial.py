# Generated by Django 2.0.5 on 2018-10-22 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_id', models.CharField(default='', max_length=70)),
                ('accumulator', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=300)),
                ('ready', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chef', to='chef.Chef')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_chef', to='manager.Dish')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_order', to='user.Order')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_restaurant', to='manager.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='chef',
            name='dishes',
            field=models.ManyToManyField(through='chef.Join', to='manager.Dish'),
        ),
        migrations.AddField(
            model_name='chef',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chef', to='manager.Restaurant'),
        ),
    ]
