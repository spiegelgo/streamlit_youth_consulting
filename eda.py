import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib import font_manager, rc
import plotly.express as px




def run_eda():
    
    # 한글 폰트 설정
    import platform
    from matplotlib import font_manager, rc
    plt.rcParams['axes.unicode_minus'] = False
    if platform.system() == 'Linux':
        rc('font', family='NanumGothic')
            
    st.subheader('전체 데이터프레임 확인')
    df = pd.read_csv('./data/youth_consulting.csv', index_col=0)
    st.dataframe(df)

    st.subheader('상담유형별 지역순 시각화')
    st.text('상담유형을 선택하면 데이터프레임과 함께')
    st.text('해당 유형이 가장 많은 지역순과 백분율로 보여드립니다.')
    st.text('줌인 줌아웃이 가능하며 원형 그래프의 경우 우측의 원하는 항목을 제거하거하거나 되돌릴 수 있습니다.')
    
    
    available_columns = [col for col in df.columns if col not in ['지역', '합계']] # 컬럼 선택시 지역과 합계는 제외
    selected_columns = st.multiselect('상담 유형을 선택하세요', available_columns)

    df_filtered = df[df['지역'] != '전국'] # 지역 컬럼에서의 전국 데이터는 제외한 지역리스트
    # 선택한 '상담유형'의 데이터프레임 출력
    if selected_columns:
        selected_df = df_filtered[selected_columns + ['지역']]  # '지역' 열을 포함하여 선택된 열만 필터링
        selected_df.set_index('지역', inplace=True)  # '지역'을 인덱스로 설정
        st.write(selected_df)
        st.subheader('시각화')

        # 선택한 컬럼과 '지역' 컬럼의 데이터 시각화
        for column in selected_columns:
            # 바 차트 그리기
            sorted_df = df_filtered.sort_values(by=column, ascending=False) # 선택한 컬럼의 데이터 내림차순
            fig_bar = px.bar(sorted_df, x='지역', y=column,  title=f'{column} 상담 수')
            st.plotly_chart(fig_bar)

            # 파이 차트 그리기
            fig_pie = px.pie(df_filtered, names='지역', values=column, title=f'{column} 상담의 지역 백분율', hole=0.2,)
            st.plotly_chart(fig_pie)
    else:
        st.error('상담유형을 선택해주세요.')

    
    #-----------------------------------------------------------
    
    st.subheader('지역별 상담유형순 시각화')
    st.text('지역을 선택하면 선택한 데이터프레임과 함께')
    st.text('가장 많은 상담유형순서와 백분율로 보여드립니다.')
    st.text('2개 이상 선택시 결과는 합산해서 보여집니다.')
    st.text('줌인 줌아웃이 가능하며 원형 그래프의 경우 우측의 원하는 항목을 제거하거하거나 되돌릴 수 있습니다.')
    
    choice_list = st.multiselect('지역을 선택하세요', df['지역'])
    if choice_list :
        selected_rows = df[df['지역'].isin(choice_list)]
        st.write(selected_rows)

        combined_data = selected_rows.drop(columns=['지역', '합계']).sum(axis=0)


        st.subheader('시각화')

        labels = combined_data.index.tolist()
        values = combined_data.values.tolist()

        # 바 차트 그리기
        sorted_values = sorted(values, reverse=True)
        sorted_labels = [x for _, x in sorted(zip(values, labels), reverse=True)]
        fig1 = px.bar(x=sorted_labels, y=sorted_values, title=f'{", ".join(choice_list)} 의 상담수')
        st.plotly_chart(fig1)

        # 파이차트로 그려보자
        fig2 = px.pie(names=labels, values=values, title=f'{", ".join(choice_list)} 의 상담 백분율', hole=0.2)
        st.plotly_chart(fig2)    


    else:
        st.error('지역을 선택해주세요.')
    
