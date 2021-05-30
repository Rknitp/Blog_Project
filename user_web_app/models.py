from django.db import models #by defaault given
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model): #76
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='django_profile_pic')

    def __str__(self): #79
        return f'{self.user.username}Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) #-->saving the old instance image

        img=Image.open(self.image.path)#-->assigning the old image to new variable

        if img.height>300 or img.width>300: #-->fixing the dimension of image
            output_size=(300,300)#max size
            img.thumbnail(output_size) #resizing the image
            img.save(self.image.path)#saving the image
