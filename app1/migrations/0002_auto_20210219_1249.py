# Generated by Django 3.1.4 on 2021-02-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockdetails',
            old_name='admin_nm',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='adminregi',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100, unique=True),
        ),
    ]
