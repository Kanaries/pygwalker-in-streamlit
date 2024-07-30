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

st.markdown('### More details for pygwalker, please refer it: <a href="https://kanaries.net/pygwalker">https://kanaries.net/pygwalker</a>', unsafe_allow_html=True)

# You should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    return StreamlitRenderer(df, spec="./gw_config.json", debug=False)

renderer = get_pyg_renderer()

st.subheader("Display Explore UI")

tab1, tab2, tab3, tab4 = st.tabs(
    ["graphic walker", "data profiling", "graphic renderer", "pure chart"]
)

with tab1:
    renderer.explorer()

with tab2:
    renderer.explorer(default_tab="data", key="pyg_explorer_1")

with tab3:
    renderer.viewer()

with tab4:
    st.markdown("### registered per weekday")
    renderer.chart(0)
    st.markdown("### registered per day")
    renderer.chart(1)
