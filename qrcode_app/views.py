from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import QRCode
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from datetime import datetime, timedelta
from PIL import Image, ImageDraw

def generate_qrcode(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        file = request.FILES.get('file')
        is_temporary = request.POST.get('is_temporary') == 'on'
        fill_color = request.POST.get('fill_color', '#000000')  # Cor do QR code
        back_color = request.POST.get('back_color', '#FFFFFF')  # Cor de fundo
        logo = request.FILES.get('logo')  # Logo opcional
        expiration_days = request.POST.get('expiration_days')

        # Define expiration_date como None se expiration_days não for fornecido
        expiration_date = None
        if is_temporary and expiration_days:
            expiration_date = datetime.now() + timedelta(days=int(expiration_days))

        qr = QRCode(
            link=link,
            file=file,
            is_temporary=is_temporary,
            expiration_date=datetime.now() + timedelta(days=expiration_days) if is_temporary else None,
            fill_color=fill_color,
            back_color=back_color,
            logo=logo
        )
        qr.save()

        # Gerar o QR code
        qr_data = link if link else qr.file.url
        qr_img = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr_img.add_data(qr_data)
        qr_img.make(fit=True)

        # Criar a imagem do QR code
        img = qr_img.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')

        # Adicionar o logo (se fornecido)
        if logo:
            logo_img = Image.open(logo)
            logo_size = 50  # Tamanho do logo
            logo_img = logo_img.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            img.paste(logo_img, pos)

        # Salvar a imagem do QR code
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr.qrcode_image.save(f'{qr.id}.png', ContentFile(buffer.getvalue()), save=False)
        qr.save()

        return render(request, 'qrcode_app/qrcode_detail.html', {'qr': qr})

    return render(request, 'qrcode_app/generate_qrcode.html')

def qrcode_detail(request, qr_id):
    qr = get_object_or_404(QRCode, id=qr_id)
    return render(request, 'qrcode_app/qrcode_detail.html', {'qr': qr})