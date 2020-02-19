from django.db import models

# Create your models here.
class Worksite(models.Model):
    name = models.CharField(max_length = 256)
    supervisor = models.CharField(max_length = 256)
    location = models.CharField(max_length = 256)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Employee(models.Model):
    name = models.CharField(max_length = 256)
    age = models.PositiveIntegerField()
    worksite = models.ForeignKey(Worksite , related_name = 'employees',  on_delete=models.CASCADE,)
    def __str__(self):
        return self.name
