import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import font_manager, rc
import plotly.express as px


# 한글 폰트 설정
font_path = "C:/Windows/Fonts/H2GTRE.ttf"  # 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


def run_df():
    
    st.subheader('데이터프레임 확인하기')
    df = pd.read_csv('./data/youth_consulting.csv', index_col=0)
    #print(df)
    st.text('컬럼을 누르면 각각 최소값부터, 최대값부터 확인 가능합니다.')
    st.dataframe(df)
    
    st.subheader('지역별 최소, 최대 유형')
    st.text('지역을 선택하면 지역별로 볼 수 있습니다.')
    choice_list = st.multiselect('지역을 선택하세요', df['지역'])
    if choice_list :
        selected_rows = df[df['지역'].isin(choice_list)]
        st.write(selected_rows)
        
        max_values = selected_rows.drop(columns=['지역', '합계']).max()
        min_values = selected_rows.drop(columns=['지역', '합계']).min()
        max_column = max_values.idxmax()
        max_value = max_values[max_column]
        min_column = min_values.idxmin()
        min_value = min_values[min_column]
        
        st.info(f"가장 많은 유형은 : {max_column} 관련의 상담으로 {format(max_value, ',')} 건 입니다.")
        st.warning(f"가장 적은 유형은 : {min_column} 관련의 상담으로 {format(min_value, ',')} 건 입니다.")

        
        st.subheader('시각화')
        st.text('위에서 선택한 지역을 차트로 확인하자')
        
        if not selected_rows.empty:
            labels = selected_rows.drop(columns=['지역', '합계']).columns.tolist()
            values = selected_rows.drop(columns=['지역', '합계']).values.tolist()[0]
            
            # 바 차트 그리기
            sorted_values = sorted(values, reverse=True)
            sorted_labels = [x for _,x in sorted(zip(values,labels), reverse=True)]
            fig1 = px.bar(x=sorted_labels, y=sorted_values, title='상담 유형 Bar 차트')
            st.plotly_chart(fig1)

            
            # 파이차트로 그려보자
            fig2 = px.pie(names=labels, values=values, title='상담 유형 Pie 차트', hole=0.2)

            st.plotly_chart(fig2)
    else:
        pass
    
