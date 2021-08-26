from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import (Category, Restaurant, Branch, Food,
                     FoodReview, RestaurantReview, RestaurantYoutubeReview)
from .serializers import (CategorySerializer, RestaurantSerializer,
                          BranchSerializer, FoodSerializer,
                          FoodReviewSerializer, RestaurantReviewSerializer,
                          RestaurantYoutubeReviewSerializer)


class CatagoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RestaurantList(generics.ListCreateAPIView):
    # Ex: request- /api/v1/restaurants/?category=1&sponsored=False

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'category': ['exact', ],  # to allow null use 'isnull'
        'featured': ['iexact'],
        'sponsored': ['iexact'],
        'is_new': ['iexact'],
        'ratings': ['iexact', 'gte', ],
        'name': ['iexact', 'icontains', ],
    }


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'zone': ['exact', ],
        'location__city__city_name': ['icontains', ],
        'restaurant__category__name': ['icontains', ]
    }


class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        ''' url endpoint: restaurants/rest_id/food '''
        return Food.objects.filter(restaurant=self.kwargs['rest_id'])


class FoodReviewList(generics.ListCreateAPIView):
    serializer_class = FoodReviewSerializer

    def get_queryset(self):
        return FoodReview.objects.filter(food=self.kwargs['food_id'])


class RestaurantReviewList(generics.ListCreateAPIView):
    serializer_class = RestaurantReviewSerializer

    def get_queryset(self):
        return RestaurantReview.objects.filter(restaurant=self.kwargs['pk'])


class RestaurantYoutubeList(generics.ListCreateAPIView):
    serializer_class = RestaurantYoutubeReviewSerializer

    def get_queryset(self):
        return RestaurantYoutubeReview.objects.filter(
            restaurant=self.kwargs['rest_id'])


# Detail Views

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class RestaurantReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RestaurantReview.objects.all()
    serializer_class = RestaurantReviewSerializer
