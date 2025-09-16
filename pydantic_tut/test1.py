from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List, Dict, Optional, Annotated

class PatientContactDetails(BaseModel):
    email: EmailStr 
    phone: int
    
class Patient(BaseModel):
    
    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give name of the patient in less than 50 characters", examples=['Abhilash', 'Nitish'])]
    age: int = Field(gt=0,lt=120)
    weight: float = Field(gt=0)
    married: Annotated[bool, Field(default=None, description='Is the patient married or not?')]
    linkedin: AnyUrl
    allergies: Optional[List[str]] = Field(max_length=5)
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