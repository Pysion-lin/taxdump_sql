# Generated by Django 3.0.4 on 2020-03-11 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxdump', '0005_auto_20200311_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nodes',
            old_name='genetic_code',
            new_name='genetic_code_id',
        ),
    ]