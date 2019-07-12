from django.db import models


class Typepaste(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Paste(models.Model):
	type = models.ForeignKey(Typepaste,
							related_name='pastes',
	 						on_delete=models.CASCADE,
	 						default=1
	 						)
	text = models.CharField(max_length=50)
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

	def __str__(self):
		return self.text 


