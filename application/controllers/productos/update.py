# -*- coding:utf-8 -*-
import web
import config as config

class Update:
    def __init__(self):
        pass

    def GET(self, codigo_barras):
        producto = config.model_productos.select_codigo(codigo_barras) # Selecciona el registro que coincida con el nombre
        return config.render.update_product(producto) # Envia el registro y renderiza update.html

    def POST(self,codigo_barras):
        formulario = web.input() # almacena los datos del formulario web
        codigo_barras = formulario['codigo_barras'] # almacena el codigo del input
        nombre_p = formulario['nombre_p'] # almacena el nombre del input 
        marca = formulario['marca'] # almacena la marca del input 
        descripcion = formulario['descripcion'] # almacena la descripcion del input
        tipo =  formulario['tipo'] # almacena el tipo del input
        config.model_productos.update_producto(codigo_barras,nombre_p,marca,descripcion,tipo) # actualiza los valores
        raise web.seeother('/index_product') # redirecciona al index

