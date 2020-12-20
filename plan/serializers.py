from rest_framework import serializers

from core.models import Exercise, Plan


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id', 'name')
        read_only_fields = ('id',)


class PlanSerializer(serializers.ModelSerializer):
    exercises = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Exercise.objects.all()
    )

    class Meta:
        model = Plan
        fields = ('id', 'title', 'exercises', 'description', 'link')
        read_only_fields = ('id',)


class PlanDetailSerialzer(PlanSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)
