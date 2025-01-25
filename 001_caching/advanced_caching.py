import streamlit as st


# cache the data for 1h (1h = 3600 seconds)
@st.cache_data(ttl=3600)
def cache_function():
    pass


# set the max num of entries in the cache. will discard old values in the cache
# this avoids the cache run out of memory.
@st.cache_data(max_entries=1000)
def cache_function_2():
    pass


# disable the caching spinner showed in the UI.
@st.cache_data(show_spinner=False)
def show_spinner():
    pass


# custom message while showing the spinner.
@st.cache_data(show_spinner="Custom spinner message...")
def custom_spinner_message():
    pass


# use underscore before a param to exclude it from the cache
@st.cache_data
def exlude_params(_model, x):
    pass


# NOTES:
#
# Cache docs:
# https://docs.streamlit.io/develop/concepts/architecture/caching
#
# Check when dealing with large data:
# https://docs.streamlit.io/develop/concepts/architecture/caching#dealing-with-large-data
