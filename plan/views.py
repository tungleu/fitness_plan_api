from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Exercise, Plan

from plan import serializers


class BasePlanComponentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseViewSet(BasePlanComponentViewSet):
    queryset = Exercise.objects.all()
    serializer_class = serializers.ExerciseSerializer
    def get_serializer_class(self):
        if self.action == 'upload_image':
            return serializers.ExerciseImageSerializer
        return self.serializer_class
    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        exercise = self.get_object()
        serializers = self.get_serializer(
            exercise,
            data=request.data
        )
        if serializers.is_valid():
            serializers.save()
            return Response(
                serializers.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializers.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlanSerializer
    queryset = Plan.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.PlanDetailSerialzer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
