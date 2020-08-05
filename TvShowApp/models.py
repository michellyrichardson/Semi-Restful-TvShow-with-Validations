from django.db import models

# Create your models here.
class ShowsManager(models.Manager):
    def show_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 2:
            errors['title'] = "Title must be at least 2 characters long"
        if len(post_data['network']) < 3:
            errors['network'] = "Network must be at least 3 characters long"
        if len(post_data['description']) < 10:
            errors['description'] = "Description must be at least 10 characters long"
        return errors

class Showsnew(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()

class Allshows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()