# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class Categoria(object):
    def __init__(self,nome="produto",imag="imagem",id=0):
        self.nome=nome
        self.imag=imag
        self.id=id

def index(write_tmpl):
    produto=["Coleira KRL","Coleira Cabresto","Coleira Asturias","Coleira Enforcador"]
    categorias=[Categoria(),Categoria("Coleira","coleira",1)]
    values={"Produtos":produto,"Categoria":categorias}
    write_tmpl("/templates/table.html",values)


