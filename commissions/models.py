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
    date_mod = models.DateTimeField('last modified')
    date_accepted = models.DateTimeField(null=True)
    user = models.EmailField(max_length=254,null=True) #TODO, remove null and make implementation
    user_id = models.PositiveSmallIntegerField(null=True) #TODO, remove null and make implementation
    complete = models.BooleanField(default=False)

    contact = models.CharField(max_length=200, null=True)
    file = models.FileField(upload_to='user/uploads/', null=True) #TODO
    charnotes = models.CharField(max_length=2000, null=True)
    comments = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return str(self.user) + '-' + str(self.user_id)