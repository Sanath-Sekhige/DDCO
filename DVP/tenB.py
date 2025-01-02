import plotly.express as px

data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Lat': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    'Lon': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740]
}

fig = px.scatter_geo(data, lat='Lat', lon='Lon', text='City')
fig.update_geos(projection_type="orthographic")
fig.update_layout(title="Sample Map")
fig.show()
