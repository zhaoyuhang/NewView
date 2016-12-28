from django.db import models
from django.contrib.auth.models import User
from Account.models import Interviewee, Interviewer


class Room(models.Model):
    # url = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=200, default="Default room title")
    description = models.CharField(max_length=1000, default="Default description for a default room")
    state = models.BooleanField(default=False)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    interviewer = models.OneToOneField(Interviewer, default=Interviewer())
    interviewees = models.ManyToManyField(Interviewee)

    def __str__(self):
        return self.title
