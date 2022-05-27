import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from app_edit import edit_txt

def run_chart() :

    df = pd.read_csv('data/Flight_Dataset.csv', index_col=0)
    
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


