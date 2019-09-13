from django.urls import path
from .views import current_user, UserList, ClientViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('clients', ClientViewSet, basename='client')
urlpatterns = [
    path('api/',include(router.urls)),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]