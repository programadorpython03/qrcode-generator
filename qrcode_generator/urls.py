from django.contrib import admin
from django.urls import path
from qrcode_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', views.generate_qrcode, name='generate_qrcode'),
    path('qrcode/<uuid:qr_id>/', views.qrcode_detail, name='qrcode_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)