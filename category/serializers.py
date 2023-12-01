from rest_framework import serializers
from .models import Specialist, Works, Category

class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ('name', 'rate', 'id')

class WorkSerializer(serializers.ModelSerializer):
    specialist_type = SpecialistSerializer(many=False)
    class Meta:
        model = Works
        fields = ('id', 'name', 'hours', 'count', 'specialist_type' )

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = ('id', )

class CatergorySerializer(serializers.ModelSerializer):
    #services = WorksSerializer(many=True)
    class Meta:
        model = Category
        fields = ('name', 'id', 'services', 'isOriginal')

