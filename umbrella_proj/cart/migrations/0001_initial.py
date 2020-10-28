# Generated by Django 3.1.2 on 2020-10-28 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_ordered', models.IntegerField()),
                ('local_price', models.FloatField()),
                ('total_cost', models.FloatField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.orders')),
            ],
        ),
    ]
