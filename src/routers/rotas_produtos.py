from fastapi import APIRouter, Depends, status, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoResponse, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.exceptions.exceptions import ResourceNotFoundException, TooPerfectException

router = APIRouter()

#Separando as responsalibidades nesse caso um rota para produtos

                       #status correto do retorno              #schema que sera retornado
@router.post('/produtos', status_code = status.HTTP_201_CREATED, response_model=ProdutoSimples)#Depends - injecao de get_db na funcao
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do usuario para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    usuario_localizado = RepositorioUsuario(session).buscarPorId(produto.usuario_id)
    if not usuario_localizado:
        raise ResourceNotFoundException("Usuario", produto.usuario_id)
    # Nesta linha nosso repositorio encaminha o schema a persistencia de produto para salvar no BD
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

                       #status correto do retorno              #schema que sera retornado
@router.put('/produtos/{produto_id}', status_code = status.HTTP_204_NO_CONTENT)#Depends - injecao de get_db na funcao
def editar_produto(produto_id: int, produto: Produto, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do produto para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    produto_localizado = RepositorioProduto(session).buscarPorId(produto_id)
    if not produto_localizado:
        raise ResourceNotFoundException("Produto", produto_id)
    # Nesta linha nosso repositorio encaminha o schema a persistencia de produto para Atualizar no BD
    RepositorioProduto(session).editar(produto_id, produto)
    #return {'messagem': 'Produto Atualizado com sucesso'}

                    #status correto do retorno            #schema que sera retornado
@router.get('/produtos', status_code = status.HTTP_200_OK, response_model=List[ProdutoResponse])#Depends - injecao de get_db na funcao
def listar_produtos(session: Session = Depends(get_db)):
    # Nesta linha nosso repositorio encaminha retorna os produtos salvos no BD
    produtos = RepositorioProduto(session).listar()
    return produtos

@router.get('/produtos/{produto_id}', status_code = status.HTTP_200_OK, response_model=ProdutoResponse)#Depends - injecao de get_db na funcao
def exibir_produto(produto_id: int, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do produto para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    produto_localizado = RepositorioProduto(session).buscarPorId(produto_id)
    if not produto_localizado:
        raise ResourceNotFoundException("Produto", produto_id)
    return produto_localizado
                                      #status correto do retorno 
@router.delete('/produtos/{produto_id}', status_code = status.HTTP_204_NO_CONTENT)#Depends - injecao de get_db na funcao
def remover_produto(produto_id: int, session: Session = Depends(get_db)):
    # Faz uma busca pelo Id do produto para verificar se ele existe.
    # Caso nao encontrado gera uma Exception
    produto_localizado = RepositorioProduto(session).buscarPorId(produto_id)
    if not produto_localizado:
        raise ResourceNotFoundException("Produto", produto_id)
    # Nesta linha nosso repositorio encaminha o schema a persistencia de produto para deletar no BD
    RepositorioProduto(session).remover(produto_id)
    #return {'messagem': 'Produto Deletado com sucesso'}
