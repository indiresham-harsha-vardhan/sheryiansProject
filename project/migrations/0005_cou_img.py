# Generated by Django 5.1.3 on 2025-01-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='cou',
            name='img',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
