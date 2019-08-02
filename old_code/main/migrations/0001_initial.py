# Generated by Django 2.0.6 on 2018-08-04 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('sequoia_admin', 'Full access to Sequoia'),),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('sequoia_admin', 'Full access to Sequoia'),),
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('sequoia_admin', 'Full access to Sequoia'),),
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('sequoia_admin', 'Full access to Sequoia'),),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('sequoia_admin', 'Full access to Sequoia'),),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('sequoia_admin', 'Full access to Sequoia'),),
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(verbose_name='transaction date')),
                ('report_description', models.CharField(max_length=200)),
                ('custom_description', models.CharField(blank=True, max_length=200)),
                ('expense', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Status')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Store')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.SubCategory')),
            ],
            options={
                'permissions': (('sequoia_admin', 'Full access to Sequoia'),),
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Transaction'),
        ),
    ]