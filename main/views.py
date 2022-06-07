from rest_framework.viewsets import ModelViewSet
from .serializers import SkillSerializer, EnemySerializer, ThingSerializer, LocationSerializer
from .models import Skill, Enemy, Thing, Location
from rest_framework.generics import ListAPIView 
import django_filters.rest_framework
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delSkill(self,request, pk=None):
        skill=self.queryset.get(id=pk)
        skill.delete()
        return Response('Succses')



class EnemyViewSet(ModelViewSet):
    queryset = Enemy.objects.all()
    serializer_class = EnemySerializer


class ThingViewSet(ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class GetThingView(ListAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title','damage']


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class GetLocationView(ListAPIView):
    queryset = Location.objects.filter( Q(enemy__enemy_name='Демон') )
    serializer_class = LocationSerializer
