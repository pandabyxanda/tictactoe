from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.


class Testing(models.Model):
    name = models.CharField(max_length=255, verbose_name='words yahho')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    # for admin panel (not only)
    # def __str__(self):
    #     return self.word
    #
    # def get_absolute_url(self):
    #     return reverse('words', kwargs=('word.id', self.pk))
    #
    # class Meta:
    #     verbose_name = 'words__'
    #     verbose_name_plural = 'words__'
    #     ordering = ['-pk', ]