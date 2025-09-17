from pydantic import BaseModel

class Address(BaseModel):
    
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    
    name: str
    gender: str
    age: int 
    address: Address
    
address_dict = {'city':'Nagpur','state':'Maharasthra','pin':'444444'}

address1 = Address(**address_dict)

patient_info = {
    'name':'abhi', 
    'gender': 'male',
    'age':31, 
    'address': address1
}

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    
    print(patient)
    
insert_patient_data(patient1)