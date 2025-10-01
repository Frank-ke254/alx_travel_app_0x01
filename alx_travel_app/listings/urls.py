from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet
from . import views


router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path('', include(router.urls)),
]