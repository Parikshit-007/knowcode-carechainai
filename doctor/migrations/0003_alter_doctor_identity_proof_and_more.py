# Generated by Django 4.1.13 on 2024-02-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_identity_proof_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='identity_proof',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='medical_liscence',
            field=models.TextField(),
        ),
    ]
