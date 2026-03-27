from fastapi import FastAPI, status, Response, HTTPException
from pydantic import BaseModel, Field
from typing import Union, List 
from uuid import uuid4

app = FastAPI()

class VechicleOut(BaseModel):
    id: Union[int, str] 
    name: str
    model: str
    year: int
    serial_number: str = Field(exclude=True)

class VechicleIn(BaseModel):
    name: str
    model: str
    year: int
    serial_number: str

vechicles: List[VechicleOut] = []


@app.get("/")
def home_screen():
    return {"message": "Hello, World!"}

@app.get("/api/vechicles", response_model=list[VechicleOut])
def all_vechicles(brand: str = 'BMW', model: str = ''):
    return vechicles

@app.get("/api/vechicles/{vechicle_id}", response_model=VechicleOut)
def find_vechicle_by_id(vechicle_id: Union[int, str], response: Response):
    for vechicle in vechicles:
        if vechicle.id == vechicle_id:
            return vechicle
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Vechicle with id {vechicle_id} not found"
    )

@app.post("/api/vechicles", status_code=status.HTTP_201_CREATED, response_model=VechicleOut)
def create_vechicle(vechicle: VechicleIn):
    new_vechicle = VechicleOut(
        id=str(uuid4()),
        name=vechicle.name,
        model=vechicle.model,
        year=vechicle.year,
        serial_number=vechicle.serial_number
    )
    
    vechicles.append(new_vechicle)
    return new_vechicle

@app.put("/api/vechicles/{vechicle_id}")
def update_vechicle(vechicle_id: int, req: VechicleIn):
    for vechile in vechicles:
        if vechicle.id == vechicle_id:
            update_data = vechicle.model_copy(update=vehicle.model_dump(exclude_unset=True))
            vehicles[vehicles.index(vehicle)] = update_data
        return update_data
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Vechicle with id {vechicle_id} not found"
    ) 