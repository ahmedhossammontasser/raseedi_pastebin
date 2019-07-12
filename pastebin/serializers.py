from rest_framework import serializers
from .models import Paste, Typepaste

class PasteSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Paste
		fields = ('id', 'type', 'text', 'allowedusers' , 'owner')
		read_only_fields = ('owner' , )


class TypepasteSerializer(serializers.ModelSerializer):

	class Meta: 
		model = Typepaste
		fields = ('id', 'name') 

