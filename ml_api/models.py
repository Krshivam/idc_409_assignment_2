import os
from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.

def media_file_name(instance,filename):
	basename ,ext = os.path.splitext(filename)
	print(ext)
	base = None
	if(ext.lower() == '.csv'):
		base = 'insurance'
	else:
		base = 'gbdt'
	return os.path.join('mediafiles',base+ext.lower())


class FileUpload(models.Model):
	file = models.FileField(blank=False,null=False,upload_to=media_file_name)

class BestModel(models.Model):
	file = models.FileField(blank=False,null=False,upload_to=media_file_name)