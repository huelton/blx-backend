from pydantic import BaseModel
from typing import Optional, List


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    produtos: List[ProdutoSimples] = []

    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool =  False
    usuario_id: Optional[int]

    class Config:
        orm_mode = True

class ProdutoResponse(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool =  False
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observacoes'
    usuario_id: Optional[int]
    produto_id: Optional[int]

    class Config:
        orm_mode = True


class PedidoResponse(BaseModel):
    id: Optional[int] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observacoes'
    usuario: Optional[UsuarioSimples]
    produto: List[ProdutoSimples] = []

    class Config:
        orm_mode = True
