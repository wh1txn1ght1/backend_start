"print('Backend start initialized')" 
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message": "Backend initialized successfully"}