from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated  # Agregada importación
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from venta.models import Categoria, Producto, PedidoPersonalizado, Proveedor, PedidoPersonalizadoApp
from venta.carrito import Carrito

from .serializers import (
    UserSerializer,
    CategoriaSerializer,
    ProductoSerializer,
    CarritoSerializer,
    PedidoPersonalizadoSerializer,
    ProveedorSerializer,
    PedidoPersonalizadoAppSerializer,
    CustomTokenObtainPairSerializer,
    RegistroSerializer
)
##APP

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Vista personalizada para obtener el par de tokens (access y refresh)
    utilizando el email y contraseña del usuario.
    """
    serializer_class = CustomTokenObtainPairSerializer # Asegúrate de crear este serializador

class UserProfileView(APIView):


    def get(self, request, *args, **kwargs):
        # Lógica para obtener y devolver detalles del perfil del usuario actual
        user = request.user  # Obtener el usuario autenticado
        # Puedes personalizar esto según tu modelo de usuario y cómo almacenas la información del perfil
        profile_data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_staff': user.is_staff,
            # Agrega otros campos del perfil que quieras devolver
        }
        return Response(profile_data, status=status.HTTP_200_OK)

class UpdateProfileView(APIView):

    def post(self, request, *args, **kwargs):
        # Lógica para actualizar el perfil del usuario
        user = request.user  # Obtener el usuario autenticado
        # Puedes personalizar esto según tu modelo de usuario y cómo almacenas la información del perfil
        # Recibe los datos del perfil actualizados desde el cuerpo de la solicitud (request.data)
        # Actualiza los campos del perfil según sea necesario
        # Guarda los cambios en la base de datos
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        user.email = request.data.get('email', user.email)
        # Agrega otros campos del perfil que quieras actualizar
        user.save()
        return Response({'message': 'Perfil actualizado correctamente'}, status=status.HTTP_200_OK)

class RegistroAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistroSerializer

##DJANGO 

class IndexView(APIView):
    
    def get(self,request):
        lista_categorias = Categoria.objects.all()
        serializer_categoria = CategoriaSerializer(lista_categorias,many=True)
        return Response(serializer_categoria.data)
    
class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg  = 'categoria_id'
    serializer_class = CategoriaSerializer

##
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    lookup_url_kwarg  = 'producto_id'
    serializer_class = ProductoSerializer
    
class ProductoView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

##

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_url_kwarg  = 'user_id'
    serializer_class = UserSerializer
    
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

##

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrito.objects.all()
    lookup_url_kwarg  = 'carrito_id'
    serializer_class = CarritoSerializer
    
class CarritoView(generics.ListAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

##

class PedidoPersonalizadoViewSet(viewsets.ModelViewSet):
    queryset = PedidoPersonalizado.objects.all()
    serializer_class = PedidoPersonalizadoSerializer

class PedidoPersonalizadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PedidoPersonalizado.objects.all()
    lookup_url_kwarg  = 'pedidopersonalizado_id'
    serializer_class = PedidoPersonalizadoSerializer
    
class PedidoPersonalizadoView(generics.ListAPIView):
    queryset = PedidoPersonalizado.objects.all()
    serializer_class = PedidoPersonalizadoSerializer


class PedidoPersonalizadoView(generics.CreateAPIView):
    queryset = PedidoPersonalizado.objects.all()
    serializer_class = PedidoPersonalizadoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

##

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    lookup_url_kwarg  = 'Proveedor_id'
    serializer_class = ProveedorSerializer
    
class ProveedorView(generics.ListAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

###


class PedidoPersonalizadoAppViewSet(viewsets.ModelViewSet):
    queryset = PedidoPersonalizadoApp.objects.all()
    serializer_class = PedidoPersonalizadoAppSerializer

class PedidoPersonalizadoAppDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PedidoPersonalizadoApp.objects.all()
    lookup_url_kwarg  = 'pedidopersonalizadoapp_id'
    serializer_class = PedidoPersonalizadoAppSerializer
    
class PedidoPersonalizadoAppView(generics.ListAPIView):
    queryset = PedidoPersonalizadoApp.objects.all()
    serializer_class = PedidoPersonalizadoAppSerializer


class PedidoPersonalizadoAppView(generics.CreateAPIView):
    queryset = PedidoPersonalizadoApp.objects.all()
    serializer_class = PedidoPersonalizadoAppSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    



