from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    is_youtuber = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    @property
    def group(self):
        groups = self.groups.all()
        return groups[0].name if groups else None
