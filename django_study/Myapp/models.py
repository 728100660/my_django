from django.db import models

# Create your models here.
class Animals(models.Model):
    a_name = models.CharField(max_length=6)
    is_delete = models.BooleanField(default=False)

class Animals_manager(models.Manager):
    def get_queryset(self):
        return super(Animals_manager,self).get_queryset().filter(is_delete)