# -*- coding: utf-8 -*-

from django.db import models

class JCPerson(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=31, null=False)


class JCBook(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=127, null=False)
    owner = models.ForeignKey(JCPerson, related_name='使用人')

