from django.db import models

# Create a model, inheriting from the Django models class (always make your ORM this way)
class Hubapp(models.Model):
    # There are many, many fields available, see Django documentation for other types
    # Charfield limits the length, good field to use for titles 
    title = models.CharField(max_length=100)
    # TextField allows for a longer description
    description = models.TextField()
    technology = models.CharField(max_length=200)
    # FilePathField will be a string, it has restrictions
    image = models.CharField(max_length=100)
    link1 = models.CharField(max_length=500)