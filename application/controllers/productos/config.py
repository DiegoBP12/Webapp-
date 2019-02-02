# -*- coding:utf-8 -*-
import web
import application.models.model_productos as model_productos # importa el model de personas
render = web.template.render('application/views/productos/', base='master') # configura la ubicación de las vistas