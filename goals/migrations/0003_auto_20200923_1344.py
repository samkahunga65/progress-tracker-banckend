# Generated by Django 3.0.4 on 2020-09-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_auto_20200923_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='details',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='goal',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tracker',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='goal',
            name='startDate',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='day',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
