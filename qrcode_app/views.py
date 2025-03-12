import qrcode
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import QRCode
from io import BytesIO
from django.core.files.base import ContentFile
from datetime import datetime, timedelta

def generate_qrcode(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        file = request.FILES.get('file')
        is_temporary = request.POST.get('is_temporary') == 'on'
        expiration_days = request.POST.get('expiration_days')

        # Define expiration_date como None se expiration_days não for fornecido
        expiration_date = None
        if is_temporary and expiration_days:
            expiration_date = datetime.now() + timedelta(days=int(expiration_days))

        qr = QRCode(
            link=link,
            file=file,
            is_temporary=is_temporary,
            expiration_date=datetime.now() + timedelta(days=expiration_days) if is_temporary else None
        )
        qr.save()

        # Gerar o QR code
        qr_data = link if link else qr.file.url
        qr_img = qrcode.make(qr_data)
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        qr.qrcode_image.save(f'{qr.id}.png', ContentFile(buffer.getvalue()), save=False)
        qr.save()

        return render(request, 'qrcode_app/qrcode_detail.html', {'qr': qr})

    return render(request, 'qrcode_app/generate_qrcode.html')

def qrcode_detail(request, qr_id):
    qr = get_object_or_404(QRCode, id=qr_id)
    return render(request, 'qrcode_app/qrcode_detail.html', {'qr': qr})