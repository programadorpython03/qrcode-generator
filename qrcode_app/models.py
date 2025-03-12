from django.db import models
import uuid
from datetime import datetime, timedelta

class QRCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='qrcodes/files/', blank=True, null=True)
    is_temporary = models.BooleanField(default=False, blank=True, null=True)
    qrcode_image = models.ImageField(upload_to='qrcodes/images/', blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        if self.is_temporary and self.expiration_date:
            return datetime.now() > self.expiration_date
        return False

    def __str__(self):
        return f"QRCode {self.id}"