# Fashion Trend Forecasting - India

A data science project that forecasts fashion trend popularity in India using real Google search data.

## What it does
- Pulls live search interest data from Google Trends for fashion keywords (pastel saree, oversized shirt, cargo pants) in India
- Visualizes 12-month search trends
- Uses Facebook Prophet to forecast the next 90 days of interest
- Deployed as an interactive web dashboard

## Live App
👉 [Try it here](https://fashiontrendforecasting-45sjbldd4thughg3wmmfza.streamlit.app/)

## Tech Stack
- Python
- Streamlit (dashboard)
- Pytrends (Google Trends API)
- Prophet (time-series forecasting)
- Pandas

## How to run locally
```
pip install -r requirements.txt
streamlit run app.py
```
## Future improvements
- Add more fashion categories
- Compare trends across Indian cities
- Add social media sentiment data
