# Generated by Django 3.0.4 on 2020-09-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='startDate',
            field=models.DateTimeField(),
        ),
    ]
