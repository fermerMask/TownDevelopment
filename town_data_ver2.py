import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="DataViz Studio",
    layout="wide",
    initial_sidebar_state="expanded"
)

def data_read(file):
    if file is not None:
        data_frame = pd.read_csv(file)
        return data_frame

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
df = data_read(uploaded_file)

with st.sidebar:
    st.title("データ分析プラットフォーム")


