import numpy as np
import streamlit as st
import time

from sklearn.linear_model import LinearRegression


st.title("Caching Demo")

st.button("Test Cache")

# cache data example
st.subheader("Cache Data")


@st.cache_data
def cache_function():
    time.sleep(5)
    out = "Run finish..."
    return out


out = cache_function()
st.write(out)

# cache resource example
st.subheader("Cache Resource")

@st.cache_resource
def cache_linear_regression():
    time.sleep(5)
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y = np.array([1, 2, 3, 4, 5])

    model = LinearRegression().fit(X, y)

    return model


linear_regression = cache_linear_regression()
x = np.array([5]).reshape(-1, 1)
y_hat = linear_regression.predict(x)

st.write(f"The predictioin is: {y_hat[0]}")
