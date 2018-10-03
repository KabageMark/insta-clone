from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile-pics')
    bio = models.TextField()

    
class Image(models.Model):
    image = models.ImageField(upload_to='images-uploaded')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    image_profile = ForeignKey(Profile)
    image_likes = models.PositiveIntegerField(max_length =30)
    image_comments = models.CharField(max_length =30)
