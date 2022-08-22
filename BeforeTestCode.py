import pandas as pd
import streamlit as st
from io import  StringIO
from strsimpy.jaro_winkler import JaroWinkler

from action import *
from TAKE_OUT_TYPE import *
import time


endcoding = 'utf-8-sig'
data_DB=pd.read_excel('./清單.xlsx')
df = pd.read_csv("./測試樣本.csv",encoding=encoding)

#df['Assignee_Name_regex']=df['Assignee_Name'].astype(str).str.upper()

#'逗號切割，留下逗號前的字串[0]' '去除標點符號','去除空白'
genre = st.radio(
     "逗號切割，留下逗號前的字串[0]",
     ('YES', 'NO'))

if genre == 'YES':
    df['Assignee_Name_regex']=df['Assignee_Name'].astype(str).str.partition(',')[0]
else:
    df['Assignee_Name_regex']=df['Assignee_Name']

st.write(df)


# list.append
select_contorl=['去除Corp類型', '去除Ltd類型', '去除LLC類型','去除THE、AND、OF','去除有限合夥類型(gmbh & co. kg,Lp)',
     '去除錯字(company、corp、kabusiki kaisha...)','去除Llp','去除Lllp類型','去除Pte類型','去除Pllc類型']
container = st.container()
all = st.checkbox("Select all")
 
if all:
    options = st.multiselect(
     '選擇資料處理項目',
     select_contorl,
     select_contorl)
else:
    options = st.multiselect(
     '選擇資料處理項目',
     select_contorl,
     ['去除Corp類型', '去除Ltd類型', '去除LLC類型','去除THE、AND、OF','去除錯字(company、corp、kabusiki kaisha...)']
     )


TAKE_OUT_WORDS=[]#加入拿掉的字串
for i in options:
    if i=='去除Corp類型':
        TAKE_OUT_WORDS.append(CORP)
    if i=='去除Ltd類型':
        TAKE_OUT_WORDS.append(LIMITED)
    if i=='去除LLC類型':
        TAKE_OUT_WORDS.append(LLC)
    if i=='去除THE、AND、OF':
        TAKE_OUT_WORDS.append(NON_MEAN_WORDS)
    if i=='去除有限合夥類型(gmbh & co. kg,Lp)':
        TAKE_OUT_WORDS.append(LP)
    if i=='去除錯字(company、corp、kabusiki kaisha...)':
        WRONG_WORDS=WRONG_WORDS_ALL()
        TAKE_OUT_WORDS.append(WRONG_WORDS)
    if i=='去除Llp':
        TAKE_OUT_WORDS.append(LLP)
    if i=='去除Lllp類型':
        TAKE_OUT_WORDS.append(LLLP)
    if i=='去除Pte類型':
        TAKE_OUT_WORDS.append(PTE)    
    if i=='去除Pllc類型':
        TAKE_OUT_WORDS.append(PLLC)
        

TAKE_OUT_WORDS=sum(TAKE_OUT_WORDS,[])

st.sidebar.write(TAKE_OUT_WORDS)

df['Assignee_Name_regex']=df['Assignee_Name_regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
df['Assignee_Name_regex']=df['Assignee_Name_regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))

st.write(df)


genre_1 = st.radio(
     "去除標點符號",
     ('YES', 'NO'))

if genre_1 == 'YES':
    df['Assignee_Name_regex']=df['Assignee_Name_regex'].replace('[^A-Za-z0-9]+',' ',regex=True)
    df['Assignee_Name_regex']=df['Assignee_Name_regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
else:
    df['Assignee_Name_regex']=df['Assignee_Name_regex']

st.write(df)

genre_2 = st.radio(
     "去除空格",
     ('YES', 'NO'))

if genre_1 == 'YES':
    df['Assignee_Name_regex']=df['Assignee_Name_regex'].replace(' ','',regex=True)    
else:
    df['Assignee_Name_regex']=df['Assignee_Name_regex']

st.write(df)




from strsimpy.jaro_winkler import JaroWinkler



#有BARS
jarowinkler = JaroWinkler()
my_bar = st.progress(0)
TEMP=[]#存入相似度
AC=[]#存入比對好的質
for percent_complete in range(100):
    for i in range(0,len(df[option_df])):
        temp_data=df_count.loc[df_count['Regex'].str.contains(df['Assignee_Name_regex'][i])]#表單中找到含有相似的字串
        #st.write(temp_data)
        for j in range(0,len(temp_data['Regex'])):
            similar=jarowinkler.similarity(df['Assignee_Name_regex'].iloc[i],temp_data['Regex'].iloc[j])
            TEMP.append(similar)
                
        if max(TEMP, default=0)>=0.95:
            index=TEMP.index(max(TEMP))
            #st.write(index,i,j,temp_data.shape)
            #st.write(temp_data[option_df].iloc[index])
            AC.append(temp_data[option_df].iloc[index])
            TEMP.clear()
        else:
            AC.append('NULL')
            TEMP.clear()

            my_bar.progress(percent_complete + 1)
    df["AC"]=pd.Series(AC)
   



#無BAR
startTime = time.time()
df_count=df_count.drop_duplicates(subset=['Regex'], keep='first')
#st.write(df_count)
with st.spinner('比對中請稍後...'):
                
        
    TEMP=[]#存入相似度
    AC=[]#存入比對好的質
                
    for i in range(0,len(df[option_df])):
        temp_data=df_count.loc[df_count['Regex'].str.contains(df['Assignee_Name_regex'][i])]#表單中找到含有相似的字串
                        #st.write(temp_data)
        for j in range(0,len(temp_data['Regex'])):
            similar=jarowinkler.similarity(df['Assignee_Name_regex'].iloc[i],temp_data['Regex'].iloc[j])
            TEMP.append(similar)
                
        if max(TEMP, default=0)>=0.95:
            index=TEMP.index(max(TEMP))
                        #st.write(index,i,j,temp_data.shape)
                        #st.write(temp_data[option_df].iloc[index])
            AC.append(temp_data[option_df].iloc[index])
            TEMP.clear()
        else:
            AC.append('NULL')
            TEMP.clear()
                            
        
            df["AC"]=pd.Series(AC)
            t = time.time() - startTime

            st.write(df[[option_df,'AC']],t)
            

            st.balloons()
            time.sleep(1)