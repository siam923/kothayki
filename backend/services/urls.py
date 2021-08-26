from django.urls import path

from .views import ServiceList, AreaList, YoutuberDetail, YoutuberList 


urlpatterns = [
    path('services/', ServiceList.as_view()),
    path('area/', AreaList.as_view()),
    path('youtube/', YoutuberList.as_view()),
    path('youtube/<int:pk>/', YoutuberDetail.as_view()),
]