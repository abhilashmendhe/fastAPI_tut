# Run -> $ uvicorn main:app --reload

from fastapi import FastAPI 
from load_patients_data import load_patients_data

app = FastAPI()

patients_data = {} # Cache

@app.get("/")
async def hello_world():
    return {"message":"Patient management system API"}

@app.get("/about")
async def about():
    return {"message":"Fully functional API to manage patients records"}

@app.get("/view")
async def view():
    global patients_data
    patients_data = await load_patients_data()
    return patients_data