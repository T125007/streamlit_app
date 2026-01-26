import streamlit as st
import pandas as pd
import plotly.express as px

st.title('広告費と売り上げ')
#データの読み込み
df = pd.read_csv('ad_expense_sales.csv')