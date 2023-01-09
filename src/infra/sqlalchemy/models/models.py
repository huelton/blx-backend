from sqlalchemy import Column, Table, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))    
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    #Bidirecional
    usuario = relationship('Usuario', back_populates='produtos')
    pedido = relationship('Pedido', back_populates='produto')

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    telefone = Column(String)
    #Bidirecional
    produtos = relationship('Produto', back_populates='usuario')
    pedido = relationship('Pedido', back_populates='usuario')

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True, index=True)
    quantidade =  Column(Integer)
    entrega = Column(Boolean)
    endereco = Column(String)
    observacoes = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario_pedido'))
    produto_id = Column(Integer, ForeignKey('produto.id', name='fk_produto_pedido'))  

    # previously one-to-many Parent.children is now
    # one-to-one Parent.child
    usuario = relationship("Usuario", back_populates="pedido", uselist=False)

    # previously one-to-many Parent.children is now
    # one-to-one Parent.child
    produto = relationship("Produto", back_populates="pedido", uselist=True)
