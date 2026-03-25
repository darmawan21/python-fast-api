from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_screen():
    return {"message": "Hello, World!"}