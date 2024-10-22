from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Prefecture Data Analysis",
    layout="wide"
)


@st.cache_resource
def get_pyg_render(df) -> "StreamlitRenderer":
    return StreamlitRenderer(df,spec="./gw_config.json",spec_io_mode="rw")

st.title("Test App")
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    renderer = get_pyg_render(df)
    renderer.explorer()


