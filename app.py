import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
from prophet import Prophet

st.title("Fashion Trend Forecasting - India")

keywords = ["pastel saree", "oversized shirt", "cargo pants"]
selected = st.selectbox("Choose a fashion keyword", keywords)

pytrends = TrendReq(hl='en-IN', tz=330)
pytrends.build_payload([selected], timeframe='today 12-m', geo='IN')
data = pytrends.interest_over_time()

st.subheader(f"Search interest for: {selected}")
st.line_chart(data[selected])

df = data.reset_index()[['date', selected]]
df.columns = ['ds', 'y']
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

st.subheader("90-Day Forecast")
fig = model.plot(forecast)
st.pyplot(fig)
