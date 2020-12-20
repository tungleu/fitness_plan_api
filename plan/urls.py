from django.urls import path, include
from rest_framework.routers import DefaultRouter

from plan import views

router = DefaultRouter()
router.register('exercises', views.ExerciseViewSet)
router.register('plans', views.PlanViewSet)

app_name = 'plan'

urlpatterns = [
    path('', include(router.urls))
]