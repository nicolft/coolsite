from django.db import models

# Create your models here.

class CommType(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=220)
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id) + '-' + self.name
#     examples =


class CommReq(models.Model):
    commType = models.ForeignKey(CommType, on_delete=models.SET_NULL, null=True)
    date_init = models.DateTimeField(auto_now=True)
    date_mod = models.DateTimeField('last modified', auto_now_add=True)
    date_accepted = models.DateTimeField()
    user = models.EmailField(max_length=254)
    user_id = models.PositiveSmallIntegerField()
    complete = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user) + '-' + str(self.user_id)