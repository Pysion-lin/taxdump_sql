# Generated by Django 3.0.4 on 2020-03-11 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxdump', '0007_auto_20200311_0835'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='citations',
            unique_together=set(),
        ),
    ]
