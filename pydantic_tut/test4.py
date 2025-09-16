from pydantic import BaseModel,EmailStr,computed_field
from typing import List, Dict

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float 
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
  
    @computed_field
    @property
    def bmi(self)->float:
        bmi = round((self.weight/self.height**2),2)
        return bmi
patient_info = {
    'name':'abhi', 
    'email': 'abhi@icici.com',
    'age':'310', 
    'weight': 72.12,
    'height': 1.6, 
    'married': True, 
    'allergies':['pollen','dust'],
    'contact_details':{'email':'abhi@gmail.com','phone':'99999999','emergency':'123123123123'}
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    
    print(patient)
    
insert_patient_data(patient1)