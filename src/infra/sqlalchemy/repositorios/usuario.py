from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():

    def __init__(self, session: Session):
        self.session =  session

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome=usuario.nome, 
                                    senha=usuario.senha,
                                    telefone=usuario.telefone)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)

        return db_usuario

    def listar(self):
        stmt =  select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all() # retornar uma lista correta

        return usuarios

    def buscarPorId(self, usuario_id: int):
        stmt =  select(models.Usuario).where(models.Usuario.id == usuario_id)
        usuario = self.session.execute(stmt).scalars().first()
        return usuario

    def editar(self, usuario_id: int, usuario: schemas.Usuario):
        update_stmt = update(models.Usuario).where(
            models.Usuario.id == usuario_id).values(nome=usuario.nome, 
                                                    senha=usuario.senha,
                                                    telefone=usuario.telefone)
        self.session.execute(update_stmt)
        self.session.commit()  

    def remover(self, usuario_id: int):
        delete_stmt = delete(models.Usuario).where(models.Usuario.id == usuario_id)
        self.session.execute(delete_stmt)
        self.session.commit()
