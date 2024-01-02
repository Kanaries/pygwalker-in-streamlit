import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pygwalker_tools.metrics import MetricsChart

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Pygwalker Tools - Metrics Tool",
    layout="wide"
)

# Add Title
st.title("Pygwalker Tools - Metrics Tool")

FIELD_MAP = {
    "date": "active_time",
    "user_id": "user_id",
    "user_signup_date": "user_signup_date"
}

CACHE_TTL = 3600
CHART_HEIGHT = 800


@st.cache_data()
def get_dataset() -> pd.DataFrame:
    df = pd.read_csv("https://pygwalker-public-bucket.s3.amazonaws.com/datas/metrics_mock_datas")
    return df


@st.cache_resource(ttl=CACHE_TTL)
def new_user_retention(time_size: int, time_unit: str) -> str:
    retention = MetricsChart(
        get_dataset(),
        FIELD_MAP,
        params={"time_unit": time_unit, "time_size": time_size}
    ).retention()

    new_user_count = MetricsChart(get_dataset(), FIELD_MAP).new_user_count().properties(height=60)

    return (retention & new_user_count).to_html()


@st.cache_resource(ttl=CACHE_TTL)
def pv() -> str:
    return MetricsChart(get_dataset(), FIELD_MAP).pv().to_html()


@st.cache_resource(ttl=CACHE_TTL)
def uv() -> str:
    return MetricsChart(get_dataset(), FIELD_MAP).uv().to_html()


@st.cache_resource(ttl=CACHE_TTL)
def cohort_matrix() -> str:
    heatmap = MetricsChart(
        get_dataset(),
        FIELD_MAP
    ).cohort_matrix()

    new_user_count = MetricsChart(get_dataset(), FIELD_MAP, reverse_axis=True).new_user_count()

    return (new_user_count | heatmap).to_html()


@st.cache_resource(ttl=CACHE_TTL)
def active_user_count(within_active_days: int) -> str:
    return MetricsChart(get_dataset(), FIELD_MAP, params={"within_active_days": within_active_days}).active_user_count().to_html()


@st.cache_resource(ttl=CACHE_TTL)
def user_churn_rate(within_active_days: int) -> str:
    return MetricsChart(get_dataset(), FIELD_MAP, params={"within_active_days": within_active_days}).user_churn_rate_base_active().to_html()


pv_tab, uv_tab, active_user_tab, retention_tab, cohort_matrix_tab, user_churn_rate_tab = st.tabs(
    ["pv", "uv", "active_user", "1 day retention", "cohort_matrix", "user_churn_rate"]
)

with pv_tab:
    components.html(pv(), height=CHART_HEIGHT)
with uv_tab:
    components.html(uv(), height=CHART_HEIGHT)
with active_user_tab:
    components.html(active_user_count(30), height=CHART_HEIGHT)
with retention_tab:
    components.html(new_user_retention(1, "day"), height=CHART_HEIGHT)
with cohort_matrix_tab:
    components.html(cohort_matrix(), height=CHART_HEIGHT, scrolling=True)
with user_churn_rate_tab:
    components.html(user_churn_rate(30), height=CHART_HEIGHT)
