from django.db import models


class chatClient(models.Model):
	
	messageClient = models.TextField(null=True)
	reponseBot	  = models.TextField(null=True)
	def __unicode__(self):
		return self.titre



