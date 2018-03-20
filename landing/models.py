from django.db import models

# Create your models here.
class Subscriber (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)


    def __str__(self):
        return "id: %s name: %s" % (self.id, self.name,)
