from django.db import models

class Team(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    designation = models.CharField(max_length=32)
    facebook_url = models.URLField(max_length=255)
    Instagram_url = models.URLField(max_length=255)
    linkedin_url  = models.URLField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = self.first_name +" " +self.last_name
        return name