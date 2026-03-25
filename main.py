from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, List 

app = FastAPI()

class Vechicle(BaseModel):
    id: Union[int, str] 
    name: str
    model: str
    year: int

@app.get("/")
def home_screen():
    return {"message": "Hello, World!"}

@app.get("/api/vechicles", response_model=list[Vechicle])
def all_vechicles(brand: str, model: str):
    return [Vechicle(id=1, name="Car A", model=model, year=2020), Vechicle(id=2, name="Car B", model=model, year=2021)]

@app.get("/api/vechicles/{vechicle_id}")
def find_vechicle_by_id(vechicle_id: Union[int, str]):
    return {"vechicle_id": vechicle_id}

@app.post("/api/vechicles")
def create_vechicle(vechicle: Vechicle):
    return vechicle