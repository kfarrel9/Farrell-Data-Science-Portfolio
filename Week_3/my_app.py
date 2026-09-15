import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

if st.button("Click me"):
    st.write("Button clicked!")

import pandas as pd

st.subheader("Exploring Our Dataset")

df = pd.read_csv("data/sample_data.csv")

# if in Week 2. this leaves week 3 that we entered in terminal, and now looks from a wider view
# pd.read_csv("./week_2/data/sample_data.csv")

st.write("Here's our data")
st.dataframe(df)

