
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime 
from datetime import date

def run_ml() :
    st.subheader('항공권 가격 예측 페이지입니다.')

    df = pd.read_csv('data/Flight_Dataset.csv')

    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')
    ct = joblib.load('data/ct.pkl')


    airline_list = list(df['airline'].unique())
    airline = st.selectbox('항공선을 선택해주세요', airline_list)
    st.write('')

    # 경유지 수의 최소값을 0으로 설정해준다.
    stops = st.number_input('출발지와 목적지 도시 간의 경유지 수', min_value=0, max_value=5)
    st.write('')

    seat_choice = st.radio('좌석 클래스를 선택해주세요.', ['Economy', 'Business'])
    if seat_choice == 'Economy' :
        seat = 0 
    elif seat_choice == 'Business' :
        seat = 1
    st.write('')

    dep_list = list(df['source_city'].unique())
    arr_list = list(df['destination_city'].unique())

    day = st.date_input("날짜를 선택해주세요.", min_value = date.today())
    today = date.today()
    days_left = (day-today).days
    

    st.markdown('##### 출발 / 도착 정보')
    cols = st.columns((1,1))
    dep_city = cols[0].selectbox('출발 도시를 선택하세요.', dep_list)
    arr_city = cols[1].selectbox('도착 도시를 선택하세요.', arr_list)
    
    # 출발 도시와 도착 도시를 똑같이 선택했을 경우 : Error
    if dep_city == arr_city :
        st.error('Error :: 서로 다른 도시를 선택해주세요')
    
    else :

        # 지속시간 : 출발 도시와 도착 도시, 경유 수를  구한 후, 지속시간의  평균을 구한다. 
        duration = df.loc[(df['source_city'] == dep_city) & (df['destination_city'] == arr_city) & (df['stops'] == stops), 'duration']
        duration = round(duration.mean(), 2)
        st.write('')


        # 도착 시간은 구한 지속시간을 출발 시간에 더해준다.
        dep_time = cols[0].time_input("출발 시간", datetime.time())
        
        # 구한 지속 시간에서 시, 분을 구하고
        dur_H = int(duration)
        dur_M = int(round((duration - dur_H) * 100, -1))

        # 출발 시간의 시, 분과 더하여 도착 시간을 구한다.
        arr_H = dep_time.hour + dur_H
        arr_M = dep_time.minute + dur_M
        
        # 분 단위가 60을 넘을 경우 시간을 다시 계산해준다.
        if arr_M >= 60 :
            arr_H = arr_H + (arr_M//60)
            arr_M = arr_M % 60
            arr_time = datetime.time(arr_H, arr_M)
        else :
            arr_time = datetime.time(arr_H, arr_M)
        
        cols[1].text_input("도착 시간", arr_time, disabled=True)
    
    


        if st.button('예측 시작하기') :
            new_data = np.array([airline, stops, seat, duration, days_left])
            
            print(new_data)
            new_data = new_data.reshape(1, 5)
            new_data = ct.transform(new_data)

            new_data = scaler_X.transform(new_data)

            y_pred = regressor.predict(new_data)

            y_pred = scaler_y.inverse_transform(y_pred)
            y_pred = round(y_pred[0,0])

            st.write('')
            st.info("예측한 항공권 가격은 " + str(y_pred) + "달러 입니다.")
    
