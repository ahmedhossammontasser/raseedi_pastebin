from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token  

router = routers.DefaultRouter()
router.register('pastes', views.PasteView)
router.register('typepastes', views.TypepasteView)
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
	path('',include(router.urls)),
	# path('api-auth',include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  

]
