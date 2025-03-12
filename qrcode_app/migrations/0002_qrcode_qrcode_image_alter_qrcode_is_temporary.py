# Generated by Django 5.1.7 on 2025-03-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='qrcode_image',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes/images/'),
        ),
        migrations.AlterField(
            model_name='qrcode',
            name='is_temporary',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
