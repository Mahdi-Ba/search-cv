# Generated by Django 2.2 on 2020-05-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20200428_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='en_title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
