# Generated by Django 2.1.4 on 2019-01-11 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_auto_20190111_1240'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('transaction_id', 'tag_name')},
        ),
    ]