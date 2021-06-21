from django.db import models

# Create your models here.
class Docs(models.Model):
	title = models.CharField(max_length=100)
	document_up = models.FileField(upload_to='')

	def __str__(self):
		return self.title

	def delete(self, *args, **kwargs):
		self.document_up.delete()
		super().delete(*args, **kwargs)


