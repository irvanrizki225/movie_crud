from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source = 'creator.username')

    class Meta:
        model = Movie
        # fields = ('id', 'judul', 'genre', 'year', 'creator')
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(many = True, queryset = Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movie')
