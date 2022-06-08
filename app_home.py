import streamlit as st
import pandas as pd


def run_home() :
    st.markdown('#### 항공권 예약 데이터 셋을 분석하여 가격을 예측한 앱')
    st.write('')
    st.markdown('##### 항공권 데이터 정보')
    with st.expander('항공권 데이터 정보 확인하기'):
        st.markdown("##### 📑 데이터 정보")
        st.markdown("- airline : 항공사 이름, 6개의 다른 항공사\n"
                    "- flight : 비행 코드\n"
                    "- source_city : 항공편이 출발하는 도시, 6개의 고유한 도시\n"
                    "- departure_time : 출발 시간, 기간을 그룹화하여 생성 한 6개의 고유한 시간\n"
                    "- stops : 출발지와 목적지 도시 간의 경유지 수\n"
                    "  - 2개 이상인 경유지는 2로 처리 \n "
                    "- arrival_time : 도착 시간, 기간을 그룹화하여 생성한 6개의 고유한 시간\n"
                    "- destination_city : 목적지 도시, 항공편이 착륙할 6개의 고유한 도시\n" 
                    "- class : 좌석 클래스, 비즈니스와 이코노미\n"
                    "  - 비즈니스 : 1\n"
                    "  - 이코노미 : 0 \n "
                    "- duration : 소요 시간, 도시 간 이동에 걸리는 전체 시간을 시간 단위로 표시\n"  
                    "- days_left : 여행일에서 예약일을 뺀 남은 일수\n"
                    "- price : 티켓 가격 정보\n")
    
    st.write('')

    st.markdown('##### 항공권 데이터')
    df = pd.read_csv('data/Flight_Dataset.csv', index_col=0)
    st.dataframe(df)
