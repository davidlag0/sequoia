# Generated by Django 2.0.6 on 2018-07-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180725_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='custom_description',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
