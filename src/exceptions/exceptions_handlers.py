import pytz
import datetime

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from src.exceptions.exceptions import ResourceNotFoundException, TooPerfectException

data_hora = datetime.datetime.now()
time_utc = pytz.timezone('America/Sao_Paulo').localize(data_hora)

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer akljnv13bvi2vfo0b0bw'
}

def resource_exception_handler(request: Request, exc: ResourceNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        headers= headers,
        content={
            "timeStamp": f"{data_hora}",
            "status": status.HTTP_404_NOT_FOUND,            
            "error": f"{exc.name} Exception",
            "message": f"{exc.name} ID : {exc.id} nao encontrado"
            })

def too_perfect_exception_handler(request: Request, exc: TooPerfectException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        headers= headers,
        content={
            "timeStamp": f"{data_hora}",
            "status": status.HTTP_404_NOT_FOUND,            
            "error": f"{exc.name} Exception",
            "message": f"{exc.name} ID : {exc.id} nao encontrado"
            })

def include_exception_handlers(app):
	app.add_exception_handler(ResourceNotFoundException, resource_exception_handler)
	app.add_exception_handler(TooPerfectException, too_perfect_exception_handler)

