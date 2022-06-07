from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnemyViewSet, SkillViewSet, ThingViewSet, GetThingView, GetLocationView, LocationViewSet

router = DefaultRouter()
router.register('enemy', EnemyViewSet, )
router.register('skill', SkillViewSet, )
router.register('thing', ThingViewSet, )
router.register('location', LocationViewSet, )




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/thing/filters', GetThingView.as_view()),
    path('api/location/filters', GetLocationView.as_view()),
]
