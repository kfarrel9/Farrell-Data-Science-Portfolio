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

# grabs a string from list and names it as city
city = st.selectbox('Select a city', df["City"].unique())

st.write(f"People in {city}")

# filters the dataframe to only show rows where the City column matches the selected city
st.dataframe(df[df["City"] == city])

# st.bar_chart(df["Salary"])


# st.color_picker('Pick a color')