from rest_framework.serializers import ModelSerializer
from .models import Location, Thing, Enemy, Skill


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'

class EnemySerializer(ModelSerializer):
    class Meta:
        model = Enemy
        fields = '__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'