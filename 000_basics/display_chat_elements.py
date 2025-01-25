import streamlit as st
import time


# chat input
prompt = st.chat_input("Type your prompt")
st.write(f"Prompt: {prompt}")

st.divider()


# chat message
with st.chat_message("user"):
    st.write(prompt)

with st.chat_message("assistant"):
    st.write("Sorry, I'm out of service :(")

st.divider()


# status
with st.status("Loading data...") as status:
    st.write("validating...")
    time.sleep(5)
    status.update(label="Completed!", state="complete", expanded=False)

st.divider()


# write stream
def get_stream_data():
    _LOREM_IPSUM = """
    Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(get_stream_data)
