from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.forms import ModelForm
from django.contrib.auth.models import User

class Testimonial(models.Model):

    title = models.CharField(max_length=50, null=True)
    text = models.TextField()
    author = models.OneToOneField('auth.user', on_delete=models.CASCADE, blank=True, null=True)
    affiliation = models.CharField(max_length=100, blank=True)
    added = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    active = models.BooleanField(default=False)
    
def publish(self):
	self.published_date = timezone.now()
	self.save()

def __unicode__(self):
	return self.title