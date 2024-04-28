from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Welcome to Sandy Frank's API, je vais construire ma propre appli maintenant"}


@app.get("/data/")

def data():
    return {"Les données": "Sont ceux des proteines de la base de données NCBI"}

@app.post("/prediction/")



# python -m pip freeze > requirement.txt

#  uvicorn main:app --reload

# docker build -t testfastapi .   # sans fichier docker-compose.yaml pour les interaction dynamique

# docker run -p 8000:8000 testfastapi

# docker-compose up --build       #  Ceci quand tu as le docker-compose.yaml

# docker images

# pip freeze > requirements.txt