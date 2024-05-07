import streamlit as st

def run_home():
    st.subheader('지역별, 상담유형별로 청소년 고민상담 현황을 알아보자')
    
    st.markdown("'한국청소년활동진흥원'에서 제공한")
    st.markdown('지역별 상담 유형 통계 정보(2019).csv 파일을 통해 만들어졌습니다')
    st.link_button('해당 데이터셋은 이 곳에서 받았습니다','https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=6aa14c34-4866-4a3f-9223-09c12d58ad4b')
    st.markdown('데이터 설명 : 청소년 상담시 청소년들이 주로 물어보는 카테고리의 지역별 건수')
    st.markdown('활용분야 : 특정지역의 청소년들이 고민하는 유형을 분석하여 정책 방향 및 전문 상담사 배정시 활용')
    st.image('./image/consulting.png',use_column_width = True)