# Generated by Django 2.2.6 on 2019-10-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='checked_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
