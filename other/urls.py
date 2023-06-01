from django.urls import path
from .views import CurrentDateView, RandomNumberView, HelloWorldView, IndexView

urlpatterns = [
    path('datetime/', CurrentDateView.as_view(), name='datetime'),
    path('random/', RandomNumberView.as_view(), name='random'),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('index/', IndexView.as_view(), name='index'),
]