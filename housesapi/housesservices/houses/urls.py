from django.urls import path

from .views import HouseViewSet, home
from .views import CheckerAPIView

urlpatterns = [
    path('', home, name='home'),
    path('houses', HouseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('houses/<str:pk>', HouseViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('checker', CheckerAPIView.as_view())
]
