# -*- coding:utf-8 -*-
import web
import config as config

class View():
    def __init__(self):
        pass
    
    def GET(self,codigo_barras):
        producto = config.model_productos.select_codigo(codigo_barras) # Selecciona el registro que coincida con el codigo
        return config.render.view_product(producto) # Envia el registro y renderiza el view.html
        