from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

router = APIRouter()

#Separando as responsalibidades nesse caso um rota para usuario

                        #status correto do retorno             #schema que sera retornado
@router.post('/signup', status_code = status.HTTP_201_CREATED, response_model=Usuario)#Depends - injecao de get_db na funcao
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    # Nesta linha nosso repositorio encaminha o schema a persistencia de usuario para salvar no BD
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado

                       #status correto do retorno
@router.put('/usuarios/{usuario_id}', status_code = status.HTTP_204_NO_CONTENT)#Depends - injecao de get_db na funcao
def editar_usuario(usuario_id: int, usuario: Usuario, session: Session = Depends(get_db)):
    # Nesta linha nosso repositorio encaminha o schema a persistencia de produto para salvar no BD
    RepositorioUsuario(session).editar(usuario_id, usuario)
    #return {'messagem': 'Produto Atualizado com sucesso'}

                       #status correto do retorno        #schema que sera retornado
@router.get('/usuarios', status_code = status.HTTP_200_OK, response_model=List[Usuario])#Depends - injecao de get_db na funcao
def listar_usuarios(session: Session = Depends(get_db)):
    # Nesta linha nosso repositorio encaminha retorna os usuarios salvos no BD
    usuarios = RepositorioUsuario(session).listar()
    return usuarios

                                   #status correto do retorno        #schema que sera retornado
@router.get('/usuarios/{usuario_id}', status_code = status.HTTP_200_OK, response_model=Usuario)#Depends - injecao de get_db na funcao
def exibir_usuarios(usuario_id: int, session: Session = Depends(get_db)):
    # Nesta linha nosso repositorio encaminha retorna os usuarios salvos no BD
    usuario = RepositorioUsuario(session).buscarPorId(usuario_id)
    if usuario != None:
        return usuario
    else:
        return {'mensagem': 'Usuario nao encontrado'}

@router.delete('/usuarios/{usuario_id}', status_code = status.HTTP_204_NO_CONTENT)#Depends - injecao de get_db na funcao
def remover_usuario(usuario_id: int, session: Session = Depends(get_db)):
    # Nesta linha nosso repositorio encaminha o schema a persistencia de produto para salvar no BD
    RepositorioUsuario(session).remover(usuario_id)
    #return {'messagem': 'Produto Deletado com sucesso'}