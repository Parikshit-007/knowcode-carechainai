# Generated by Django 4.1.13 on 2024-02-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_identity_proof_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='identity_proof',
            field=models.FileField(upload_to='identity_proofs/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='medical_liscence',
            field=models.FileField(upload_to='medical_licenses/'),
        ),
    ]
