# Generated by Django 5.1.7 on 2025-03-12 01:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.URLField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='qrcodes/files/')),
                ('is_temporary', models.BooleanField(default=False)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
