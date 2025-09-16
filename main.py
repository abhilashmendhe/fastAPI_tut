# Run -> $ uvicorn main:app --reload

from fastapi import FastAPI, Path, HTTPException
from utils import load_patients_data

app = FastAPI()

patients_data = {} # Cache

@app.get("/")
async def hello_world():
    return {"message":"Patient management system API"}

@app.get("/about")
async def about():
    return {"message":"Fully functional API to manage patients records"}

@app.get("/patients")
async def patients():
    global patients_data
    patients_data = await load_patients_data()
    return patients_data

@app.get("/patients/{patient_id}")
async def get_one_patient(patient_id:str = Path(..., description='ID of the patient in the DB', example='P001')):
    if patient_id in patients_data:
        return {'patient_id':patient_id,"patient_details":patients_data[patient_id]}
    
    raise HTTPException(status_code=404, detail="Patient not found")
