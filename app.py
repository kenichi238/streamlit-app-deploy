import streamlit as st

# Streamlitアプリのタイトル
st.title("Hello Streamlit!")

# サイドバー
st.sidebar.header("設定")
user_name = st.sidebar.text_input("お名前を入力してください", "太郎")

# メインコンテンツ
st.write(f"こんにちは、{user_name}さん！")
st.write("これはStreamlitで作成されたWebアプリです。")

# ボタン
if st.button("クリックしてください"):
    st.success("ボタンがクリックされました！")
    st.balloons()

# スライダー
age = st.slider("年齢を選択してください", 0, 100, 25)
st.write(f"選択された年齢: {age}歳")

# チャート例
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)