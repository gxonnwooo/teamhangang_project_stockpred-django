# Generated by Django 4.0.2 on 2022-02-14 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockpredapp', '0010_auto_20220211_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_name',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rnn_data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rnn_result',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
