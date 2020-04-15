from django.db import models

class Todo(models.Model):

	title= models.CharField(max_length=100)
	description=models.TextField()
	timestamp= models.DateTimeField(auto_now=True)
	is_completed=models.BooleanField(default=False)
