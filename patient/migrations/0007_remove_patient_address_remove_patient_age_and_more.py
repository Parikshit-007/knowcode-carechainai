# Generated by Django 4.1.13 on 2024-02-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20231223_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='BroughtBy',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='CareOfPerson',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Case',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='CityTaluka',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ConditionDuringArrival',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ContactNumber',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='MiddleName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ModeOfArrival',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ReferredBy',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='RelationWithPatient',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Religion',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='State',
        ),
        migrations.AddField(
            model_name='patient',
            name='Insurance_Provider',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='Insurance_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='Relationship',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='allergy',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='blood',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='card_num',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='facility_code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='fullname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='patient',
            name='initial_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='membernum',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='referred',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]