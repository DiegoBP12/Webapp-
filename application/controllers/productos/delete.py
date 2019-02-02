# -*- coding:utf-8 -*-
import web
import config as config

class Delete():
    def __init__(self):
        pass

    def GET(self, codigo_barras):
        productos = config.model_productos.select_codigo(codigo_barras) # Selecciona el registro que coincida con codigo
        return config.render.delete_product(productos) # Envia el registro y renderiza delete.html

    def POST(self, codigo_barras):
        formulario = web.input() # Crea objeto formulario con los datos enviados con el formulario
        codigo_barras = formulario['codigo_barras'] # Obtiene el nombre almacenado en el formulario
        config.model_productos.delete_producto(codigo_barras) # Borra el registro del codigo seleccionado
        raise web.seeother('/index_product') # redirecciona raíz