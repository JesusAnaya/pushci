from django.db import models
from django.conf import settings


class Github(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    account_id = models.IntegerField()
    email = models.EmailField()
    access_token = models.CharField(max_length=255)
    avatar_url = models.URLField()

    def __unicode__(self):
        return u'{0} - {1}'.format(self.user, self.user_name)
