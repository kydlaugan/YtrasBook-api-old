# Generated by Django 4.2.4 on 2023-08-31 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_panier_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='contact_1',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact_2',
        ),
    ]
