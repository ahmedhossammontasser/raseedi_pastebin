from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Paste, Typepaste
from .serializers import PasteSerializer , TypepasteSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import models

class TypepasteView(viewsets.ReadOnlyModelViewSet): 
	""" ReadOnlyModelViewSet to prevent any from adding new type """
	queryset =  Typepaste.objects.all()
	serializer_class = TypepasteSerializer

class PasteView(viewsets.ModelViewSet):
	queryset =  Paste.objects.all()
	serializer_class = PasteSerializer
	permission_classes = (permissions.AllowAny, )

	## check if type == 3 to save certain users manytomany
	def perform_create(self, serializer):
		if  self.request.user.is_anonymous :
			serializer.save()
		else :
			serializer.save(owner = self.request.user)
		
	def list(self, request):
		""" Returns a list of all pastes ,current user allowed to show/watch """
		queryset = Paste.objects.filter(models.Q(type=1) | models.Q(type=3  , allowedusers__id__exact= self.request.user.id))
		
		serializer = PasteSerializer(queryset, many=True)
		return Response(serializer.data)


	@action(detail=False, permission_classes=[permissions.IsAuthenticated])
	def get_own_pastes(self, request):
		""" Returns a list of users own pastes """
		queryset = Paste.objects.filter(owner=request.user)
		serializer = PasteSerializer(queryset, many=True)
		return Response(serializer.data)
