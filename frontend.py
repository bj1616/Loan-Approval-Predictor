import streamlit as st
import requests

API_URL = "http://host.docker.internal:8000/predict"


st.title("Loan Approval Predictor")


with st.sidebar:
    st.subheader(f"This System is developed in order to help customers to know their status of getting 'loan approvals' by providing their certain details.")

col1,col2= st.columns(2)
with col1:
    dependents = st.number_input("Enter the No of Dependents",min_value=0,max_value=50,value=4)
    education = st.selectbox("Are You Graduated?",options=[True,False])
    employment_status = st.selectbox("Are You Self-Employed?",options=[True,False])
    Income_per_annum = st.number_input("Enter Your Income per Annum",min_value=0,value=50000,step=500)
    Loan_amount = st.number_input("Enter Your loan Amount",min_value=0,value=400000,step=10000)

with col2:
    Loan_term = st.number_input("Enter the Loan Duration",min_value=0,value=12)
    Cibil_score = st.number_input("Enter Your CIBIL score:",min_value=0,value=750,step=50)
    Residential_assets_value = st.number_input("Enter Your Residential Assets Value",min_value=-1,value=0,step=10000)
    Commercial_assets_value = st.number_input("Enter Your Commercial Assets Value",min_value=-1,value=0,step=10000)
    Luxury_assets_value = st.number_input("Enter Your Luxury Assets Value",min_value=-1,value=0,step=10000)


# col1, col2, col3 = st.columns([3, 1, 3])
# with col2:
if st.button("Predict",type="primary"):
    input_data = {
    'Dependents':dependents,
    'Education':education, 
    'Employment_status':employment_status, 
    'Income_per_annum':Income_per_annum,
    'Loan_amount':Loan_amount, 
    'Loan_term':Loan_term, 
    'Cibil_score':Cibil_score, 
    'Residential_assets_value':Residential_assets_value,
    'Commercial_assets_value':Commercial_assets_value, 
    'Luxury_assets_value':Luxury_assets_value  
    }


    try:
        response = requests.post(API_URL,json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Result:**{result.get('predicted_category', {}).get('message')}**")
            st.success(f"Confidence Score:**{result.get('predicted_category', {}).get('confidence')}**")
            st.success(f"Class Probabilities:**{result.get('predicted_category', {}).get('class_probabilities')}**")
            
        else:
            st.error(f"Error in Prediction **{response.status_code} - {response.text}**",icon="🚨")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the fastapi server do check the Api is runninig on provided port")
            

        

       