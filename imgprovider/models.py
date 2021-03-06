from django.db import models
from django.conf import settings
from django.utils import timezone

class ImgPost(models.Model): 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    rating = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True)

    def publish(self):
            self.published_date = timezone.now()
            self.save()

    def __str__(self):
        return self.title