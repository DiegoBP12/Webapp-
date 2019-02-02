import web

urls=('/home', 'application.controllers.principal.home.Home',
    '/index_clients','application.controllers.clientes.index.Index',
    '/insert_clients', 'application.controllers.clientes.insert.Insert',
    '/update_clients/(.*)', 'application.controllers.clientes.update.Update',
    '/delete_clients/(.*)', 'application.controllers.clientes.delete.Delete',
    '/view_clients/(.*)', 'application.controllers.clientes.view.View',
    '/index_product','application.controllers.productos.index.Index',
    '/insert_product', 'application.controllers.productos.insert.Insert',
    '/update_product/(.*)', 'application.controllers.productos.update.Update',
    '/delete_product/(.*)', 'application.controllers.productos.delete.Delete',
    '/view_product/(.*)', 'application.controllers.productos.view.View',)#(url , ubicacion del archivo)

render = web.template.render('application/views/clientes/', base = 'master2')

if __name__ == "__main__": #metodo principal, doble guion = private
    app = web.application(urls, globals())
    web.config.debug = False # Hide debug print
    def NotFound():
        return web.notfound(render.notfound())
    app.notfound = NotFound
    def internalerror():
        return web.internalerror(render.internal())
    app.internalerror = internalerror
    app.run()
