from rest_framework import serializers
from django.contrib.auth.models import User
from venta.models import User, Categoria, Producto, PedidoPersonalizado, Proveedor, PedidoPersonalizadoApp
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from venta.carrito import Carrito

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class PedidoPersonalizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoPersonalizado
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class PedidoPersonalizadoAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoPersonalizadoApp
        fields = '__all__'

#APP
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Verifica si el usuario está activo
        if not user.is_active:
            raise serializers.ValidationError("La cuenta de usuario no está activa.")

        # Agrega el ID del usuario a la respuesta
        data['user_id'] = user.id
        data['username'] = user.username

        return data

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user