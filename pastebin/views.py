from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count

from .models import Paste, Typepaste
from .serializers import PasteSerializer, TypepasteSerializer, UserSerializer, SatatisticSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework_csv.renderers import CSVRenderer

from datetime import datetime

class UserViewSet(viewsets.ViewSet):
	"""
	A ViewSet for listing  users.
	"""
	def list(self, request):
		queryset = User.objects.all()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)

class TypepasteView(viewsets.ReadOnlyModelViewSet): 
	"""
		ReadOnlyModelViewSet to prevent any from adding new type 
	"""
	queryset =  Typepaste.objects.all()
	serializer_class = TypepasteSerializer

class PasteView(viewsets.ModelViewSet):
	"""
		ModelViewSet  

    retrieve:
        Return the given paste.
		Anonymous user can watch all public paste 

    create:
        Create a new paste.

    destroy:
        Delete a paste.

    update:
        Update a paste.

    """	
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
		"""
			Returns a list of all pastes which current_user allowed to show/watch order by created_at
			Anonymous user can watch all public paste 
		"""
		queryset = Paste.objects.filter(models.Q(type=1) | models.Q(type=3  , allowedusers__id__exact= self.request.user.id)).order_by('-created_at')
		
		serializer = PasteSerializer(queryset, many=True)
		return Response(serializer.data)

	@action(detail=False, permission_classes=[permissions.IsAuthenticated])
	def get_own_pastes(self, request):
		""" 
			Returns a list of users own pastes 
		"""
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


	@action(detail=False, renderer_classes=[CSVRenderer])
	def statistics(request, format=None):
		""" 
			Returns csv file contain a list of users_id and counter of own pastes  
		"""
		pastes_grouped_by_owner_id = Paste.objects.all().values('owner' ).annotate(total=Count('type')).order_by('total')
		serializer = SatatisticSerializer(pastes_grouped_by_owner_id, many=True)
		return Response( serializer.data )
