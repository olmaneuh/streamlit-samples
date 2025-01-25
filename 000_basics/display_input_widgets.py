import streamlit as st

# buttons
primary_btn = st.button(label="Primary", type="primary")
seconday_btn = st.button(label="Secondary", type="secondary")

if primary_btn:
    st.write("primay_btn is True")

if seconday_btn:
    st.write("seconday_btn is True")

st.divider()


# checkbox
checkbox = st.checkbox("Accept terms and conditions.")

if checkbox:
    st.write("Terms and conditions accepted.")
else:
    st.write("Terms and conditions not accepted.")

st.divider()


# radio buttons
radio = st.radio("Choose a letter: ", options=["A", "B", "C"], horizontal=True)
st.write(f"Letter choosen: {radio}")

st.divider()


# selectbox
select = st.selectbox(
    "Choose a stock:", options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META"]
)
st.write(f"Stock picked: {select}")

st.divider()


# multiselect
multiselect = st.multiselect(
    "Choose your favorite stocks:",
    options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META"],
)
st.write(f"Stocks picked: {multiselect}")

st.divider()


# slider
slider = st.slider(
    "Choose a number:", min_value=0.0, max_value=10.0, value=5.0, step=1.0
)
st.write(f"Number: {slider}")

st.divider()


# number input
number_input = st.number_input("How many stocks:", min_value=1, value=1, step=1)
st.write(f"Stocks quantity: {number_input}")

st.divider()


# text input
text_input = st.text_input("Type you stock", placeholder="META")
st.write(f"Stock: {text_input}")

st.divider()


# text area
text_area = st.text_area("Notes:", height=50)
st.write(f"Notes: {text_area}")

st.divider()


# date
date = st.date_input("Pick a date")
st.write(f"Date: {date}")

st.divider()


# time
time = st.time_input("Pick a time")
st.write(f"Time: {time}")
