import pygwalker as pyg
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("Use Pygwalker In Streamlit")

# Add subtitle
SUB_TITLE = """
<span>Learn how to use pygwalker: </span>
<a target="_blank" href="https://docs.kanaries.net/graphic-walker/create-data-viz">document</a>
"""
components.html(SUB_TITLE, height=40)

# Generate the HTML using Pygwalker
pyg_html = pyg.walk(pd.DataFrame(), return_html=True, hideDataSourceConfig=False)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
