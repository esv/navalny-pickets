# coding: utf-8

# python manage.py schemamigration picket --initial

"""
python manage.py schemamigration picket --auto
python manage.py migrate picket
"""

from django.db import models
from django.contrib.auth.models import User

class Organizer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.phone)


class Picket(models.Model):
    begin_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True, null=True)

    title = models.CharField(max_length=100)

    place_readable = models.TextField(blank=True, null=True)
    place_latlong = models.CharField(max_length=100)

    status = models.IntegerField(blank=True, null=True, choices=((0, u'Запланирован'),(1, u'Проведен'),(2, u'Согласован'),))

    organizer = models.ForeignKey(Organizer)
    created_at = models.DateTimeField(auto_now_add=True)

    participants = models.ManyToManyField(User)

    def __unicode__(self):
        return '%s' % (self.title,)

    def is_participant(self, user):
        return user in self.participants
