from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pastes', views.PasteView)
router.register('Typepastes', views.TypepasteView)

urlpatterns = [
	path('',include(router.urls)),
	path('api-auth',include('rest_framework.urls'))
]
