import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert_clients() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        rfc = formulario['RFC'] # almacena el rfc escrito en el input
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        telefono = formulario ['telefono'] # almacena el telefono escrito en el input
        email = formulario['correo'] # almacena el email escrito en el input
        direccion = formulario['direccion'] # almacena la direccion escrito en el input
        config.model_clientes.insert_cliente(rfc,nombre,telefono,email,direccion) # llama al metodo insert_cliente y le pasa los datos guardados 
        raise web.seeother('/index_clients') # redirecciona el HTML 
