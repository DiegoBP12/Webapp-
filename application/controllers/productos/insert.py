import web
import config as config

class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render.insert_product() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        codigo_barras = formulario['codigo_barras'] # almacena el codigo escrito en el input
        nombre_p = formulario['nombre_p'] # almacena el nombre escrito en el input
        marca = formulario['marca'] # almacena el email escrito en el input
        descripcion = formulario['descripcion'] # almacena la descripcion en el input
        tipo = formulario['tipo'] # almacena el tipo en el input
        config.model_productos.insert_producto(codigo_barras,nombre_p,marca,descripcion,tipo) # llama al metodo insert_datos y le paso los datos guardados 
        raise web.seeother('/index_product') # redirecciona el HTML 
