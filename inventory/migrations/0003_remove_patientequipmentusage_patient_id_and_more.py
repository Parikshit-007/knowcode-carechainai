# Generated by Django 4.1.13 on 2024-02-20 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_remove_patient_address_remove_patient_age_and_more'),
        ('inventory', '0002_patientequipmentusage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientequipmentusage',
            name='patient_id',
        ),
        migrations.AddField(
            model_name='patientequipmentusage',
            name='patient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]
