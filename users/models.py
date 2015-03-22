from django.db import models

class User(models.Model):
    firstname = models.CharField("First Name", max_length=30)
    lastname = models.CharField("Last Name", max_length=30, null=True, blank=True)
    email = models.EmailField("Email", max_length=60, null=True, blank=True)

    def __unicode__(self):
        return self.firstname

    @models.permalink
    def get_absolute_url(self):
        return ('user-detail', [self.id])


class AboutText(models.Model):
    display_order = models.IntegerField()
    title = models.CharField(max_length=80)
    content = models.TextField()

    def __unicode__(self):
        return str(self.display_order) + ": " + self.title

