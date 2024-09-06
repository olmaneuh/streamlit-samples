import streamlit as st

# add title
st.title("Display Text")

# add header
st.header("This is the main header")

# add subheader
st.subheader("This is a subheader")

# markdown
st.markdown("Markdown **text**")
st.markdown("# Header 1")
st.markdown("## Header 2")
st.markdown("### Header 3")
st.markdown("#### Header 4")

# caption
st.caption("This is a caption")

# code block
st.code(
    """
    import pandas as pd

    df = pd.read_csv('raw_data.csv')
    """
)

# preformatted text
st.text("Just a regular text")

# LaTex
latex_expression = r"\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}"
st.latex(latex_expression)

# divider
st.divider()

# write
st.write("Hello **World!** :sunglasses:")
