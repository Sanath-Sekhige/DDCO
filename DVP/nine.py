import plotly.graph_objs as go
import plotly.offline as pyo
import random

data = go.Scatter3d(
    x=[random.uniform(1, 10) for _ in range(50)],
    y=[random.uniform(1, 10) for _ in range(50)],
    z=[random.uniform(1, 10) for _ in range(50)],
    mode='markers',
    marker=dict(size=5, color=[random.uniform(1, 10) for _ in range(50)], colorscale='Viridis')
)

layout = dict(
    title='3D Scatter Plot',
    scene=dict(
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        zaxis_title='Z-axis'
    )
)

fig = go.Figure(data=[data], layout=layout)

pyo.plot(fig, filename='3d_scatter_plot.html')
