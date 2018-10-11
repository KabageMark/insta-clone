from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile-pics')
    bio = models.TextField()
    user= models.ForeignKey(User)

    @classmethod
    def get_all(cls):
        all_objects = Profile.objects.all()
        return all_objects
     
    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(user__name__icontains=search_term)
        return profile
    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Image.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def save_image(self):
        return self.save()

    @classmethod   
    def delete_image(self):
        return self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images-uploaded')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    image_likes = models.PositiveIntegerField()
    image_comments = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    
    @classmethod
    def get_all(cls):
        all_objects = Image.objects.all()
        return all_objects

    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result

    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Image.objects.filter(name=current_value).update(name=new_value)
        return fetched_object

    @classmethod
    def save_image(self):
        return self.save()

    @classmethod    
    def delete_image(self):
        return self.delete()
 
class Comment(models.Model):
    user = models.ForeignKey(User,null=True)
    post=models.ForeignKey(Image,related_name='comments',null=True)
    comment=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    user = models.OneToOneField(User,related_name='l_user')
    post=models.ForeignKey(Image,related_name='likes')
    like=models.CharField(max_length=3,default='1')