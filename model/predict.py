import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse


with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

labels = model.classes_.tolist()

def loan_approval_prediction(data:dict):

    df = pd.DataFrame([{
       'no_of_dependents':data.Dependents,
       'education':data.Education, 
       'self_employed':data.Employment_status, 
       'income_annum':data.Income_per_annum,
       'loan_amount':data.Loan_amount, 
       'loan_term':data.Loan_term, 
       'cibil_score':data.Cibil_score, 
       'residential_assets_value':data.Residential_assets_value,
       'commercial_assets_value':data.Commercial_assets_value, 
       'luxury_assets_value':data.Luxury_assets_value  
    }])

    prediction_output = model.predict(df)[0]
    predict_probabilities = model.predict_proba(df)[0]
    confidence = max(predict_probabilities)

    class_probs = dict(zip(labels,map(lambda p:round(p,4),predict_probabilities)))

    if prediction_output == 0:
        return {"message":"🤩Congratulation!! Your Loan is Approved",
                "confidence":confidence,
                "class_probabilities":class_probs
                }
    else:
        return {"message":"😔sorry!! Your Loan is not Approved,Please try later!!",
                "confidence":confidence,
                "class_probabilities":class_probs
                }
    
    

    


