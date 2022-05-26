import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# plt 한글 사용
matplotlib.rcParams['font.family'] ='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] =False

def run_eda() :
    st.subheader('데이터 분석 페이지입니다.')

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

    # 가장 많이 사용하는 항공사
    fig3 = plt.figure()
    airline_order = df['airline'].value_counts()
    plt.bar(df.airline.unique(), df.airline.value_counts())
    plt.title('가장 많이 사용하는 항공사')
    st.pyplot(fig3)

    # 가장 많은 출발 시간 대
    fig2 = plt.figure(figsize=(8,5))
    sns.countplot(data=df, x='departure_time', order=df['departure_time'].value_counts().index)
    plt.title('가장 많은 출발 시간')
    st.pyplot(fig2)
