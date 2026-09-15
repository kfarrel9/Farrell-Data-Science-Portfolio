import streamlit as st

st.title("Hello, streamlit!")
st.write("This is my first Streamlit app.")

if st.button("Click me"):
    st.write("Button clicked!")

import pandas as pd

st.subheader("Exploring Our Dataset")

df = pd.read_csv("/Users/kfarrell/Documents/Farrell-Data-Science-Portfolio-Fall2026/Week_3/data/sample_data.csv")
