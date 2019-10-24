from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT

from core.models import UserRole


class Wall(models.Model):
    title = models.CharField('Title', max_length=200)
#    slug = models.SlugField(help_text='Undvik att ändra detta, eftersom det påverkar webbadressen', unique=True)
    description = models.TextField('Description', blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class WallRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wall = models.ForeignKey(Wall, on_delete=models.CASCADE, related_name='roles')
    roles = models.ManyToManyField(UserRole)


class Collection(models.Model):
    title = models.CharField('Title', max_length=200)
    wall = models.ForeignKey(Wall, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Card(models.Model):
    INDICATOR_CHOICES = (
        (-1, '- Off -'),
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    )
    title = models.CharField('Title', max_length=200)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    relations = models.ManyToManyField(
        RECURSIVE_RELATIONSHIP_CONSTANT, verbose_name='Relations',
        # related_name='xxx_%(app_label)s_%(class)s_set',
        blank=True)
    int_indicator = models.SmallIntegerField(default=-1, choices=INDICATOR_CHOICES)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
