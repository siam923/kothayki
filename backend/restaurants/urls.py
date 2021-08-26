from django.urls import path

from .views import (CatagoryList, RestaurantList,
                    BranchList, BranchDetail,
                    FoodList, FoodReviewList, RestaurantReviewList,
                    RestaurantYoutubeList, RestaurantDetail,
                    FoodDetail, RestaurantReviewDetail)


urlpatterns = [
    path('', RestaurantList.as_view()),
    path('categories/', CatagoryList.as_view()),
    path('branches/', BranchList.as_view()),
    path('branches/<int:pk>', BranchDetail.as_view()),
    path('<int:rest_id>/foods/', FoodList.as_view()),
    path('foods/<int:food_id>/review/', FoodReviewList.as_view()),
    path('<int:pk>/reviews', RestaurantReviewList.as_view()),
    path('<int:rest_id>/youtube/reveiws', RestaurantYoutubeList.as_view()),
    path('<int:pk>/', RestaurantDetail.as_view()),
    path('foods/<int:pk>/', FoodDetail.as_view()),
    path('reviews/<int:pk>/', RestaurantReviewDetail.as_view()),
]
