from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class Words(BaseModel):
    id:str
    title: str
    description:str
    words: []
    
games = []

@app.post("/createGame")
def create_game(words:Words):
    games.appen(words)

app.mount("/", StaticFiles(directory='static', html=True), name='static')