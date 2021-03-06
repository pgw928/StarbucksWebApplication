# Generated by Django 3.0.3 on 2020-08-24 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200819_1541'),
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Histories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='상품명')),
                ('quantity', models.IntegerField(default=0, verbose_name='수량')),
                ('total', models.IntegerField(default=0, verbose_name='총가격')),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
