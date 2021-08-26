from django.contrib import admin

from .models import (Restaurant, Food, Category, RestaurantYoutubeReview, 
                    RestaurantReview, Branch, FoodReview)

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(RestaurantReview)
admin.site.register(Branch)
admin.site.register(FoodReview)
admin.site.register(RestaurantYoutubeReview)
