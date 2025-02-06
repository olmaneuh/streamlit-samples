import streamlit as st

st.title("Stateful Apps")

st.write("Session State:")
st.write(st.session_state)

st.button("Update state")

# set the value using the key-value syntax
if "key" not in st.session_state:
    st.session_state["key"] = "value"

# set the value using the attribute syntax
if "attribute" not in st.session_state:
    st.session_state.attribute = "another-value"

# read value from session state
st.write(f"Reading with key-value syntax: {st.session_state['key']}")
st.write(f"Reading with attribute-value syntax: {st.session_state.attribute}")

# update values in state
st.session_state["key"] = "new-value"
st.session_state.attribute = "another-new-value"

# delete item in state
delete_btn = st.button("Delete state")

if delete_btn:
    del st.session_state["key"]
    del st.session_state.attribute
