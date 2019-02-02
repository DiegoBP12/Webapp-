# -*- coding:utf-8 -*-
import web
import config as config

class View():
    def __init__(self):
        pass
    
    def GET(self,rfc):
        cliente = config.model_clientes.select_rfc(rfc) # Selecciona el registro que coincida con el nombre
        return config.render.view_clients(cliente) # Envia el registro y renderiza el view.html
        