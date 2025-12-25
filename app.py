#pickle file load
#pydantic model for validation
#predict route --> user values(frontend) --> backend via apis --> model runs on it -->response generated --> pass to the frontend 

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,field_validator
from typing import Annotated
from schema.user_input import Loan_details
from model.predict import loan_approval_prediction

MODEL_VERSION = '1.0.0'

app = FastAPI()
#loading pickle file...


#pydantic class for validation...

@app.get('/')
def home_screen():
    return {'message':'Loan Approval Prediction system'}

@app.get('/health')
def health_check():
    return {
        'status code':'OK',
        'version':MODEL_VERSION

        }

@app.post('/predict')
def loan_app(user_input:Loan_details):
    # loan_approval_prediction(user_input)

    return JSONResponse(status_code=200,content={"predicted_category":loan_approval_prediction(user_input)})




