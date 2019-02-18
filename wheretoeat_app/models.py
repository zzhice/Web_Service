from django.db import models

# Create your models here.
class basicModel(models.Model):
    name = models.CharField(max_length=50)
    code = models.TextField()

    def __str__(self):
        return '{},{}'.format(self.name, self.code)