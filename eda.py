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

    st.subheader('청소년 고민상담유형 차트 1')
    st.markdown('상담유형을 선택하면 선택한 상담유형만의 데이터프레임과 함께')
    st.markdown('해당 유형이 가장 많은 지역순과 백분율로 보여드립니다.')
    st.markdown('2개 이상 선택시 선택한 상담수를 합산하여 지역별 그래프를 추가로 보여드립니다')
    st.markdown('줌인 줌아웃이 가능하며 원형 그래프의 경우')
    st.markdown('우측의 원하는 항목을 제거하거하거나 되돌릴 수 있습니다.')
    
    
    available_columns = [col for col in df.columns if col not in ['지역', '합계']] # 컬럼 선택시 지역과 합계는 제외
    selected_columns = st.multiselect('상담 유형을 선택하세요', available_columns)

    df_filtered = df[df['지역'] != '전국'] # 지역 컬럼에서의 전국 데이터는 제외한 지역리스트


    if selected_columns:
        # 선택된 컬럼의 데이터프레임 생성
        selected_df = df_filtered[selected_columns + ['지역']]
        selected_df.set_index('지역', inplace=True)
        st.write(selected_df)

        # 선택된 컬럼이 2개 이상인 경우의 차트 생성
        if len(selected_columns) >= 2:
            # 선택된 을 합산하여 새로운 컬럼 생성
            selected_df['합산'] = selected_df[selected_columns].sum(axis=1)

            # 바 차트 그리기 ( 합산)
            selected_df = selected_df.sort_values(by='합산', ascending=False)
            fig_bar1 = px.bar(selected_df, x=selected_df.index, y='합산', title=f'{", ".join(selected_columns)} 고민상담수 총합')
            st.plotly_chart(fig_bar1)

            # 파이 차트 그리기 ( 합산 비율)
            fig_pie1 = px.pie(selected_df, names=selected_df.index, values='합산', title=f'{", ".join(selected_columns)} 고민상담의 지역 비율', hole=0.2)
            st.plotly_chart(fig_pie1)

        # 선택된 컬럼들의 각각의 차트 생성
        for column in selected_columns:
            # 바 차트 그리기
            sorted_df = df_filtered.sort_values(by=column, ascending=False)
            fig_bar = px.bar(sorted_df, x='지역', y=column, title=f'지역별 {column} 고민 상담 수')
            st.plotly_chart(fig_bar)

            # 파이 차트 그리기
            fig_pie = px.pie(df_filtered, names='지역', values=column, title=f'{column} 고민상담의 지역 비율', hole=0.2)
            st.plotly_chart(fig_pie)

    # 선택된 컬럼이 없는 경우 에러 메시지 출력
    else:
        st.error('상담 유형을 선택해주세요.')


    
    #-----------------------------------------------------------
    
    st.subheader('청소년 고민상담유형 차트 2')
    st.markdown('지역을 선택하면 선택한 데이터프레임과 함께')
    st.markdown('가장 많은 고민상담유형순서와 고민상담유형의 비율을 보여드립니다.')
    st.markdown('2개 이상 선택시 결과는 합산해서 보여집니다.')
    st.markdown('줌인 줌아웃이 가능하며 원형 그래프의 경우')
    st.markdown('원하는 항목을 제거하거하거나 되돌릴 수 있습니다.')
    
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
        fig1 = px.bar(x=sorted_labels, y=sorted_values, title=f'{", ".join(choice_list)} 의 고민상담 수')
        st.plotly_chart(fig1)

        # 파이차트로 그려보자
        fig2 = px.pie(names=labels, values=values, title=f'{", ".join(choice_list)} 의 고민상담 비율', hole=0.2)
        st.plotly_chart(fig2)    


    else:
        st.error('지역을 선택해주세요.')
    
