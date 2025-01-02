import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Value': [15, 18, 20, 23, 25, 28, 30, 32, 35, 38]
})

fig = go.Figure(data=[go.Scatter(x=df['Date'], y=df['Value'], mode='lines')], 
                layout=dict(title='Time Series Plot', xaxis_title='Date', yaxis_title='Value'))
pyo.plot(fig, filename='time_series_plot.html')
