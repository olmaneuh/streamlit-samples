import streamlit as st


# title
st.title("Layout Examples")


# sidebar
with st.sidebar:
    st.title("Sidebar Section")
    st.write("You can add various widgets here.")
    sidebar_select = st.selectbox(
        "Choose a stock:", options=["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META"]
    )

    st.write(f"Your stock: {sidebar_select}")


# columns
st.header("Colums Layout")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Column 1")
    st.button("Ok", type="primary")

with col2:
    st.write("Column 2")
    st.slider("Day", min_value=1, max_value=31, value=1)

with col3:
    st.write("Column 3")
    st.text_input("Name:", placeholder="e.g. Tony Stark")


# tabs
st.header("Tabs Layout")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("This is Tab 1 content")
    st.checkbox("Check me")

with tab2:
    st.write("This is Tab 2 content")
    st.radio("Choose one", ["Option A", "Option B", "Option C"])


# expander
st.header("Expander Layout")

with st.expander("Click to expand"):
    st.write("This is the content inside the expander section.")


# container
st.header("Container Layout")

with st.container():
    st.write("This is inside the container")

st.write("This is outside the container")
