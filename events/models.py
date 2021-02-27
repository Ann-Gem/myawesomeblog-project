from django.db import models

# Create your models here.
class Event(models.Model):
	eveni_image = models.ImageField(upload_to='event_images/')
	eveni_text = models.CharField(max_length=300)
		