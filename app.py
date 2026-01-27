import streamlit as st
import pandas as pd
import plotly.express as px

st.title('青年の年代別 体力運動能力の推移')

# 1. サイドバーで種目を選ぶ (streamlit_03.py の技術)
with st.sidebar:
    st.header('表示設定')
    event = st.selectbox('種目を選択してください', 
                         ['握力','上体起し','長座体前屈', '反復横跳び','20mシャトルラン','持久走', '50m走', '立ち幅とび', 'ソフトボール投げ','ハンドボール投げ','新体力テストの合計点'])
    
    # 2. 性別を選ぶ (streamlit_03.py の技術)
    target_gender = st.radio("性別", ["男子", "女子"])

# --- 3. 習った if 文だけでファイルを切り替える (streamlit_05.py の応用) ---
if event == '握力':
    file_name = 'akuryoku.csv'
elif event == '上体起し':
    file_name = 'jyoutaiokosi.csv'
elif event == '長座体前屈':
    file_name = 'tyouzataizennkutu.csv'
elif event == '反復横跳び':
    file_name = 'hannpukuyokotobi.csv'
elif event == '20mシャトルラン':
    file_name = 'syatorurann.csv'
elif event == '持久走':
    file_name = 'zikyuusou.csv'
elif event == '50m走':
    file_name = '50msou.csv'
elif event == '立ち幅とび':
    file_name = 'tatohabatobi.csv'
elif event == 'softball.csv':
    file_name = 'tatohabatobi.csv'
elif event == 'ハンドボール投げ':
    file_name = 'handball.csv'
else:
    file_name = 'goukeitenn.csv'

# データを読み込む
df = pd.read_csv(file_name, header=1)

# 列に名前をつける
df.columns.values[0] = "年齢"
df.columns.values[1] = "性別"

# 4. データを絞り込む (streamlit_05.py の技術)
df_selection = df[df["性別"] == target_gender]

# 年齢を選ばせる (unique() は streamlit_05.py で使用済み)
target_age = st.selectbox("年齢を選択してください", df_selection["年齢"].unique())

# 5. 特定の行を抜き出す (特定の条件で抽出)
row = df_selection[df_selection["年齢"] == target_age]

# 6. グラフ用の準備
# 横軸(x)は列の名前、縦軸(y)はその行の数値
years = df.columns[2:]
values = row.iloc[0, 2:]

# --- 7. グラフの表示 (streamlit_ex_01.py の技術) ---
st.subheader(f"{target_age} {target_gender} の {event} 推移")

fig = px.line(x=years, y=values, markers=True,
              labels={'x': '年度', 'y': '記録（単位）'})
st.plotly_chart(fig)

# 表の表示 (streamlit_01.py の技術)
st.dataframe(row)