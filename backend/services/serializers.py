from rest_framework import serializers
from .models import Service, City, Area, YoutubeReview
from users.serializers import UserSerializer


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'type',)
        model = Service


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = City


class AreaSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Area
        fields = '__all__'


class YoutuberReviewSerializer(serializers.ModelSerializer):
    youtuber = UserSerializer()

    class Meta:
        model = YoutubeReview
        fields = '__all__'
