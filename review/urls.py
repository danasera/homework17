from django.urls import path

from .views import ReviewViewSet

urlpatterns = [
    path('reviews/', ReviewViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('reviews/<int:id>/', ReviewViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy'}
    )),
]