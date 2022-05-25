import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    st.subheader('데이터 분석 페이지입니다.')

    st.write('항공권 데이터')
    df = pd.read_csv('data/Flight_Dataset.csv', index_col=0)
    st.dataframe(df)


    col_list = df.columns.to_list()
    col_choice = st.multiselect('보고싶은 데이터의 컬럼을 선택하세요.', col_list)
    if len(col_choice) != 0 :
        st.dataframe(df[col_choice])

    st.write('데이터 통계량')
    st.dataframe(df.describe())


    st.write('컬럼들 간의 상관계수 확인하기')
    cor_list = ['stops', 'class', 'duration', 'days_left', 'price']
    selected_list = st.multiselect('컬럼을 2개 이상 선택하세요', cor_list)
   
    if len(selected_list) > 1 :

        st.write('선택하신 컬럼끼리의 상관계수입니다.')
        st.dataframe(df[selected_list].corr())

        fig = plt.figure()
        sns.heatmap(data=df[selected_list].corr(), annot=True, 
                    fmt='.2f', vmin=-1, vmax=1, cmap='GnBu', linewidths=0.5)
        st.pyplot(fig)