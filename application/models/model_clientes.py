import config as config # importa el archivo config

db = config.db # crea un objeto del objeto db creado en config 

'''
Metodo para seleccionar todos los registros de la tabla clientes
'''
def select_clientes():
    try:
        return db.select('clientes') # selecciona todos los registros de la tabla de clientes
    except Exception as e:
        print "Model select_clientes Error ()",format(e.args)
        print "Model select_clientes Message {}",format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el nombre dado
'''
def select_rfc(rfc):
    try:
        return db.select('clientes', where= 'rfc = $rfc', vars=locals())[0] #selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_rfc Error ()",format(e.args)
        print "Model select_rfc Message {}",format(e.message)
        return None

'''
Metodo para insertar un nuevo registro 
'''
def insert_cliente(rfc,nombre,telefono,correo,direccion):
    try:
        return db.insert('clientes',rfc=rfc,nombre=nombre,telefono=telefono,correo=correo,direccion=direccion) # inserta un registro en clientes
    except Exception as e:
        print "Model insert_cliente Error ()",format(e.args)
        print "Model insert_cliente Message {}",format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el rfc recibido
'''
def delete_cliente(rfc):
    try:
        return db.delete('clientes', where='rfc=$rfc', vars=locals()) # borra un registro de personas
    except Exception as e:
        print "Model delete_cliente Error ()",format(e.args)
        print "Model delete_cliente Message {}",format(e.message)
        return None

'''
Metodo para actualizar el email, del nombre recibido
'''
def update_cliente(rfc,nombre,telefono,correo,direccion): # actualiza el registro
    try:
            return db.update('clientes',
            nombre=nombre,
            telefono=telefono,
            correo=correo,
            direccion=direccion,
            where='rfc=$rfc',
            vars=locals())
    except Exception as e:
        print "Model update_cliente Error ()",format(e.args)
        print "Model update_cliente Message {}",format(e.message)
        return None

