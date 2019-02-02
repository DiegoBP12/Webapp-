# -*- coding:utf-8 -*-
import web
import application.models.model_clientes as model_clientes # importa el model de personas
render = web.template.render('application/views/clientes/', base='master') # configura la ubicación de las vistas