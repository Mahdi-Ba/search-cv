# Generated by Django 2.2 on 2020-04-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20200428_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='working_area',
            field=models.ManyToManyField(blank=True, to='prerequisites.WorkingArea'),
        ),
    ]
