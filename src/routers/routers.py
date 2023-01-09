from src.routers import rotas_produtos, rotas_usuarios, rotas_pedidos

def include_routers(app):
    #INCLUINDO ROTAS_PRODUTOS
    app.include_router(rotas_produtos.router)
    #INCLUINDO ROTAS_USUARIOS
    app.include_router(rotas_usuarios.router)
    #INCLUINDO ROTAS_PEDIDO
    app.include_router(rotas_pedidos.router)




