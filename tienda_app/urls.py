from django.urls import path
from .api.views import CompraAPIView
from .views import CompraView, CompraRapidaView, compra_rapida_fbv

urlpatterns = [
    # Vista original del proyecto base
    path('compra/<int:libro_id>/', CompraView.as_view(), name='finalizar_compra'),
    path('api/v1/comprar/', CompraAPIView.as_view(), name='api_comprar'),

    # Paso 1: FBV Spaghetti
    path('compra-rapida-fbv/<int:libro_id>/', compra_rapida_fbv, name='compra_rapida_fbv'),

    # Paso 2: CBV + Service Layer
    path('compra-rapida/<int:libro_id>/', CompraRapidaView.as_view(), name='compra_rapida'),
]