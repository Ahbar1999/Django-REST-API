# Generated by Django 4.1.7 on 2023-03-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]