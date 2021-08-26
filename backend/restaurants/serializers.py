from rest_framework import serializers

from services.models import YoutubeReview
from .models import (Category, Restaurant, Food,
                     Branch, RestaurantReview, FoodReview,
                     RestaurantYoutubeReview)
from services.serializers import YoutuberReviewSerializer, AreaSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerOfRestOrReadOnly
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    permission_classes = (IsOwnerOrReadOnly,)
    category = CategorySerializer(read_only=True)
    youtube_review = YoutuberReviewSerializer(read_only=True)
    owner = UserSerializer()

    class Meta:
        model = Restaurant
        fields = '__all__'
        read_only_fields = ('ratings', 'sponsored', 'featured',)


class BranchSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    location = AreaSerializer()

    class Meta:
        model = Branch
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    permission_classes = (IsOwnerOfRestOrReadOnly,)

    class Meta:
        model = Food
        fields = '__all__'


class FoodReviewSerializer(serializers.ModelSerializer):

    #review = YoutuberReviewSerializer()
    # user = UserSerializer()

    class Meta:
        model = FoodReview
        fields = '__all__'

    # def create(self, validated_data):
    #     youtuber_validated_data = validated_data.pop('review')
    #     youtuber_review = YoutubeReview.objects.create(youtuber_validated_data)
    #     food = validated_data.pop('food')
    #     new_review = FoodReview.objects.create(
    #                     review=youtuber_review,
    #                     food=food)
    #     return new_review


class RestaurantReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = RestaurantReview
        fields = '__all__'


class RestaurantYoutubeReviewSerializer(serializers.ModelSerializer):
    review = YoutuberReviewSerializer()

    class Meta:
        model = RestaurantYoutubeReview
        fields = '__all__'
