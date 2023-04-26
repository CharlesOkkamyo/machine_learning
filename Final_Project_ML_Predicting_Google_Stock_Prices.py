import streamlit as st
import numpy as np 
import pandas as pd 

st.title('Final Project of Google Stocks Prediction and Machine Learning')

Date = 'date'

def load_data(nrows):
    data = pd.read_csv('\\google-stock-dataset-Daily.csv.')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[Date] = pd.to_datetime(data[Date])
    return data

data_load_state = st.text('Loading data...')
training_data = load_data(10000)
data_load_state.text('Loading data...done!')

hist_values = np.histogram(
    training_data[Date].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
