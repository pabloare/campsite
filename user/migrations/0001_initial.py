# Generated by Django 2.0.5 on 2018-08-24 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_order', to='manager.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='noUsername', max_length=30)),
                ('note', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total', models.FloatField(default=0.0)),
                ('dishes', models.ManyToManyField(through='user.JoinOrder', to='manager.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wants_to_pay', models.BooleanField(default=False)),
                ('card', models.BooleanField(default=False)),
                ('change_if_cash', models.IntegerField(default=0)),
                ('has_payed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='user.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='manager.Restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='seat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='manager.Seat'),
        ),
        migrations.AddField(
            model_name='joinorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='user.Order'),
        ),
    ]
