FROM python:3.10.9-slim


WORKDIR /streamlit


COPY req.txt /streamlit/


RUN pip install --no-cache-dir -r req.txt

EXPOSE 8501

COPY . /streamlit/

ENTRYPOINT ["streamlit", "run"]


CMD ["streamlit.py"]


# http://localhost:8501/





## FROM python:3.10.9-slim

# Definir un repertoire de travail dans mon conteneur

## WORKDIR /app

# Copie le fichier requirements.txt dans le conteneur

## COPY requirements.txt /app

# Install les dépendances

## RUN pip install --no-cache-dir -r requirements.txt


# Copie le contenu du repertoire courant dans le conteneur

## COPY . /app

## EXPOSE 8000 

# Commande pour executer l'application fastapi

## CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000","--reload"] 


