# Generated by Django 4.1.13 on 2024-05-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipd', '0008_alter_ipdregistration_bed'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward',
            name='daily_charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
