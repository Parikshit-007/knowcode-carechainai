# Generated by Django 4.1.13 on 2024-02-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipd', '0003_alter_ipdregistration_ward'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipdregistration',
            name='discharge_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
