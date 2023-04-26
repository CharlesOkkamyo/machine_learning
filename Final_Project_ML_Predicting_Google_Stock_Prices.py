import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

st.title('Uber pickups in NYC')
data = pd.read_csv('google_stock_data.csv', index_col='Date', parse_dates=True)
