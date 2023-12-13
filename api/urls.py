from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'producto',views.ProductoViewSet,basename='mathilo')
router.register(r'proveedor',views.ProveedorViewSet,basename='mathilo')

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('producto',views.ProductoView.as_view()),
    path('user',views.UserView.as_view()),
    path('user/profile', views.UserProfileView.as_view(), name='user-profile'),  # Ruta para obtener detalles del perfil del usuario actual
    path('user/update-profile', views.UpdateProfileView.as_view(), name='update-profile'),  # Ruta para actualizar el perfil del usuario
    path('carrito',views.CarritoView.as_view()),
    path('proveedor',views.ProveedorView.as_view()),
    path('pedidoPersonalizadoapp',views.PedidoPersonalizadoAppView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('producto/<int:producto_id>',views.ProductoDetailView.as_view()),
    path('user/<int:user_id>',views.UserDetailView.as_view()),
    path('carrito/<int:carrito_id>',views.CarritoDetailView.as_view()),
    path('proveedor/<int:proveedor_id>',views.ProveedorDetailView.as_view()),
    path('pedidoPersonalizadoapp/<int:pedidopersonalizadoapp_id>',views.PedidoPersonalizadoAppDetailView.as_view()),
    path('pedidospersonalizadosapp/', views.PedidoPersonalizadoAppView.as_view(), name='pedidospersonalizadosapp'),
    path('admin/',include(router.urls)),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token-create'),  # Nueva ruta para la autenticación
    path('pedidoPersonalizado',views.PedidoPersonalizadoView.as_view()),
    path('pedidoPersonalizado/<int:pedidopersonalizado_id>',views.PedidoPersonalizadoDetailView.as_view()),
    path('pedidospersonalizados/', views.PedidoPersonalizadoView.as_view(), name='pedidospersonalizados'),
    path('registro/', views.RegistroAPIView.as_view(), name='registro'),
]