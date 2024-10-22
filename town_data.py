import streamlit as st
import pandas as pd

def data_read(file):
    if file is not None:
        data_frame = pd.read_csv(file)
        return data_frame

# アプリのタイトル
st.title("データの可視化")

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
df = data_read(uploaded_file)

data_tab, visual_tab = st.tabs([":data: Data", ":graph: visualization"])

with data_tab:
    if df is not None:
        st.table(df)
    else:
        st.info("csvファイルが読み込まれていません。")

with visual_tab:
    if df is not None:
        # チェックボックスで表示する項目を選択
        options = df.columns.tolist()

        # X軸とY軸を選択できるように変更
        x_axis = st.selectbox("X軸を選択してください", options)
        y_axis = st.multiselect("Y軸に表示するデータを選択してください", options, default=[options[1]])

        # グラフの種類を選択
        chart_type = st.selectbox("グラフの種類を選択してください:", ["line", "bar", "area"])

        # グラフの表示
        if x_axis and y_axis:
            # X軸の列が存在するか確認してデータをプロット
            if x_axis in df.columns:
                plot_data = df.set_index(x_axis)[y_axis]

                # グラフの描画
                if chart_type == "line":
                    st.line_chart(plot_data, use_container_width=True)
                elif chart_type == "bar":
                    st.bar_chart(plot_data, use_container_width=True)
                elif chart_type == "area":
                    st.area_chart(plot_data, use_container_width=True)
            else:
                st.error(f"選択されたX軸 '{x_axis}' はデータに存在しません。")
        else:
            st.warning("表示する項目が選択されていません。")
