import pandas as pd
import streamlit as st
from io import  StringIO
#from strsimpy.jaro_winkler import JaroWinkler
from action import *
from TAKE_OUT_TYPE import *
import time
from datetime import datetime

now = datetime.now().strftime('%Y%m%d%H%M')


#jarowinkler = JaroWinkler()
endcoding = 'utf-8-sig'


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
        '選擇要清洗的欄位',
        (df.columns))
        
        time.sleep(2)
        st.write('你的清洗欄位', df[option_df])

        #將讀進來的資料統計
        df_count=df.groupby([option_df],sort=False)[option_df].count()
        df_count=df_count.to_frame(name='NUM')
        df_count.to_csv('TEMP.csv',encoding='utf-8-sig')
        df_count=pd.read_csv('TEMP.csv',encoding='utf-8-sig')
        df_count=df_count.sort_values('NUM',ascending=False)


        #st.dataframe(df_count)
        df[option_df]=df[option_df].astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

        genre = st.radio(
        "逗號切割，留下逗號前的字串[0]",
        ('YES', 'NO'))

        if genre == 'YES':
            df['Regex']=df[option_df].astype(str).str.partition(',')[0]
            df_count['Regex']=df_count[option_df].astype(str).str.partition(',')[0]
            
        else:
            df['Regex']=df[option_df]
            df_count['Regex']=df_count[option_df]
            

        st.write(df[[option_df,'Regex']])


        
        select_contorl=SELECT_CONTORLS # 增加功能到 action.py
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
            ['去除Corp類型', '去除Ltd類型', '去除LLC類型','去除THE、AND、OF','去除錯字(company、corp、kabusiki kaisha...)','去除有限合夥類型(gmbh & co. kg,Lp)','轉譯字符(&amp;)']
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
            if i=='轉譯字符(&amp;)':
                TAKE_OUT_WORDS.append(OTHERS)
            if i =='去除機構單位(GOVERMMENT、UNIVERSITY、SCHOOL、GROUP、FOUNDATION....)':
                TAKE_OUT_WORDS.append(ORG_UNIT)
            if i =='發明人名字清洗':
                TAKE_OUT_WORDS.append(INVENTER_NAME_CLEAN)
            if i=='去除國家':
                TAKE_OUT_WORDS.append(COUNTRY)

        
        time.sleep(5)

        TAKE_OUT_WORDS=sum(TAKE_OUT_WORDS,[])

        st.sidebar.write(TAKE_OUT_WORDS)

        df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        
        df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        
        st.write(df[[option_df,'Regex']])

        genre_4 = st.radio(
        "去除括弧之間所有文字(包含括弧)",
        ('YES', 'NO'))
        if genre_4 =='YES':
            df['Regex']=df['Regex'].str.replace(r'\(.*\)', '', regex=True)
            df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))

            df_count['Regex']=df_count['Regex'].str.replace(r'\(.*\)', '', regex=True)
            df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))

        else:
            df['Regex']=df['Regex']

            df_count['Regex']=df_count['Regex']

        st.write(df[[option_df,'Regex']])

        genre_1 = st.radio(
        "去除所有符號",
        ('YES', 'NO'))

        if genre_1 == 'YES':
            df['Regex']=df['Regex'].replace('[^A-Za-z0-9]+',' ',regex=True)
            df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
            
            df_count['Regex']=df_count['Regex'].replace('[^A-Za-z0-9]+',' ',regex=True)
            df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
            
        else:
            df['Regex']=df['Regex']

            df_count['Regex']=df_count['Regex']
            
        st.write(df[[option_df,'Regex']])

        genre_3 = st.radio(
        "去除所有數字",
        ('NO','YES'))

        if genre_3 == 'YES':
            df['Regex']=df['Regex'].apply(lambda x:''.join([i for i in x if not i.isdigit()]))

            df_count['Regex']=df_count['Regex'].apply(lambda x:''.join([i for i in x if not i.isdigit()]))
            

        else:
            df['Regex']=df['Regex']
            df_count['Regex']=df_count['Regex']
            

        st.write(df[[option_df,'Regex']])

        genre_2 = st.radio(
        "去除空格",
        ('YES', 'NO'))
        
        if genre_1 == 'YES':
            df['Regex']=df['Regex'].replace(' ','',regex=True)
            df_count['Regex']=df_count['Regex'].replace(' ','',regex=True)
              
        else:
            df['Regex']=df['Regex']
            df_count['Regex']=df_count['Regex']
            

        st.write(df[[option_df,'Regex']])


        st.write("補上因為正規化後全部被拿掉的空值")
        #補上正規化(regex)後為空白的欄位
        if len(df[df['Regex']==''])>0:
            list_index_DF=df[df['Regex']==''].index.tolist()
            for i in range(0,len(list_index_DF)):
                df['Regex'][list_index_DF[i]]=df[option_df].iloc[list_index_DF[i]]

        if len(df_count[df_count['Regex']==''])>0:
            list_index_DF=df_count[df_count['Regex']==''].index.tolist()
            for i in range(0,len(list_index_DF)):
                df_count['Regex'][list_index_DF[i]]=df_count[option_df].iloc[list_index_DF[i]]
        
        
        st.write(df[[option_df,'Regex']])

      
                
        if st.button('字串清理'):
            startTime = time.time()
            df_count=df_count.drop_duplicates(subset=['Regex'], keep='first')
            #st.write(df_count)
            with st.spinner('比對中請稍後...'):
                
                dict_db = dict(zip(df_count['Regex'],df_count[option_df]))
                df[option_df+'_Clean'] = df['Regex'].map(dict_db)

                if len(df[df[option_df+'_Clean'].isnull()])>0:
                    Index=df[df[option_df+'_Clean'].isnull()].index.tolist()
                    for i in range(0,len(Index)):
                        df[option_df+'_Clean'][Index[i]]=df[option_df].iloc[Index[i]]
                
                df.fillna(value='NULL', inplace=True)
                
                #t = time.time() - startTime

                st.write(df[[option_df,option_df+'_Clean']])
            

                st.balloons()
                time.sleep(1)
                

                df=df[[option_df,option_df+'_Clean']]
                df.to_csv('CompareTemp.csv',encoding=encoding)
                csv =convert_df(df)
                st.download_button(
                    label="下載 CSV",
                    data=csv,
                    file_name='權控清洗結果'+now+'.csv',
                    mime='text/csv',
                    )
                st.success('清洗完成，請下載')
else:
    uploaded_file= st.file_uploader("選擇 EXCEL 檔案",type='xlsx')
    if uploaded_file:
        df = pd.read_excel(uploaded_file,engine='openpyxl')
        
        st.write(df)


        option_df = st.selectbox(
        '選擇要比對的欄位',
        (df.columns))
        time.sleep(2)
        st.write('你的比對欄位', df[option_df])

        #將讀進來的資料統計
        df_count=df.groupby([option_df],sort=False)[option_df].count()
        df_count=df_count.to_frame(name='NUM')
        df_count.to_csv('TEMP.csv',encoding='utf-8-sig')
        df_count=pd.read_csv('TEMP.csv',encoding='utf-8-sig')
        df_count=df_count.sort_values('NUM',ascending=False)

        df[option_df]=df[option_df].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        

     
        genre = st.radio(
        "逗號切割，留下逗號前的字串[0]",
        ('YES', 'NO'))

        if genre == 'YES':
            df['Regex']=df[option_df].astype(str).str.partition(',')[0]
            df_count['Regex']=df_count[option_df].astype(str).str.partition(',')[0]
            
        else:
            df['Regex']=df[option_df]
            df_count['Regex']=df_count[option_df]
            

        st.dataframe(df[[option_df,'Regex']])

        select_contorl=SELECT_CONTORLS #增加功能到 action.py 
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
            ['去除Corp類型', '去除Ltd類型', '去除LLC類型','去除THE、AND、OF','去除錯字(company、corp、kabusiki kaisha...)','去除有限合夥類型(gmbh & co. kg,Lp)','轉譯字符(&amp;)']
        )

        time.sleep(5)
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
            if i =='轉譯字符(&amp;)':
                TAKE_OUT_WORDS.append(OTHERS)
            if i =='去除機構單位(GOVERMMENT、UNIVERSITY、SCHOOL、GROUP、FOUNDATION....)':
                TAKE_OUT_WORDS.append(ORG_UNIT)
            if i =='發明人名字清洗':
                TAKE_OUT_WORDS.append(INVENTER_NAME_CLEAN)
            if i=='去除國家':
                TAKE_OUT_WORDS.append(COUNTRY)

        TAKE_OUT_WORDS=sum(TAKE_OUT_WORDS,[])

        st.sidebar.write(TAKE_OUT_WORDS)

        df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        
        df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
        
        st.dataframe(df[[option_df,'Regex']])


        genre_4 = st.radio(
        "去除括弧之間所有文字(包含括弧)",
        ('YES', 'NO'))
        if genre_4 =='YES':
            df['Regex']=df['Regex'].str.replace(r'\(.*\)', '', regex=True)
            df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))

            df_count['Regex']=df_count['Regex'].str.replace(r'\(.*\)', '', regex=True)
            df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
            
        else:
            df['Regex']=df['Regex']

            df_count['Regex']=df_count['Regex']

        st.write(df[[option_df,'Regex']])


        genre_1 = st.radio(
        "去除所有符號",
        ('YES', 'NO'))

        if genre_1 == 'YES':
            df['Regex']=df['Regex'].replace('[^A-Za-z0-9]+',' ',regex=True)
            df['Regex']=df['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
            
            df_count['Regex']=df_count['Regex'].replace('[^A-Za-z0-9]+',' ',regex=True)
            df_count['Regex']=df_count['Regex'].apply(lambda x:' '.join(word.upper() for word in x.split() if word not in TAKE_OUT_WORDS))
            
        else:
            df['Regex']=df['Regex']

            df_count['Regex']=df_count['Regex']
            
        st.dataframe(df[[option_df,'Regex']])

        genre_3 = st.radio(
        "去除所有數字",
        ('NO','YES'))

        if genre_3 == 'YES':
            df['Regex']=df['Regex'].apply(lambda x:''.join([i for i in x if not i.isdigit()]))

            df_count['Regex']=df_count['Regex'].apply(lambda x:''.join([i for i in x if not i.isdigit()]))

        else:
            df['Regex']=df['Regex']
            df_count['Regex']=df_count['Regex']
            
        st.dataframe(df[[option_df,'Regex']])

        genre_2 = st.radio(
        "去除空格",
        ('YES', 'NO'))
        
        if genre_1 == 'YES':
            df['Regex']=df['Regex'].replace(' ','',regex=True)
            df_count['Regex']=df_count['Regex'].replace(' ','',regex=True)
             
        else:
            df['Regex']=df['Regex']
            df_count['Regex']=df_count['Regex']
            

        st.write(df[[option_df,'Regex']])

        st.write("補上因為正規化後全部被拿掉的空值")

        #補上正規化(regex)後為空白的欄位
        if len(df[df['Regex']==''])>0:
            list_index_DF=df[df['Regex']==''].index.tolist()
            for i in range(0,len(list_index_DF)):
                df['Regex'][list_index_DF[i]]=df[option_df].iloc[list_index_DF[i]]

        if len(df_count[df_count['Regex']==''])>0:
            list_index_DF=df_count[df_count['Regex']==''].index.tolist()
            for i in range(0,len(list_index_DF)):
                df_count['Regex'][list_index_DF[i]]=df_count[option_df].iloc[list_index_DF[i]]
        
        
        st.dataframe(df[[option_df,'Regex']])

      
                
        if st.button('字串清理'):
            startTime = time.time()
            df_count=df_count.drop_duplicates(subset=['Regex'], keep='first')
            
            #st.write(df_count)
            with st.spinner('清洗中請稍後...'):
                dict_db = dict(zip(df_count['Regex'],df_count[option_df])) 
                df[option_df+'_Clean'] = df['Regex'].map(dict_db)#完全比對

                if len(df[df[option_df+'_Clean'].isnull()])>0:
                    Index=df[df[option_df+'_Clean'].isnull()].index.tolist()
                    for i in range(0,len(Index)):
                        df[option_df+'_Clean'][Index[i]]=df[option_df].iloc[Index[i]]
        
                df.fillna(value='NULL', inplace=True)
            
                t = time.time() - startTime
            
                st.dataframe(df[[option_df,option_df+'_Clean']])
                #st.write(t)

                st.balloons()
                time.sleep(1)
                
                
                df=df[[option_df,'AC']]

                df.to_excel("CompareTemp.xlsx")
                excel =to_excel(df)
                st.download_button(
                     label="下載 EXCEL",
                     data=excel,
                     file_name='權控清洗結果'+now+'.xlsx'
                     )

                st.success('清洗完成，請下載')
