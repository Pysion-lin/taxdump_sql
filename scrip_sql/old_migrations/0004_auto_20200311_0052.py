# Generated by Django 3.0.4 on 2020-03-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxdump', '0003_auto_20200311_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citations',
            name='cit_key',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='citations',
            name='taxid_list',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='citations',
            name='text',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='citations',
            name='url',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]