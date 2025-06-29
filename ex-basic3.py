import streamlit as st
import os
print(os.getcwd())
st.title("今日の料理")
st.subheader("カレーライス")
st.markdown("""
## 材料        
- 肉 200g
- 人参 1/2個
- じゃが芋 中2個
            
## 作り方      
1. 材料を切ります。
2. 肉を炒めます。
3. 煮込んでルーを入れます。      
            """) 
