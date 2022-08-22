import streamlit as st
import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
from strsimpy.jaro_winkler import JaroWinkler
#from numba import jit


encoding='utf-8-sig'
@st.cache
def convert_df(df):
# IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode(encoding)


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    return processed_data






SELECT_CONTORLS=['去除Corp類型', '去除Ltd類型', '去除LLC類型','去除THE、AND、OF','去除有限合夥類型(gmbh & co. kg,Lp)',
            '去除錯字(company、corp、kabusiki kaisha...)','去除Llp','去除Lllp類型','去除Pte類型','去除Pllc類型','轉譯字符(&amp;)']
