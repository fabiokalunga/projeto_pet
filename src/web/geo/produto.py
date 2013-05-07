# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from core.geo.model import Produto
from zen import router


def form(write_tmpl):
    values={"save_url":router.to_path(salvar)}
    write_tmpl("/geo/templates/form.html",values)


def salvar(handler,nome, sigla, categ, preco,ddd,id=None):
    ddd=long(ddd)

    if id:
        estado=Produto(id=long(id),nome=nome,sigla=sigla, categ=categ,preco=preco,ddd=ddd)
    else:
        estado=Produto(nome=nome,sigla=sigla,preco=preco, categ=categ, ddd=ddd)
    estado.put()
    handler.redirect(router.to_path(listar))

def listar(write_tmpl):
    query=Produto.query(Produto.ddd>0).order(Produto.ddd)
    # query=query.filter(Produto.ddd>0)
    # query=query.order(Produto.ddd)
    estados=query.fetch(100)
    values={"estados":estados,
            "apagar_url":router.to_path(apagar),
            "editar_url":router.to_path(editar)}
    write_tmpl("/geo/templates/produto_list.html",values)

def apagar(handler,id):
    key=ndb.Key(Produto,long(id))
    key.delete()

def editar(write_tmpl,urlsafe):
    key=ndb.Key(urlsafe=urlsafe)
    estado=key.get()
    values={"save_url":router.to_path(salvar),
            "estado":estado}
    write_tmpl("/geo/templates/form.html",values)
