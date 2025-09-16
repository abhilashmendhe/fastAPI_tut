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

pat1_dicts = patient1.model_dump() # converts to python dict
print(pat1_dicts)

pat1_json = patient1.model_dump_json() # converts to JSON
print(pat1_json)

pat2_some = patient1.model_dump(exclude=['name']) # exclude 'name'
print(pat2_some)

