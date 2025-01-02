from bokeh.plotting import figure, show

x = [1, 2, 3, 4, 5]
y = [1, 6, 8, 2, 3]

graph = figure(title="Bokeh Line Graph")
graph.line(x, y)

show(graph)
