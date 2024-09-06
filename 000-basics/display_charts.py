import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# load data
df = pd.read_csv("./data/stock_sample_data.csv")
df_geo = pd.read_csv("./data/geo_sample_data.csv")

# display lineplot
st.line_chart(data=df, x="stock")

# display area chart
st.area_chart(data=df, x="stock", y=["open", "close"])

# display bar chart
st.bar_chart(data=df, x="stock", y="close")

# display a map
st.map(df_geo)

# display matplotlib chart
fig, ax = plt.subplots()
ax.plot(df["stock"], df["close"])
ax.set_title("Matplotlib Chart")
ax.set_xlabel("Stock")
ax.set_ylabel("Close Price")

st.pyplot(fig)
