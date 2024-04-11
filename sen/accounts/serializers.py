from rest_framework import serializers
from .models import User, Material, MaterialInfo, MaterialRejection, Room, RoomMessage, FavoriteMaterial

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone', 'full_name', 'is_customer', 'is_expert']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'author', 'title', 'description', 'pdf_file', 'subject', 'grade', 'rating', 'status', 'created_at', 'filename', 'is_new', 'created_at_with_timezone']

class MaterialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialInfo
        fields = ['id', 'material', 'user', 'user_rating', 'user_comment', 'commented_at', 'created_at', 'created_at_with_timezone']

class MaterialRejectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRejection
        fields = ['id', 'material', 'expert', 'created_at', 'description', 'created_at_with_timezone']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'customer', 'name']

class RoomMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMessage
        fields = ['id', 'room', 'author', 'body', 'response_body', 'created_at']

class FavoriteMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMaterial
        fields = ['id', 'user', 'material']
