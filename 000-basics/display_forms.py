import streamlit as st


# title
st.title("Buy Your Stocks")

# form
with st.form(key="buy_stock_form"):
    # form inpyt fields
    stock = st.text_input("Stock", placeholder="e.g. META, GOOGL")
    number_shares = st.number_input("Number of shares", min_value=1, step=1)
    order_type = st.selectbox("Order type", options=["Market", "Limit", "Stop"])
    accept_terms = st.checkbox("Accept terms and conditions")

    # submit button
    submit_btn = st.form_submit_button("Buy")

# form submitted
if submit_btn:
    if accept_terms:
        share_price = 130
        total = number_shares * share_price

        # order summary
        st.header("Order Summary")
        st.write(f"**Stock:** {stock}")
        st.write(f"**Number of shares:** {number_shares}")
        st.write(f"**Price per share:** {share_price}")
        st.write(f"**Order type:** {order_type}")
        st.write(f"**Total:** {total}")

        st.success("Order submitted successfully!")
    else:
        st.warning(
            "You must accept the terms and conditions before submitting the order"
        )
