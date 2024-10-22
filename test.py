import streamlit as st
import pandas as pd

# サイドバーでフィールドリストを表示
st.sidebar.title("Field List")
columns = ["年", "男性", "女性", "合計", "世帯数", "行数", "値"]

# データフィールドをサイドバーに表示
for col in columns:
    st.sidebar.write(f"📄 {col}")

# タブの作成
data_tab, visual_tab = st.tabs([":bar_chart: Data", ":art: Visualization"])

with data_tab:
    st.header("データ表示")
    st.write("データを表示します。ここにテーブルなどを表示できます。")

with visual_tab:
    st.header("ビジュアライゼーション")

    # X軸とY軸の選択
    st.subheader("X-Axis and Y-Axis Selection")
    x_axis = st.selectbox("X-Axis", columns, index=0)
    y_axis = st.multiselect("Y-Axis", columns, default=[columns[1]])

    # その他のオプション（色、サイズなど）を選択可能にする
    st.subheader("Additional Options")
    color_option = st.selectbox("Color", columns, index=0)
    size_option = st.selectbox("Size", columns, index=0)
    shape_option = st.selectbox("Shape", columns, index=0)
    opacity_option = st.slider("Opacity", 0.0, 1.0, 0.5)

    # チャートタイプ選択
    chart_type = st.selectbox("Chart Type", ["line", "bar", "area"])

    # フィルターなどの追加オプションをここで実装（今回はダミー機能）
    st.subheader("Filters")
    filters = st.text_input("Apply filters (e.g., year > 2020)")

    # CSVファイルのアップロード
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # チャートの描画
        st.subheader("Generated Chart")
        if chart_type == "line":
            st.line_chart(df[[x_axis] + y_axis])
        elif chart_type == "bar":
            st.bar_chart(df[[x_axis] + y_axis])
        elif chart_type == "area":
            st.area_chart(df[[x_axis] + y_axis])

    else:
        st.warning("CSVファイルがアップロードされていません。")

