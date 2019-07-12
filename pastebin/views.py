from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import models

from .models import Paste, Typepaste
from .serializers import PasteSerializer, TypepasteSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action

from datetime import datetime

class UserViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing user instances.
	"""
	serializer_class = UserSerializer
	queryset = User.objects.all()

class TypepasteView(viewsets.ReadOnlyModelViewSet): 
	""" ReadOnlyModelViewSet to prevent any from adding new type """
	queryset =  Typepaste.objects.all()
	serializer_class = TypepasteSerializer

class PasteView(viewsets.ModelViewSet):
	queryset =  Paste.objects.all()
	serializer_class = PasteSerializer
	permission_classes = (permissions.AllowAny, IsOwnerOrReadOnly,)
        
	## check if type == 3 to save certain users manytomany
	def perform_create(self, serializer):
		if  self.request.user.is_anonymous :
			serializer.save()
		else :
			serializer.save(owner = self.request.user)
		
	def list(self, request):
		""" Returns a list of all pastes ,current user allowed to show/watch order by created_at"""
		queryset = Paste.objects.filter(models.Q(type=1) | models.Q(type=3  , allowedusers__id__exact= self.request.user.id)).order_by('-created_at')
		
		serializer = PasteSerializer(queryset, many=True)
		return Response(serializer.data)

	@action(detail=False, permission_classes=[permissions.IsAuthenticated])
	def get_own_pastes(self, request):
		
		""" Returns a list of users own pastes """
		queryset = Paste.objects.filter(owner=request.user)

		start_date = self.request.query_params.get('start_date', None)
		end_date = self.request.query_params.get('end_date', None)

		if start_date is not None:
			start_date = datetime.strptime( start_date , '%Y-%m-%d')
			end_date = datetime.strptime( end_date , '%Y-%m-%d')
			queryset = queryset.filter(created_at__range=(
                 start_date  ,  end_date   
            ))

		serializer = PasteSerializer(queryset, many=True)
		return Response(serializer.data)
