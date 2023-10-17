from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Initialize pygwalker communication
init_streamlit_comm()

# Add Title
st.title("Use Pygwalker In Streamlit")

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    return StreamlitRenderer(df, spec="./gw_config.json", debug=False)

renderer = get_pyg_renderer()

st.subheader("Display Explore UI")
# display explore ui, Developers can use this to prepare the charts you need to display.
renderer.render_explore()

st.subheader("Display Chart UI")

tab1, tab2 = st.tabs(
    ["registered per weekday", "registered per day"]
)

# display chart ui
with tab1:
    renderer.render_pure_chart(0)
with tab2:
    renderer.render_pure_chart(1)
