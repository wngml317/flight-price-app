import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def run_eda() :
    st.subheader('데이터 분석 페이지입니다.')

    with st.expander('항공권 데이터 정보 확인하기'):
        st.markdown("##### 📑 데이터 정보")
        st.markdown("- airline : 항공사 이름, 6개의 다른 항공사\n"
                    "- flight : 비행 코드\n"
                    "- source_city : 항공편이 출발하는 도시, 6개의 고유한 도시\n"
                    "- departure_time : 출발 시간, 기간을 빈으로 그룹화하여 생성 한 6개의 고유한 시간 레이블\n"
                    "- stops : 출발지와 목적지 도시 간의 경유지 수를 저장하는 3개의 고유한 값\n"
                    "(* 2개 이상인 경유지는 2로 처리하였다.)\n"
                    "- arrival_time : 도착 시간, 시간 간격을 빈으로 그룹화하여 생성한 6개의 고유한 시간 레이블\n"
                    "- destination_city : 목적지 도시, 항공편이 착륙할 6개의 고유한 도시\n" 
                    "- class : 좌석 클래스, 비즈니스와 이코노미\n"
                    "- duration : 소요 시간, 도시 간 이동에 걸리는 전체 시간을 시간 단위로 표시\n"  
                    "- days_left : 여행일에서 예약일을 뺀 남은 일수\n"
                    "- price : 티켓 가격 정보\n")

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
    st.markdown('##### 가격이 제일 비싼 항공권 데이터')
    df_max = df.loc[df['price'] == df['price'].max(), ]
    st.dataframe(df_max)

    st.write('')
    st.markdown('##### 가격이 제일 저렴한 항공권 데이터')
    df_min = df.loc[df['price'] == df['price'].min(), ]
    st.dataframe(df_min)



