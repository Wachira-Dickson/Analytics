from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('countries', CountryViewset, basename='country')
router.register('leagues', LeagueViewset, basename='league')
router.register('characteristics', CharacteristicViewset, basename='characteristic')
urlpatterns = router.urls
