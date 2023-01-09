from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPedido():

    def __init__(self, session: Session):
        self.session =  session


    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(quantidade=pedido.quantidade, 
                                    entrega=pedido.entrega,
                                    endereco=pedido.endereco,
                                    observacoes=pedido.observacoes,
                                    usuario_id=pedido.usuario_id,
                                    produto_id=pedido.produto_id)
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)

        return db_pedido


    def listar(self):
        stmt = select(models.Pedido)
        pedidos = self.session.execute(stmt).scalars().all() 

        return pedidos


    def buscarPorId(self, pedido_id: int):
        #produtos = self.session.query(models.Produto).all()
        stmt = select(models.Pedido).where(models.Pedido.id == pedido_id)
        pedido = self.session.execute(stmt).scalars().first()

        return pedido

    def editar(self, pedido_id: int, pedido: schemas.Pedido):
        update_stmt = update(models.Pedido).where(
            models.Pedido.id == pedido_id).values(quantidade=pedido.quantidade, 
                                                    entrega=pedido.entrega,
                                                    endereco=pedido.endereco,
                                                    observacoes=pedido.observacoes,
                                                    usuario_id=pedido.usuario_id,
                                                    produto_id=pedido.produto_id)
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, pedido_id: int):
        delete_stmt = delete(models.Pedido).where(models.Pedido.id == pedido_id)
        self.session.execute(delete_stmt)
        self.session.commit()