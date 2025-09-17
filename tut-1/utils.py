import json
import aiofiles

def load_patients_data(path="./data/patients.json"):
    
    with open(path, 'r') as f:
        data = f.read()

    return json.loads(data)

async def async_load_patients_data(path="./data/patients.json"):
    
    async with aiofiles.open(path, 'r') as f:
        data = await f.read()

    return json.loads(data)

async def save_data(data, path="./data/patients.json"):
    with open(path, 'w') as f:
        json.dump(data, f)