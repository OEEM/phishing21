import streamlit as st

import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

# col1, col2 = st.columns([1, 3])

st.title('Phishing Website Detection using Machine Learning')
#st.write('This ML-based app is developed for educational purposes. Objective of the app is detecting phishing websites only using content data. Not URL!'
        # ' You can see the details of approach, data set, and feature set if you click on _"See The Details"_. ')





choice = st.selectbox("Please select your machine learning model",
                 [
                     'Gaussian Naive Bayes', 'Support Vector Machine', 'Decision Tree', 'Random Forest',
                     'AdaBoost', 'Neural Network', 'K-Neighbours'
                 ]
                )

model = ml.nb_model

if choice == 'Gaussian Naive Bayes':
    model = ml.nb_model
    st.write('GNB model is selected!')
elif choice == 'Support Vector Machine':
    model = ml.svm_model
    st.write('SVM model is selected!')
elif choice == 'Decision Tree':
    model = ml.dt_model
    st.write('DT model is selected!')
elif choice == 'Random Forest':
    model = ml.rf_model
    st.write('RF model is selected!')
elif choice == 'AdaBoost':
    model = ml.ab_model
    st.write('AB model is selected!')
elif choice == 'Neural Network':
    model = ml.nn_model
    st.write('NN model is selected!')
else:
    model = ml.kn_model
    st.write('KN model is selected!')


url = st.text_input('Enter the URL')
# check the url is valid or not
if st.button('Check!'):
    try:
        response = re.get(url, verify=False, timeout=4)
        if response.status_code != 200:
            print(". HTTP connection was not successful for the URL: ", url)
        else:
            soup = BeautifulSoup(response.content, "html.parser")
            vector = [fe.create_vector(soup)]  # it should be 2d array, so I added []
            result = model.predict(vector)
            if result[0] == 0:
                st.success("This web page seems a legitimate!")
                st.balloons()
            else:
                st.warning("Attention! This web page is a potential PHISHING!")
                st.snow()

    except re.exceptions.RequestException as e:
        print("--> ", e)





