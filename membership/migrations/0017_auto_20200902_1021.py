# Generated by Django 3.1 on 2020-09-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0016_history_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='order_no',
            field=models.IntegerField(default=0, verbose_name='주문번호'),
        ),
        migrations.AddField(
            model_name='history',
            name='select_adr',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='주문매장'),
        ),
    ]
