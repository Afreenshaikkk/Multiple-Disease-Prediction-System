# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 15:33:00 2025

@author: Shaik Afreen
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open("D:/Multiple Disease Prediction System/saved models/diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open("D:/Multiple Disease Prediction System/saved models/heart_disease_model.sav",'rb'))
breast_cancer_model=pickle.load(open("D:/Multiple Disease Prediction System/saved models/breast_cancer_model.sav",'rb'))
parkinson_model=pickle.load(open("D:/Multiple Disease Prediction System/saved models/parkinson_model.sav",'rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         
                         ['Diabetes Prediction','Heart Disease Prediction','Breast Cancer Prediction','Parkinson Prediction'],
                         
                         icons=['droplet','activity','hurricane','person'],
                         
                         default_index=0)
    
    
    
if(selected =='Diabetes Prediction'):
    
    
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 =st.columns(3)

    with col1:

        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:

        Glucose =st.text_input('Glucose Level')

    with col3:

        BloodPressure = st.text_input('Blood Pressure value')

    with col1:

        SkinThickness = st.text_input('Skin Thickness value')

    with col2:

        Insulin= st.text_input('Insulin Level')

    with col3:

        BMI = st.text_input('BMI value')

    with col1:

        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:

        Age = st.text_input('Age of the Person')

#code for Prediction

    diab_diagnosis =''




    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
]])
            if (diab_prediction[0]==1):

                diab_diagnosis = 'The person is Diabetic'

            else:

                diab_diagnosis = 'The person is Not Diabetic'

    st.success(diab_diagnosis)
    
if(selected =='Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 =st.columns(3)

    with col1:

        age= st.text_input('Age')

    with col2:

        sex =st.text_input('Sex')

    with col3:

        cp = st.text_input('Chest Pain Types')

    with col1:

        trestbps = st.text_input('Resting Blood Pressure')

    with col2:

        chol=st.text_input('Cholestrol level in mg/dl')

    with col3:

        fbs= st.text_input('Resting Electrocardiographic Results')

    with col1:

        restecg = st.text_input('Maximum Heartrate Achieved')
    
    with col2:

        thalach= st.text_input('Maximum Heartrate during Exercise')
        
    with col3:
        exang= st.text_input('Exercise included agina')
        
    with col1:

        oldpeak= st.text_input('ST depression by Exercise')

    with col2:

        slope= st.text_input('Slope of the peak exercise ST segment')

    with col3:

        ca=st.text_input('Major vessels colored by fluroscopy')

    with col1:

        thal= st.text_input('thal:0=normal;1=fixed defect;2=reversable defect')




    # code for Prediction

    heart_disease_diagnosis =''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction= heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0]==1:

            heart_disease_diagnosis= 'The person is having a Heart Disease'

        else:

            heart_disease_diagnosis= 'The person does not have a heart disease'

    st.success(heart_disease_diagnosis)

    
    
if(selected =='Breast Cancer Prediction'):
    
    
    st.title('Breast Cancer Prediction using ML')
    col1, col2, col3 =st.columns(3)

    with col1:

        mean_radius=st.text_input('distance from center to edge')

    with col2:

        mean_texture=st.text_input('image texture')

    with col3:

        mean_perimeter= st.text_input('Avg.length around the cell')

    with col1:

        mean_area = st.text_input('Avg.size of the cell')

    with col2:

        mean_smoothness=st.text_input('Edge smoothness of the cell')

    with col3:

        mean_compactness= st.text_input('Compactness of the cell')

    with col1:

        mean_concavity= st.text_input('Depth of concave parts of the border')
    
    with col2:

        mean_concave_points= st.text_input('No. of inward curves in the background')
        
    with col3:
        mean_symmetry = st.text_input('Symmetry of the cell shape')
        
    with col1:

        mean_fractal_dimensions= st.text_input('Irregularity of the border')





    # code for Prediction

    breast_cancer_diagnosis =''

    # creating a button for Prediction

    

    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):

        user_input = [mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimensions]

        user_input = [float(x) for x in user_input]

        breast_cancer_prediction = breast_cancer_model.predict([user_input])

        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = "The person has Parkinson's disease"
        else:
            breast_cancer_diagnosis= "The person does not have Parkinson's disease"
    st.success(breast_cancer_diagnosis)
# Parkinson's Prediction Page
if(selected == "Parkinson Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3= st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        RAP = st.text_input('MDVP:RAP')

    with col1:
        PPQ = st.text_input('MDVP:PPQ')

    with col2:
        DDP = st.text_input('Jitter:DDP')

    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')

    with col2:
        DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinson_prediction = parkinson_model.predict([user_input])

        if parkinson_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)