from rest_framework import serializers
from .models import Paste, Typepaste


class UserSerializer(serializers.ModelSerializer):
	username = serializers.CharField(max_length=100)

class PasteSerializer(serializers.ModelSerializer):
	type_name = serializers.CharField(source='type.name')
	owner_name = serializers.CharField(source='owner')

	class Meta: 
		model = Paste
		fields = ('id', 'type_name', 'owner_name', 'text', 'allowedusers', 'created_at')
		read_only_fields = ('owner' , )


class TypepasteSerializer(serializers.HyperlinkedModelSerializer):

	class Meta: 
		model = Typepaste
		fields = ('id', 'name', 'url') 


