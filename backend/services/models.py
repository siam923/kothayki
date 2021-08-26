from django.db import models
from django.contrib.auth import get_user_model



## Service Type model
class Service(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


## City model
class City(models.Model):
    ## Dhaka, Chittagong, Cumilla, etc
    city_name = models.CharField(max_length=50) 

    def __str__(self):
        return self.city_name 


class Area(models.Model):
    ## e.g. panthapath, dhanmondi etc
    area_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.area_name} of {self.city.city_name}'
    
    class Meta:
        unique_together = ['area_name', 'city']

## Review Model
class YoutubeReview(models.Model):
    title = models.CharField(max_length=200)
    youtuber = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    link = models.URLField(max_length=200)

    def __str__(self):  
        return self.title + ' by ' + self.youtuber.username



    
