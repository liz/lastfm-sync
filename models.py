import datetime
from django.db import models
from django.db.models import signals
from datetime import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class LastfmPost(models.Model):
	content_type 		= models.ForeignKey(ContentType)
	pub_date			= models.DateTimeField(default=datetime.now)
	user_name			= models.CharField(max_length=255)
	chart				= models.CharField(max_length=255)
	week_start			= models.CharField(max_length=255, blank=True)
	week_end			= models.CharField(max_length=255, blank=True)
	chart_position		= models.IntegerField(blank=True, null=True)
	play_count			= models.IntegerField(blank=True, null=True)
	url					= models.URLField(blank=True)
	artist				= models.CharField(max_length=255)
	track				= models.CharField(max_length=255)
	album				= models.CharField(max_length=255)
	
	def __unicode__(self):
		return str(self.name)
		
	def get_absolute_url(self):
		return ""
		
	class Meta:
		ordering = ['-chart']