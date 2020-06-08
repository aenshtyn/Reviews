from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Project (models.Model):
    name = models.CharField(max_length =30)
    languages = models.ManyToManyField(languages)
    author = models.ForeignKey(Author)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class languages(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name