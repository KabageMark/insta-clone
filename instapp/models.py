from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile-pics')
    bio = models.TextField()
    username = models.CharField(max_length =30)

    @classmethod
    def search_by_username(cls,search_term):
        user = Users.objects.filter(user__name__icontains=search_term)
        return user
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
    image_profile = ForeignKey(Profile)
    image_likes = models.PositiveIntegerField()
    image_comments = models.TextField()
    
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