# Generated by Django 4.1.13 on 2024-02-27 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hos_login', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
