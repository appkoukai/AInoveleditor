import streamlit as st
import openai

# OpenAI APIキーを設定
openai.api_key = st.secrets["API_key"]

# Streamlit設定
st.title('文章評価アプリ') 

# ユーザー入力
user_input = st.text_area('文章を入力')

#評価機構
# 評価項目の初期値
default_items = ['テーマの出力', '描写の不足', '新規性', '改善の提案'] 
# ユーザー入力欄を設ける
evaluation_items = st.text_input('評価項目(カンマ区切りで入力)', ', '.join(default_items))
# 入力値からリストに変換
evaluation_items = evaluation_items.split(',') 
# チェックボックス表示
checked_items = [item for item in evaluation_items if st.checkbox(item)]

# ボタンクリック時に実行
if st.button('評価実行'):

# ローディングアニメーション
    with st.spinner('評価中...'):
    
        # 評価処理
            # GPT-3.5に評価してもらう
            messages = [] 
            messages.append({"role":"system", "content":f"以下の文章を評価して下さい:\n{user_input}\n\n{checked_items}"})
            messages.append({"role":"assistant", "content":"..."})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-1106",
                messages=messages
            )
            


    # 結果表示
    st.success('評価が完了しました')  
    # GPT-3.5の応答だけを抽出  
    gpt_response = response.choices[0].message.get("content")
    # 抽出した応答を表示
    st.write(gpt_response)

