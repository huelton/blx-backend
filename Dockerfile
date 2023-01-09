FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

#docker build -t myimage .

#RUN CONTAINER
#docker run -d --name mycontainer -p 80:80 myimage