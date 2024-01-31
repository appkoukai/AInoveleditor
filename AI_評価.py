import streamlit as st
import openai

# OpenAI APIキーを設定
openai.api_key = st.secrets["API_key"]

# Streamlit設定
st.title('文章評価アプリ') 

# ユーザー入力
user_input = st.text_area('文章を入力')

# 評価項目の定義と選択
evaluation_items = ['構成', '表現', '説得力']
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

