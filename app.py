import streamlit as st
from home import run_home
from eda import run_eda

def main():
    st.title('청소년 고민 상담 유형 분석')
    
    menu = ['Home','EDA']
    choice = st.sidebar.selectbox('메뉴',menu)
    
    if choice == menu[0]:
        run_home()
        
    if choice == menu[1]:
        run_eda()    


if __name__ == '__main__':
    main()