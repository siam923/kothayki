from django.contrib import admin

from .models import Service, YoutubeReview, City, Area


admin.site.register(Service)
admin.site.register(YoutubeReview)
admin.site.register(City)
admin.site.register(Area)