from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=40)

    mark = models.CharField(max_length=3)

    def __str__(self):
        return '{} {}'.format(self.name,self.mark)
