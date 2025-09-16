import json
import aiofiles

async def load_patients_data(path="./data/patients.json"):
    
    async with aiofiles.open(path, 'r') as f:
        data = await f.read()

    return json.loads(data)