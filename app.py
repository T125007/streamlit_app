import streamlit as st
import pandas as pd
import plotly.express as px

st.title('青年の年代別 体力運動能力の推移')

st.info(f"""
**このサイトの概要・目的・使用方法の説明**
1. **概要**: このアプリは、昭和から令和にかけての日本人の体力・運動能力の変遷を可視化するツール。。
2. **目的**: 文部科学省の統計データを基に、特定の年齢や性別が、時代と共にどう変化したかを確認できる。
3. **使用方法**:  1．左のサイドバーから「種目」と「性別」を選択する。
2．画面中央のセレクトボタンで「年齢」を選択する。
3．その種目・年齢をもとにしたグラフを作成する。また、年代と年齢別年代ごとの平均値のデータを作成し、年々データがどのような変化をしているのか見れるようにした。最後に年齢と性別の記録を並べた表を作成した。
""")

st.success(f"""
           **このデータの確認**
           1. **分析対象**：7歳から19歳の男女
           2. **調査項目**：握力、上体超し、長座体前屈、反復横跳び、20mシャトルラン、持久走、50m走、立ち幅跳び、ソフトボール投げ、ハンドボール投げ、合計点
           3. **データの規模**：昭和・平成・令和の3世代にわたる長期的な統計データ
           """)

# サイドバーで種目を選ぶ 
with st.sidebar:
    st.header('表示設定')
    event = st.selectbox('種目を選択してください', 
                         ['握力','上体起し','長座体前屈', '反復横跳び','20mシャトルラン','持久走', '50m走', '立ち幅とび', 'ソフトボール投げ','ハンドボール投げ','新体力テストの合計点'])
    
    # 性別を選ぶ 
    target_gender = st.radio("性別", ["男子", "女子"])

# 習った if 文だけでファイルを切り替える 
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
elif event == 'ソフトボール投げ':
    file_name = 'softball.csv'
elif event == 'ハンドボール投げ':
    file_name = 'handball.csv'
else:
    file_name = 'goukeitenn.csv'

# データを読み込む
df = pd.read_csv(file_name, header=1)

# 列に名前をつける
df.columns.values[0] = "年齢"
df.columns.values[1] = "性別"

# データを絞り込む 
df_selection = df[df["性別"] == target_gender]

# 年齢を選ばせる
target_age = st.selectbox("年齢を選択してください", df_selection["年齢"].unique())

# 特定の行を抜き出す
row = df_selection[df_selection["年齢"] == target_age]

# グラフ用の準備
years = df.columns[2:]
values = row.iloc[0, 2:]

# グラフの表示 
st.subheader(f"{target_age} {target_gender} の {event} 推移")
st.info(f"{target_age}{target_gender}の推移を読み取ることで{target_age}{target_gender} の青年はどの年代の子がどのくらいの記録を出しているのかわかり傾向を知り比較することが可能です。")

fig = px.line(x=years, y=values, markers=True,
              labels={'x': '年度', 'y': '記録（単位）'})
st.plotly_chart(fig)

# --- ここからが「全年齢平均」の追加コード！ ---

st.divider() # 線を引いて区切ると見やすくなります
st.header(f'📈 {event} の全体的な推移 (全年齢平均)')
st.info(f"{event}の全体的な推移を読み取ることで{event}はどの年代が高い数値を記録しているのかという傾向を知り、比較することができます。")

# 1. 年度（数字が入っている列）だけを抜き出す
data_only = df_selection[years]

# 2. 数字じゃない文字（…）を「空欄」にして「数字」に変える（お掃除）
data_numeric = data_only.apply(pd.to_numeric, errors='coerce')

# 3. 縦方向に平均を計算する（合体）
yearly_average = data_numeric.mean()

# 4. 平均値のグラフを表示する
fig_avg = px.line(x=yearly_average.index, 
                  y=yearly_average.values, 
                  markers=True,
                  labels={'x': '年度', 'y': '全年齢の平均記録'},
                  title=f'{target_gender} 全体の平均的な変化')

st.plotly_chart(fig_avg)

# 表の表示 
st.dataframe(row)
st.error(f"表の中にあるように、 一部の年度（古いデータなど）において欠損値「…」が見られます。この部分のデータがないことで{target_age} {target_gender} の {event} 推移のグラフで表示されないところがあります。また、全年齢の平均記録がほかの年代と比べると大幅にズレることがあります")