from django.db import models


class Category(models.Model):
    cid = models.IntegerField(verbose_name='ID from Eventbrites', unique=True)
    name = models.CharField(max_length=128)
    name_localized = models.CharField(max_length=128)
    short_name = models.CharField(max_length=128)
    short_name_localized = models.CharField(max_length=128)
    uri = models.URLField()

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('cid',)

    def __str__(self):
        return self.name

