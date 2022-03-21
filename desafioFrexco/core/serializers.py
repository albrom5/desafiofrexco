from rest_framework import serializers
from desafioFrexco.core.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False)

    def create(self, validated_data):
        user = super().create(validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'birth_date', 'password']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'birth_date']