from django.db import models

# Create your models here.


class Contact(models.Model):
    name  = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=250, null=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.email} - {self.subject}" 
    



class Post(models.Model):
    likes = models.IntegerField(default=116)

