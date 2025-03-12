from django.db import models
import uuid
from datetime import datetime, timedelta

class QRCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='qrcodes/files/', blank=True, null=True)
    is_temporary = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    qrcode_image = models.ImageField(upload_to='qrcodes/images/', blank=True, null=True)

    # Campos para personalização
    fill_color = models.CharField(max_length=7, default='#000000')  # Cor do QR code (hexadecimal)
    back_color = models.CharField(max_length=7, default='#FFFFFF')  # Cor de fundo (hexadecimal)
    logo = models.ImageField(upload_to='qrcodes/logos/', blank=True, null=True)  # Logo opcional

    def is_expired(self):
        if self.is_temporary and self.expiration_date:
            return datetime.now() > self.expiration_date
        return False

    def __str__(self):
        return f"QRCode {self.id}"