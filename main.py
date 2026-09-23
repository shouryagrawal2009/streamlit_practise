import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Kinematics Visualizer")
u= st.slider("Initial velocity (m/s)", 0, 50, 10)
a= st.slider("Acceleration (m/s2)", -10, 10, 2)

t= np.linspace(0, 10, 200)
fig= go.Figure(go.Scatter(x=t, y= u+ a*t))
st.plotly_chart(fig,m use_container_width=True)
