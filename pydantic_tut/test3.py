from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details: 
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model
    
patient_info = {
    'name':'abhi', 
    'email': 'abhi@icici.com',
    'age':'310', 
    'weight': 72.12, 
    'married': True, 
    'allergies':['pollen','dust'],
    'contact_details':{'email':'abhi@gmail.com','phone':'99999999','emergency':'123123123123'}
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    
    print(patient)
    
insert_patient_data(patient1)