from django.test import TestCase
from .models import Image,Profile
# Create your tests here.
class instagram_TestCases(TestCase):
    def setUp(self):
        self.new_image = Image(name='Dance')
        self.new_profile.save_profile()
        self.new_image.save_image()
        self.new_image = Image(id=1,name='learn', caption='Learn 2017',image='media/gallery/dance-3134828_1920.jpg',category=self.new_category,location=self.new_location)
    
    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(name='learn')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.name,'learn')


    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('learn','Greener')
        fetched = Image.objects.get(image_name='Greener')
        self.assertEqual(fetched.image_name,'Greener')
        
    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

   