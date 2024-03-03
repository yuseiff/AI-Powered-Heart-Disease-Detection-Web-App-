import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize

XGB_model = joblib.load('XGB.pkl')

# age, Sex, Cp, trestbps,chol,restecg, thalach, exang, oldpeak, slope, ca, thal

st.title('Are you Have a heart disease :mending_heart: ')
sex = st.select_slider("Gender",['Male','Female'])
age = st.number_input("Age",min_value=0,max_value=100)
cp = st.select_slider("CD",[0,1,2,3])
trestbps = st.number_input('trestbps',min_value=90,max_value=200)
chol = st.number_input('chol',min_value=51,max_value=600)
restecg = st.select_slider('restecg',[0,1,2])
thalach = st.number_input('thalach',min_value=70,max_value=210)
exang = st.select_slider('exang',[0,1])
oldpeak = st.number_input('oldpeak',min_value=0.0,max_value=6.2,step=0.5,format='%f',placeholder=0.0)
slope = st.select_slider('slope',[0,1,2])
ca = st.select_slider('ca',[0,1,2,3,4])
thal =  st.select_slider('thal',[0,1,2,3])
sex = int(sex == "Male")

def predict():
    columns = ['age','sex','cp','trestbps','chol','restecg','thalach','exang','oldpeak','slope','ca','thal']
    rows = np.array([age,sex,cp,trestbps,chol,restecg,thalach,exang,oldpeak,slope,ca,thal])
    X = pd.DataFrame([rows],columns=columns)
    X_norm = normalize(X,norm='l2')
    pred = XGB_model.predict(X_norm)[0]
    
    if pred:
        st.error('Your are having a heart disease :face_with_head_bandage:')
    else:
        st.success('Your are not having a heart disease :smile:')
        
st.button('Predict',on_click=predict)