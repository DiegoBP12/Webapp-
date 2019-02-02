# -*- coding:utf-8 -*-
import web
import config as config

class Update:
    def __init__(self):
        pass

    def GET(self, rfc):
        cliente = config.model_clientes.select_rfc(rfc) # Selecciona el registro que coincida con el rfc
        return config.render.update_clients(cliente) # Envia el registro y renderiza update.html

    def POST(self,rfc):
        formulario = web.input() # almacena los datos del formulario web
        rfc = formulario['rfc'] # almacena el rfc del input 
        nombre = formulario['nombre'] # almacena el nombre del input email
        telefono = formulario['telefono'] # almacena el telefono del input 
        email = formulario['correo'] # almacena el email del input 
        direccion = formulario['direccion'] # almacena la direccion del input email
        config.model_clientes.update_cliente(rfc,nombre,telefono,email,direccion) # actualiza los valores
        raise web.seeother('/index_clients') # redirecciona al index

