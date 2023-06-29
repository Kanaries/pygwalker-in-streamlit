import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Add Title
st.title("Use Pygwalker In Streamlit")

# Import your data
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")

# Paste the copied Pygwalker chart code here
vis_spec = """[{"visId":"gw_rZy5","name":"Chart 1","encodings":{"dimensions":[{"dragId":"gw_BUE2","fid":"ZGF0ZV8x","name":"date","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_x1ug","fid":"bW9udGhfMg==","name":"month","semanticType":"ordinal","analyticType":"dimension"},{"dragId":"gw_zRAa","fid":"c2Vhc29uXzM=","name":"season","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_ZeVh","fid":"eWVhcl81","name":"year","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_JqXv","fid":"aG9saWRheV82","name":"holiday","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_OD2F","fid":"d29yayB5ZXMgb3Igbm90XzE0","name":"work yes or not","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_KgQu","fid":"YW0gb3IgcG1fMTU=","name":"am or pm","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_PqvI","fid":"RGF5IG9mIHRoZSB3ZWVrXzE2","name":"Day of the week","semanticType":"ordinal","analyticType":"dimension"}],"measures":[{"dragId":"gw_7JNg","fid":"aW5kZXhfMA==","name":"index","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_IYM_","fid":"aG91cl80","name":"hour","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_ofd8","fid":"dGVtcGVyYXR1cmVfNw==","name":"temperature","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_sGlX","fid":"ZmVlbGluZ190ZW1wXzg=","name":"feeling_temp","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_674M","fid":"aHVtaWRpdHlfOQ==","name":"humidity","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_AxQD","fid":"d2luc3BlZWRfMTA=","name":"winspeed","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_iy94","fid":"Y2FzdWFsXzEx","name":"casual","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_9J2u","fid":"cmVnaXN0ZXJlZF8xMg==","name":"registered","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_WzEF","fid":"Y291bnRfMTM=","name":"count","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_count_fid","fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}}],"rows":[{"dragId":"gw_gJqj","fid":"cmVnaXN0ZXJlZF8xMg==","name":"registered","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"columns":[{"dragId":"gw_uZ9C","fid":"RGF5IG9mIHRoZSB3ZWVrXzE2","name":"Day of the week","semanticType":"ordinal","analyticType":"dimension"}],"color":[{"dragId":"gw_04s5","fid":"c2Vhc29uXzM=","name":"season","semanticType":"nominal","analyticType":"dimension"}],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"details":[],"filters":[],"text":[]},"config":{"defaultAggregated":true,"geoms":["auto"],"stack":"stack","showActions":false,"interactiveScale":false,"sorted":"none","zeroScale":true,"size":{"mode":"auto","width":320,"height":200},"format":{}}}]"""

# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, spec=vis_spec, return_html=True)

# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
