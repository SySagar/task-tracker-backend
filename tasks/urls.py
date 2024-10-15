from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, AuthViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]