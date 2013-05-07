# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Produto(ndb.Model):
    nome=ndb.StringProperty(required=True)
    sigla=ndb.StringProperty(required=True)
    ddd=ndb.IntegerProperty(required=True)
    preco=ndb.StringProperty(required=True)
    categ=ndb.StringProperty(required=True)


class Cidade(ndb.Model):
    nome=ndb.StringProperty(required=True)
    estado=ndb.KeyProperty(Produto,required=True)


