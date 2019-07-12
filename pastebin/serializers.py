from rest_framework import serializers
from .models import Paste, Typepaste


class UserSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=100)

class PasteSerializer(serializers.ModelSerializer):
	type_name = serializers.CharField(source='type.name', read_only=True)
	owner_name = serializers.CharField(source='owner', read_only=True)

	class Meta: 
		model = Paste
		fields = ('id', 'type','type_name', 'owner_name', 'text', 'allowedusers', 'created_at')
		read_only_fields = ('owner','type_name', 'owner_name')


class TypepasteSerializer(serializers.HyperlinkedModelSerializer):

	class Meta: 
		model = Typepaste
		fields = ('id', 'name', 'url') 


