# Generated by Django 2.0.5 on 2018-07-16 17:38

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
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_order', to='manager.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='noUsername', max_length=30)),
                ('note', models.CharField(max_length=300)),
                ('dishes', models.ManyToManyField(through='user.JoinOrder', to='manager.Dish')),
                ('seat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='manager.Seat')),
            ],
        ),
        migrations.AddField(
            model_name='joinorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='user.Order'),
        ),
    ]
