# Generated by Django 3.1 on 2020-08-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cassandra_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=101),
        ),
    ]
