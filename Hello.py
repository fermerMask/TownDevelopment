import streamlit as st

st.set_page_config(
    page_title="DataViz Studio",
    page_icon="📊",
)

st.write("# DataViz Studioへようこそ！ 👋")

#st.sidebar.success("上のデモから選択してください。")

st.markdown(
    """
    ** 👈 サイドバーからデータ分析のためのページに移動してください！

    ### CSVデータを使ったグラフの作成
    Streamlitを使えば、CSV形式のデータを簡単にアップロードし、美しいグラフに変換できます。
    データを視覚化することで、洞察を得るのが容易になり、分析結果をわかりやすく伝えることができます。
    
    ### ページの説明
    
    * Town Data Viz
    csvファイルをアップロードすると、データが簡単に表示できます。適当に分析したいときに適しています。
    
    * Data Viz
    csvファイルをアップロードすると、詳細なデータ分析を行うことができる画面が表示されます。
    相関関係等のちょっと深堀したデータ分析をしたいときに適しています。
    """
)
