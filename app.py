import streamlit as st
from home import run_home
from df import run_df

def main():
    st.title('지역별 상담 유형 데이터')
    
    menu = ['Home','df']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == menu[0]:
        run_home()
        
    if choice == menu[1]:
        run_df()    


if __name__ == '__main__':
    main()