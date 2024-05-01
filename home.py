import streamlit as st

def run_home():
    st.subheader('지역별, 상담유형별 데이터를 알아보자')
    
    st.text("'한국청소년활동진흥원'에서 제공한")
    st.text('지역별 상담 유형 통계 정보(2019).csv 파일과')
    st.text('지역별 상담 유형 통계 정보(2020).csv 파일을 통해 만들어졌습니다')
    st.link_button('해당 데이터셋은 이 곳에서 받았습니다','https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=6aa14c34-4866-4a3f-9223-09c12d58ad4b')
    st.image('./image/consulting.png',use_column_width = True)