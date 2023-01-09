from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.exceptions import exceptions_handlers
from src.routers import routers


#criar_bd() # funcao para conexar ao banco de dados
app = FastAPI()

#URLS LIBERADAS PELO CORS para acesssar a API, devem estar dentro dessa lista
origins = ['http://127.0.0.1:5500'
          ]

#Codigo para liberacao das URLs
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# INCLUINDO TODAS AS ROTAS
routers.include_routers(app)

# INCLUINDO TODOS OS EXCEPTION HANDLERS
exceptions_handlers.include_exception_handlers(app)


