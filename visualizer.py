import time, array, numpy as np
import plotly.graph_objects as go

latency = np.loadtxt('./logs/plots-all.log')

fig = go.Figure(
    data=[go.Bar(y=latency)],
    layout_title_text="127 Cached requests Single Compunit Process"
)
fig.show()