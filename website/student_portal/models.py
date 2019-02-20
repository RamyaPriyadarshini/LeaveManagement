from django.db import models
from django.urls import reverse
# Create your models here.


class Personal(models.Model):
    """docstring for Personal"""
    name = models.CharField(max_length=250)
    dept = models.CharField(max_length=25)
    regno = models.BigIntegerField(primary_key=True)
    # def __init__(self, arg):
    #     super(Personal, self).__init__()
    #     self.arg = arg

    def __str__(self):
        return self.name + ' - ' + self.dept + ' - ' + str(self.regno)

    def get_absolute_url(self):
        return reverse('views.DetailView.as_view()', kwargs={'stud': self.pk})
