import streamlit as st
from io import  StringIO
import pandas as pd
import time

encoding ='utf-8-sig'

df = pd.read_csv("",encoding=encoding)


upload_type= st.radio(
     "請選擇上傳檔案類型",
     ('Csv', 'Excel'))

if upload_type == 'Csv':
    uploaded_file = st.file_uploader("選擇CSV檔")
    if uploaded_file is not None:
     
        bytes_data = uploaded_file.getvalue()
     
        stringio = StringIO(uploaded_file.getvalue().decode(encoding))
     
        string_data = stringio.read()

        df = pd.read_csv(uploaded_file,encoding=encoding)

        option_df = st.selectbox(
        '選擇比對欄位',
        (df.columns))
        
        time.sleep(2)
        st.write('比對欄位', df[option_df])

