# Generated by Django 4.1.13 on 2024-02-20 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipd', '0002_alter_bed_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipdregistration',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipd.ward'),
        ),
    ]