from django.db import models

# Create your models here.


class UserRole(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.CharField('Description', max_length=100)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
