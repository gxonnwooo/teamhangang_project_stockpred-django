# Generated by Django 3.1.3 on 2022-02-14 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_merge_20220214_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]