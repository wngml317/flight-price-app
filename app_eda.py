import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def run_eda() :
    st.subheader('데이터 분석 페이지')
    st.write('')
    df = pd.read_csv('data/Flight_Dataset.csv', index_col=0)

    st.markdown("##### 데이터 통계량")
    with st.expander('데이터 통계량 확인하기') : 
        st.dataframe(df.describe())

    st.write('')
    
    st.markdown("##### 선택한 컬럼 별 데이터 확인")
    col_list = df.columns.to_list()
    col_choice = st.multiselect('보고싶은 데이터의 컬럼을 선택하세요.', col_list)
    if len(col_choice) != 0 :
        st.dataframe(df[col_choice])
    

    st.write('')
    st.markdown('##### 가격이 제일 비싼 항공권 데이터')
    df_max = df.loc[df['price'] == df['price'].max(), ]
    st.dataframe(df_max)

    st.write('')
    st.markdown('##### 가격이 제일 저렴한 항공권 데이터')
    df_min = df.loc[df['price'] == df['price'].min(), ]
    st.dataframe(df_min)



