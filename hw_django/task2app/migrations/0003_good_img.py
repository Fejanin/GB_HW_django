# Generated by Django 4.2.8 on 2024-01-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task2app', '0002_alter_client_date_alter_good_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='test'),
        ),
    ]
