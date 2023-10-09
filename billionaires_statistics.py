from typing import List

import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, StreamlitRenderer, PreFilter

st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title("Billionaires Statistics")
st.subheader("data source: https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset/data")

# Initialize pygwalker communication
init_streamlit_comm()


@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv("./Billionaires Statistics Dataset.csv")


@st.cache_data
def get_all_country() -> List[str]:
    return get_data()["country"].unique().tolist()


# When using `use_kernel_calc=True`, you should cache your pygwalker renderer, if you don't want your memory to explode
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = get_data()
    # When you need to publish your application, you need set `debug=False`,prevent other users to write your config file.
    return StreamlitRenderer(df, spec="./billion_config.json", debug=False)


renderer = get_pyg_renderer()

# display explore ui, Developers can use this to prepare the charts you need to display.
# renderer.render_explore()

pre_filters = []

selected_country = st.multiselect(
    'please select country',
    get_all_country(),
    []
)

if selected_country:
    pre_filters.append(PreFilter(
        field="country",
        op="one of",
        value=selected_country
    ))

renderer.set_global_pre_filters(pre_filters)

tab1, tab2 = st.tabs(
    ["Area Distribution", "Gender Distribution"]
)

# display chart ui
with tab1:
    st.subheader("Country Distribution")
    renderer.render_pure_chart(0)
    st.subheader("Area Distribution")
    renderer.render_pure_chart(2)

with tab2:
    st.subheader("Gender Distribution")
    renderer.render_pure_chart(1)
    st.subheader("Gender Distribution By Rank")
    renderer.render_pure_chart(3)
    st.subheader("Gender Distribution By Age")
    renderer.render_pure_chart(4, width=400)
