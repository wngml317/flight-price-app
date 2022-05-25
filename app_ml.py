import streamlit as st
import joblib

def run_ml() :
    st.subheader('항공권 가격 예측 페이지입니다.')

    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')

    airline_list = ['SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India']
    airline = st.selectbox('항공선을 선택해주세요', airline_list)

    stops = st.number_input('출발지와 목적지 도시 간의 경유지 수', min_value=0)

    seat_class = st.radio('좌석 클래스를 선택해주세요.', ['Economy', 'Bussiness'])