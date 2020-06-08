from django.db import models

# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length =30)
    languages = models.CharField(max_length =30)
    author = models.CharField(max_length =30)
    pub_date = models.CharField(max_length =30)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class languages(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name