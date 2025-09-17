from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from utils import load_ml_model
from models import UserInput


# 1. import ml model
model = load_ml_model()

# 2. create an app
app = FastAPI()

# 3. create post route
@app.post("/predict")
def predict_premium(data: UserInput):
    print(data)
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])
    
    prediction = model.predict(input_df)[0]
    return JSONResponse(status_code=200, content={'predicted category':prediction})
