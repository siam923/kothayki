from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views

'''
Important : My solution was to override the email template that calls the reverse of "password_reset_confirm". 
Make sure email template sends a URL to your frontend app with the UID and Token in the URL 
(instead of trying to reverse "password_reset_confirm").

Your frontend's route should take the URL, parse it and then with the updated user's password and send it back as an API call to your backend to confirm.
https://stackoverflow.com/questions/28418233/noreversematch-at-rest-auth-password-reset

### ToDO:
Override email templatle view
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('services.urls')),
    path('api/v1/restaurants/', include('restaurants.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
