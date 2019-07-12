from django.db import models
import uuid


class Typepaste(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Paste(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)	
	text = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	type = models.ForeignKey(Typepaste,
							related_name='pastes',
	 						on_delete=models.CASCADE,
	 						default=1
	 						)
	owner = models.ForeignKey('auth.User',
							   related_name='owner',
							   blank = True,
							   null = True,
							   on_delete=models.CASCADE
							)

	allowedusers = models.ManyToManyField(
						'auth.User',
						related_name='allowedusers',
						verbose_name="list of allowed users",
						blank = True,
						null = True
					)

	class meta:
		ordering = ['created_at']


	def __str__(self):
		return self.text 


