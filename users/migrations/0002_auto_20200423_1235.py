# Generated by Django 2.2 on 2020-04-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
