import streamlit as st
from datetime import datetime, timedelta


st.title("Advanced State Management")


##### display session state #####
st.write("Session State:")
st.write(st.session_state)

st.button("Update state")
st.divider()


##### store widget value in session state #####
st.subheader("1. Store widget value in session state")

st.slider(label="Select a number", min_value=1, max_value=10, key="slider")


##### initialize widget value with session state #####
st.subheader("2. Initialize widget value with session state")

if "num_input" not in st.session_state:
    st.session_state["num_input"] = 5

st.number_input(label="Select a number", min_value=1, max_value=10, key="num_input")


##### using callbacks #####
st.subheader("3. Using callbacks")

st.markdown("#### 3.1 Select you time range")


def add_days():
    start_date = st.session_state["start_date"]

    match st.session_state["day_range"]:
        case "7 days":
            st.session_state["end_date"] = start_date + timedelta(days=7)
        case "28 days":
            st.session_state["end_date"] = start_date + timedelta(days=28)


def subtract_days():
    end_date = st.session_state["end_date"]

    match st.session_state["day_range"]:
        case "7 days":
            st.session_state["start_date"] = end_date - timedelta(days=7)
        case "28 days":
            st.session_state["start_date"] = end_date - timedelta(days=28)


st.radio(
    label="Day range",
    options=["7 days", "28 days", "custom"],
    horizontal=True,
    key="day_range",
    on_change=add_days,
)

col1, col2 = st.columns(2)

col1.date_input("Start date", key="start_date", on_change=add_days)
col2.date_input("End date", key="end_date", on_change=subtract_days)
