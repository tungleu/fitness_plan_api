from rest_framework import serializers

from core.models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ('id', 'name')
        read_only_fields = ('id')