# Generated by Django 3.1.3 on 2022-02-11 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='USERNAME_FIELD',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
