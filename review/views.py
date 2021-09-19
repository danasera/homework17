from django.shortcuts import render



from rest_framework import viewsets

from .models import Review
from .serializers import ReviewSerializer, ReviewListSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        return ReviewSerializer