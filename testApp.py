import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Normal distribution")

samples = st.slider("samples", 0,10_000)
mu = st.slider("mu",0.0,1.0,step=0.001)
sigma = st.slider("sigma",0.0,1.0, step=0.001)
sample = np.random.normal(mu, sigma, samples)
bins = st.slider("bins",1,1000, value=10)


fig, ax  = plt.subplots()
sns.histplot(sample, bins=bins, kde=True, ax=ax)

st.pyplot(fig)


