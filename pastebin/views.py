from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Paste, Typepaste
from .serializers import PasteSerializer , TypepasteSerializer

class TypepasteView(viewsets.ReadOnlyModelViewSet): 
	## ReadOnlyModelViewSet to prevent autjorized user adding new type
	queryset =  Typepaste.objects.all()
	serializer_class = TypepasteSerializer

class PasteView(viewsets.ModelViewSet):
	queryset =  Paste.objects.all()
	serializer_class = PasteSerializer

	permission_classes = (permissions.AllowAny, 	)
	# permission_classes = ( permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly) 

	def perform_create(self, serializer):
		if  self.request.user.is_anonymous :
			serializer.save()
		else :
			serializer.save(owner = self.request.user)
		
	    
