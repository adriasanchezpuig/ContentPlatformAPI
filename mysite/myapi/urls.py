from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contents/', views.ContentViewSet.as_view(), name="contents"),
    path('channels/', views.ChannelViewSet.as_view(), name="channels"),
    path('platform/', views.PlatformViewSet.as_view(), name="platform"),
]