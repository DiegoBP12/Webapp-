import config as config # importa el archivo config

db = config.db # crea un objeto del objeto db creado en config 

'''
Metodo para seleccionar todos los registros de la tabla productos
'''
def select_producto():
    try:
        return db.select('productos') # selecciona todos los registros de la tabla de productos
    except Exception as e:
        print "Model select_productos Error ()",format(e.args)
        print "Model select_productos Message {}",format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el codigo dado
'''
def select_codigo(codigo_barras):
    try:
        return db.select('productos', where= 'codigo_barras=$codigo_barras', vars=locals())[0] #selecciona el primer registro que coincida con el codigo
    except Exception as e:
        print "Model select_codigo Error ()",format(e.args)
        print "Model select_codigo Message {}",format(e.message)
        return None

'''
Metodo para insertar un nuevo registro 
'''
def insert_producto(codigo_barras,nombre_p,marca,descripcion,tipo):
    try:
        return db.insert('productos',codigo_barras=codigo_barras,nombre_p=nombre_p,marca=marca,descripcion=descripcion,tipo=tipo) # inserta un registro en productos
    except Exception as e:
        print "Model insert_producto Error ()",format(e.args)
        print "Model insert_producto Message {}",format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el codigo recibido
'''
def delete_producto(codigo_barras):
    try:
        return db.delete('productos', where= 'codigo_barras=$codigo_barras', vars=locals()) # borra un registro de productos
    except Exception as e:
        print "Model delete_producto Error ()",format(e.args)
        print "Model delete_producto Message {}",format(e.message)
        return None

'''
Metodo para actualizar 
'''
def update_producto(codigo_barras,nombre_p,marca,descripcion,tipo): # actualiza el registro del producto
    try:
            return db.update('productos',
            nombre_p=nombre_p,
            marca=marca,
            descripcion=descripcion,
            tipo=tipo,
            where= 'codigo_barras = $codigo_barras',
            vars=locals())
    except Exception as e:
        print "Model update_producto Error ()",format(e.args)
        print "Model update_producto Message {}",format(e.message)
        return None

