import streamlit as st
import pandas as pd
import plotly.express as px

st.title('青年の年代別 体力運動能力の推移')
# 1. ファイル名と種目名の対応付け
file_map = {
    "握力": "akuryoku.csv",
    "50m走": "50msou.csv",
    "ハンドボール投げ": "handball.csv",
    "反復横とび": "hannpukuyokotobi.csv",
    "上体起こし": "jyoutaiokosi.csv",
    "ソフトボール投げ": "softball.csv",
    "20mシャトルラン": "syatorurann.csv",
    "立ち幅とび": "tatohabatobi.csv",
    "長座体前屈": "tyouzataizennkutu.csv",
    "持久走": "zikyuusou.csv"
}
#サイドバーの設定
with st.sidebar:
    #種目の設定
    st.header('種目選択')
    selected_event_name = st.selectbox('検索する種目を選択してください',list(file_map.keys()))

    # 性別・年齢の選択肢（CSVの1~2列目から抽出）
    target_gender = st.radio("性別", ["男子", "女子"])

df = df[df['event_name'].isin(selected_event)] 
df = df[df['year']==selected_year] 

st.dataframe(df)
if not df.empty:
    fig = px.scatter(
        df,
        x='event_name',
        y='year',
    )
    st.plotly_chart(fig)