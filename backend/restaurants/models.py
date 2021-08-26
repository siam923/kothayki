import random
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.db.models.signals import pre_save

from services.models import Service, Area, YoutubeReview


def restaurant_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'restaurants/restaurant/restaurant_{0}/{1}'.format(instance.id, filename)


def food_image_path(instance, filename):
    new_filename = str(random.randint(1, 383232)) 
    name = new_filename + '_' + filename
    return f"restaurants/foods/{name}"


# Example google api req
# https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=YOUR_API_KEY


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(
                        upload_to='restaurants/category/thumbnail',
                        blank=True)

    def __str__(self):
        return self.name 


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=restaurant_directory_path, blank=True, null=True)
    # it will be one to one
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Restaurant Description')
    featured = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    priority = models.PositiveIntegerField(default=1)
    ratings = models.FloatField(default=0.0)

    class Meta:
        ordering = ['-priority']
    
    def __str__(self):
        return self.name


class RestaurantYoutubeReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.ForeignKey(YoutubeReview, 
            on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.restaurant.name + ' review by ' + self.review.youtuber.username


class Branch(models.Model):
    restaurant = models.ForeignKey(
            Restaurant, on_delete=models.CASCADE
        )
    name = models.CharField(max_length=50)
    lng = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    location = models.ForeignKey(Area, on_delete=models.CASCADE, default=None)
    zone = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name +' branch of ' + self.restaurant.name


## Food 
class Food(models.Model):
    image = models.ImageField(upload_to=food_image_path, blank=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=100.0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name='Food details')

    def __str__(self):
        return f"{self.name} of {self.restaurant.name}"

class FoodReview(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    text = models.TextField(blank=True, verbose_name='Food Review')
    review = models.ForeignKey(YoutubeReview, 
            on_delete=models.CASCADE, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.food.name + ' review by ' + self.review.youtuber.username

class RestaurantReview(models.Model):
    SCORE_CHOICES = zip(range(6), range(6))
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Restaurant Review')
    rating = models.PositiveSmallIntegerField(choices=SCORE_CHOICES, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'Rating({self.restaurant.name} - {self.rating} by {self.user.username})'


def pre_save_review(sender, instance, *args, **kwargs):
    rest_id = instance.restaurant.id
    review = RestaurantReview.objects.values('restaurant__id').\
                        annotate(Avg('rating'))
    avg_rating = review.get(restaurant__id=rest_id)['rating__avg']
    Restaurant.objects.filter(pk=rest_id).update(ratings=avg_rating)

pre_save.connect(pre_save_review, sender=RestaurantReview)     

## review.object.filter(id=id).aggregate(Avg('ratings'))    

# 94939454760