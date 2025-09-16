from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List, Dict, Optional

class PatientContactDetails(BaseModel):
    email: EmailStr 
    phone: int
    
class Patient(BaseModel):
    
    name: str 
    age: int 
    weight: float
    married: bool = False
    linkedin: AnyUrl
    allergies: Optional[List[str]]= None
    # contact_details: Dict[str,str]
    contact_details: PatientContactDetails
    
    
patient_contacts = {
    'email': 'abhi@gmail.com',
    'phone': 9999999990
}
patient_info = {
    'name':'abhi', 
    'age':31, 
    'weight': 72.12, 
    'married': True, 
    'linkedin':"http://linkedin.com/adf123asd",
    'allergies':['pollen','dust'],
    # 'contact_details':{'email':'abhi@gmail.com','phone':'99999999'}
    'contact_details': patient_contacts
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    
    print(patient)
    
insert_patient_data(patient1)