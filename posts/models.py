from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32,blank=False)
    catrgory = models.CharField(max_length=32, blank=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title