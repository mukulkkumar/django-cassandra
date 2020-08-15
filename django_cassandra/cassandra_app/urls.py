from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
