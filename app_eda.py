from pyparsing import col
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import plotly.express as px

from app_edit import edit_txt

def run_eda() :
    st.subheader('데이터 분석 페이지입니다.')

    with st.expander('항공권 데이터 정보 확인하기'):
        st.markdown()

    with st.expander('항공권 데이터 확인하기'):
        df = pd.read_csv('data/Flight_Dataset.csv', index_col=0)
        st.dataframe(df)

    with st.expander('데이터 통계량 확인하기') : 
        st.dataframe(df.describe())

    st.write('')
    col_list = df.columns.to_list()
    col_choice = st.multiselect('보고싶은 데이터의 컬럼을 선택하세요.', col_list)
    if len(col_choice) != 0 :
        st.dataframe(df[col_choice])
    

    st.write('')
    edit_txt('가격이 제일 비싼 항공권 데이터')
    df_max = df.loc[df['price'] == df['price'].max(), ]
    st.dataframe(df_max)

    st.write('')
    edit_txt('가격이 제일 저렴한 항공권 데이터')
    df_min = df.loc[df['price'] == df['price'].min(), ]
    st.dataframe(df_min)


    st.write('')
    edit_txt('컬럼들 간의 상관계수 확인하기')
    cor_list = ['stops', 'class', 'duration', 'days_left', 'price']
    selected_list = st.multiselect('컬럼을 2개 이상 선택하세요', cor_list)
   
    if len(selected_list) > 1 :

        st.write('선택하신 컬럼끼리의 상관계수입니다.')
        st.dataframe(df[selected_list].corr())

        fig = plt.figure()
        sns.heatmap(data=df[selected_list].corr(), annot=True, 
                    fmt='.2f', vmin=-1, vmax=1, cmap='GnBu', linewidths=0.5)
        st.pyplot(fig)


    
    airline_sorted = df['airline'].value_counts()
    fig1 = px.bar(airline_sorted, title='가장 많이 사용하는 항공사')
    st.plotly_chart(fig1)

    dep_sorted = df['departure_time'].value_counts()
    fig2 = px.bar(dep_sorted, title='가장 많은 출발 시간 대')
    st.plotly_chart(fig2)


