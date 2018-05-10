from django.db import models
from django.contrib.auth.models import User

class Disease(models.Model):
	user = models.ForeignKey(User)
	#title = models.CharField(max_length=50)
	count = models.IntegerField(default=0)
	#temp = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username + " " + str(self.count)
