import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import font_manager, rc
import plotly.express as px


# 한글 폰트 설정
font_path = "./data/NANUMGOTHIC.TTF"  # 한글 폰트 경로 
# 윈도우에 있는 기본 폰트로 하려 했으나 설정이 다른 컴퓨터에서 해본 결과
# 폰트를 찾지 못하는 일이 발생하여 data 폴더 안에 폰트를 하나 넣었다
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


def run_eda():
    
    st.subheader('데이터프레임 확인하기')
    df = pd.read_csv('./data/youth_consulting.csv', index_col=0)
    #print(df)
    
    st.dataframe(df)

    st.subheader('상담유형별 지역데이터의 시각화')
    st.text('상담유형을 선택하면 지역별 데이터를 보여드립니다.')
    
    available_columns = [col for col in df.columns if col not in ['지역', '합계']] # 컬럼 선택시 지역과 합계는 제외
    selected_columns = st.multiselect('상담 유형을 선택하세요', available_columns)

    df_filtered = df[df['지역'] != '전국'] # 지역 컬럼에서의 전국 데이터는 제외한 지역리스트

    if selected_columns:
        # 선택한 컬럼과 '지역' 컬럼의 데이터 시각화
        for column in selected_columns:
            # 바 차트 그리기
            sorted_df = df_filtered.sort_values(by=column, ascending=False) # 선택한 컬럼의 데이터 내림차순
            fig_bar = px.bar(sorted_df, x='지역', y=column, title=f'{column} 관련 유형의 지역별 상담 수')
            st.plotly_chart(fig_bar)

            # 파이 차트 그리기
            fig_pie = px.pie(df_filtered, names='지역', values=column, title=f'{column} 관련 유형 의 지역별 Pie 차트', hole=0.2,)
            st.plotly_chart(fig_pie)
    else:
        st.error('상담유형을 선택해주세요.')

    

    #-----------------------------------------------------------
    st.subheader('지역별 상담유형 데이터와 시각화')
    st.text('지역을 선택하면 상담유형별 데이터를 보여드립니다.')
    st.text('2개 이상 선택시 결과는 합산해서 보여집니다')
    choice_list = st.multiselect('지역을 선택하세요', df['지역'])
    if choice_list :
        selected_rows = df[df['지역'].isin(choice_list)]
        st.write(selected_rows)

        combined_data = selected_rows.drop(columns=['지역', '합계']).sum(axis=0)

        max_value = combined_data.max()
        min_value = combined_data.min()
        max_column = combined_data.idxmax()
        min_column = combined_data.idxmin()

        st.success(f"선택한 지역의 가장 많은 유형은 : {max_column} 관련의 상담으로 {format(max_value, ',')} 건 입니다.")
        st.warning(f"선택한 지역의 가장 적은 유형은 : {min_column} 관련의 상담으로 {format(min_value, ',')} 건 입니다.")

        st.subheader('시각화')
        st.text('위에서 선택한 지역을 차트로 확인하자')

        labels = combined_data.index.tolist()
        values = combined_data.values.tolist()

        # 바 차트 그리기
        sorted_values = sorted(values, reverse=True)
        sorted_labels = [x for _, x in sorted(zip(values, labels), reverse=True)]
        fig1 = px.bar(x=sorted_labels, y=sorted_values, title=f'{", ".join(choice_list)} 의 상담 유형 Bar 차트')
        st.plotly_chart(fig1)

        # 파이차트로 그려보자
        fig2 = px.pie(names=labels, values=values, title=f'{", ".join(choice_list)} 의 상담 유형 Pie 차트', hole=0.2)
        st.plotly_chart(fig2)    


    else:
        st.error('지역을 선택해주세요.')
    