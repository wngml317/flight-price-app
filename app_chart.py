import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def run_chart() :

    df = pd.read_csv('data/Flight_Dataset.csv', index_col=0)
    
    st.write('')
    st.markdown('##### 컬럼들 간의 상관계수 확인하기')
    col_list = ['stops', 'class', 'duration', 'days_left', 'price']
    selected_list = st.multiselect('컬럼을 2개 이상 선택하세요', col_list)
   
    if len(selected_list) > 1 :

        st.write('선택하신 컬럼끼리의 상관계수입니다.')
        st.dataframe(df[selected_list].corr())

        fig = plt.figure()
        sns.heatmap(data=df[selected_list].corr(), annot=True, 
                    fmt='.2f', vmin=-1, vmax=1, cmap='RdPu', linewidths=0.5)
        st.pyplot(fig)

    st.write('')

    with st.expander('📌 가장 많이 이용하는 항공사 확인하기') : 
        airline_sorted = df['airline'].value_counts()
        df_airline = pd.DataFrame({'airline' : airline_sorted.index, 'values' : airline_sorted.values})
        fig1 = px.bar(df_airline, x='airline', y='values')
        st.plotly_chart(fig1)



    with st.expander('📌 가장 많은 출발 시간 대 확인하기') : 
        dep_sorted = df['departure_time'].value_counts()
        df_dep = pd.DataFrame({'departure_time' : dep_sorted.index, 'values' : dep_sorted.values})
        fig2 = px.bar(df_dep, x='departure_time', y='values')
        st.plotly_chart(fig2)


