from django.db import models

class User(models.Model):
    firstname = models.CharField("First Name", max_length=100)
    lastname = models.CharField("Last Name", max_length=100, null=True, blank=True)
    email = models.EmailField("Email", max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.firstname

    @models.permalink
    def get_absolute_url(self):
        return ('user-detail', [self.id])
