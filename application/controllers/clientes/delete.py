# -*- coding:utf-8 -*-
import web
import config as config

class Delete():
    def __init__(self):
        pass

    def GET(self, rfc):
        clientes = config.model_clientes.select_rfc(rfc) # Selecciona el registro que coincida con nombre
        return config.render.delete_clients(clientes) # Envia el registro y renderiza delete.html

    def POST(self, rfc):
        formulario = web.input() # Crea objeto formulario con los datos enviados con el formulario
        rfc = formulario['rfc'] # Obtiene el rfc almacenado en el formulario
        config.model_clientes.delete_cliente(rfc) # Borra el registro del nombre seleccionado
        raise web.seeother('/index_clients') # redirecciona raíz