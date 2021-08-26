from django.shortcuts import render
from rest_framework import generics

from .models import Service, Area, YoutubeReview
from .serializers import ServiceSerializer, AreaSerializer, YoutuberReviewSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class YoutuberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = YoutubeReview.objects.all()
    serializer_class = YoutuberReviewSerializer

class YoutuberList(generics.ListCreateAPIView):
    queryset = YoutubeReview.objects.all()
    serializer_class = YoutuberReviewSerializer