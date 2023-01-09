from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido, PedidoResponse
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.exceptions.exceptions import ResourceNotFoundException, TooPerfectException

router = APIRouter()

#Separando as responsalibidades nesse caso um rota para pedido

                       #status correto do retorno             #schema que sera retornado
@router.post('/pedidos', status_code = status.HTTP_201_CREATED, response_model=Pedido)#Depends - injecao de get_db na funcao
def criar_pedido(pedido: Pedido, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do Produto para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    produto_localizado = RepositorioProduto(session).buscarPorId(pedido.produto_id)
    if not produto_localizado:
        raise ResourceNotFoundException("Produto", pedido.produto_id)

    # Faz uma busca pelo Id do Usuario para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    usuario_localizado = RepositorioUsuario(session).buscarPorId(pedido.usuario_id)
    if not usuario_localizado:
        raise ResourceNotFoundException("Usuario", pedido.usuario_id)    
    
    # Nesta linha nosso repositorio encaminha o schema a persistencia de pedido para salvar no BD
    pedido_criado = RepositorioPedido(session).criar(pedido)
    return pedido_criado
 
                      #status correto do retorno        #schema que sera retornado
@router.get('/pedidos', status_code = status.HTTP_200_OK, response_model=List[PedidoResponse])#Depends - injecao de get_db na funcao
def listar_pedidos(session: Session = Depends(get_db)):
    # Nesta linha nosso repositorio encaminha retorna os pedidos salvos no BD
    pedidos = RepositorioPedido(session).listar()
    return pedidos

@router.get('/pedidos/{pedido_id}', status_code = status.HTTP_200_OK, response_model=PedidoResponse)#Depends - injecao de get_db na funcao
def exibir_pedido(pedido_id: int, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do pedido para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    pedido_localizado = RepositorioPedido(session).buscarPorId(pedido_id)
    if not pedido_localizado:
        raise ResourceNotFoundException("Pedido", pedido_id)
    return pedido_localizado

                       #status correto do retorno              #schema que sera retornado
@router.put('/pedidos/{pedido_id}', status_code = status.HTTP_204_NO_CONTENT)#Depends - injecao de get_db na funcao
def editar_produto(pedido_id: int, pedido: Pedido, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do Produto para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    produto_localizado = RepositorioProduto(session).buscarPorId(pedido.produto_id)
    if not produto_localizado:
        raise ResourceNotFoundException("Produto", pedido.produto_id)

    # Faz uma busca pelo Id do Usuario para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    usuario_localizado = RepositorioUsuario(session).buscarPorId(pedido.usuario_id)
    if not usuario_localizado:
        raise ResourceNotFoundException("Usuario", pedido.usuario_id)  
    
    # Faz uma busca pelo Id do produto para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    pedido_localizado = RepositorioPedido(session).buscarPorId(pedido_id)
    if not pedido_localizado:
        raise ResourceNotFoundException("Pedido", pedido_id)
    # Nesta linha nosso repositorio encaminha o schema a persistencia de produto para Atualizar no BD
    RepositorioPedido(session).editar(pedido_id, pedido)
    #return {'messagem': 'Produto Atualizado com sucesso'}

@router.delete('/pedidos/{pedido_id}', status_code = status.HTTP_204_NO_CONTENT)#Depends - injecao de get_db na funcao
def remover_produto(pedido_id: int, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do Pedido para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    pedido_localizado = RepositorioPedido(session).buscarPorId(pedido_id)
    if not pedido_localizado:
        raise ResourceNotFoundException("Pedido", pedido_id)
    # Nesta linha nosso repositorio encaminha o schema a persistencia de produto para deletar no BD
    RepositorioPedido(session).remover(pedido_id)
    #return {'messagem': 'Produto Deletado com sucesso'}