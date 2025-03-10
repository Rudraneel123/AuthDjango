from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,LoginAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/',LoginAPIView.as_view()),
]
