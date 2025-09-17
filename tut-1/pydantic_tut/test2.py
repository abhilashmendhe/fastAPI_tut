from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int
    weight: float 
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com','icici.com']
        
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain.')

        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value 
        else: 
            raise ValueError('Age should be in between 0 and 100')
    
patient_info = {
    'name':'abhi', 
    'email': 'abhi@icici.com',
    'age':'31', 
    'weight': 72.12, 
    'married': True, 
    'allergies':['pollen','dust'],
    'contact_details':{'email':'abhi@gmail.com','phone':'99999999'}
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    
    print(patient)
    
insert_patient_data(patient1)