from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, session: Session):
        self.session =  session

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome, 
                                    detalhes=produto.detalhes, 
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    usuario_id = produto.usuario_id)
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)

        return db_produto

    def listar(self):
        #produtos = self.session.query(models.Produto).all()
        stmt = select(models.Produto)
        produtos = self.session.execute(stmt).scalars().all() 

        return produtos

    
    def buscarPorId(self, produto_id: int):
        #produtos = self.session.query(models.Produto).all()
        stmt = select(models.Produto).where(models.Produto.id == produto_id)
        produto = self.session.execute(stmt).scalars().first()

        return produto

    def editar(self, produto_id: int, produto: schemas.Produto):
        update_stmt = update(models.Produto).where(
            models.Produto.id == produto_id).values(nome=produto.nome, 
                                                        detalhes=produto.detalhes, 
                                                        preco=produto.preco,
                                                        disponivel=produto.disponivel)
        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, produto_id: int):
        delete_stmt = delete(models.Produto).where(models.Produto.id == produto_id)
        self.session.execute(delete_stmt)
        self.session.commit()