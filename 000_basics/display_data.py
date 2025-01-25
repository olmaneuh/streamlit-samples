import pandas as pd
import streamlit as st

df = pd.read_csv("./data/stock_sample_data.csv")

st.title("Display Data")

# display dataframe
st.dataframe(df)
st.write(df)

# display a table
st.table(df)

# display a metric
st.metric(label="META", value=527.42, delta=-9.91, delta_color="normal")
