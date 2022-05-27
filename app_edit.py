import streamlit as st
import urllib


def edit_txt(txt) : 
    html_temp  = f"""
    <h5 style = "text_align:center; font-weight: bold;"> {txt} </h5>
    """
    st.markdown(html_temp, unsafe_allow_html = True)


def col_content(txt) : 
    html_temp  = f"""
    <h5 style = "text_align:center; font-weight: bold;"> 📑 데이터 정보
- airline : 항공사 이름, 6개의 다른 항공사.

- flight : 비행 코드

- source_city : 항공편이 출발하는 도시, 6개의 고유한 도시

- departure_time : 출발 시간, 기간을 빈으로 그룹화하여 생성 한 6개의 고유한 시간 레이블

- stops : 출발지와 목적지 도시 간의 경유지 수를 저장하는 3개의 고유한 값 
  (* 2개 이상인 경유지는 2로 처리하였다.)

- arrival_time : 도착 시간, 시간 간격을 빈으로 그룹화하여 생성한 6개의 고유한 시간 레이블

- destination_city : 목적지 도시, 항공편이 착륙할 6개의 고유한 도시

- class : 좌석 클래스, 비즈니스와 이코노미

- duration : 소요 시간, 도시 간 이동에 걸리는 전체 시간을 시간 단위로 표시

- days_left : 여행일에서 예약일을 뺀 남은 일수

- price : 티켓 가격 정보 </h5>
    """
    st.markdown(html_temp, unsafe_allow_html = True)


      