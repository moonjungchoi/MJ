import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('MOONJUNG π ')

def  plotting_demo():
    
    #uploaded_file = st.file_uploader("Choose a file")

   #money=pd.read_csv(uploaded_file)
    money = pd.read_csv("money_data7.csv")

    option = st.selectbox(
        'How would you like to choice year ?',
        ('2020', '2021', '2022'))

    option2 = int(option)

    st.write('You selected:', option)

    money = money[:] [money['A_YEAR']== option2]
   
    global  aa
   
    aa = money


    fig, ax = plt.subplots(2,2, figsize=(12,8))

    plt.subplot(221)
    plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='purple' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('America rate')


    plt.subplot(222)
    plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='pink' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Korea rate')

    plt.subplot(223)
    plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='green' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Kospi Rate')

    plt.subplot(224)
    plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('House Price')

    st.pyplot(fig)
    #st.dataframe(money)
       

def bar_chart():

    url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="

    years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]

    df = pd.DataFrame([]) 

    for    i    in     years: 
        df1 = pd.read_html( url + i  )[0]
        df1['λλ'] =  i 
        df = pd.concat([df, df1], axis=0)
        
    baseball = df    

    baseball.ν.replace({'λμ°':'Dusan','μΌμ±':'SS','ν€μ':'KU','νν': 'HH','λ‘―λ°':'Lotte','λ₯μΌ':'NecSen'}, inplace=True)
    
    option = st.selectbox(
        'How would you like to choice year ?',
        ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))

    option2 = option

    st.write('You selected:', option)

    df7  =  baseball[:] [ baseball.λλ==option2 ]
    x = df7.ν
    y = df7.μΉλ₯ 
    
    global  bb
   
    bb = baseball

    
    fig, ax = plt.subplots(figsize=(12,8))

    colors = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7' ,'C8', 'C9', 'C10' ]
    plt.bar(  x,  y,  color= colors ) 

    for   num ,   v    in   enumerate( y ):
        plt.text (  num -0.4  ,   v + 0.01 ,  v   )

    plt.title( "year korea baseball winrate data", position=(0.5,1.1))
    st.pyplot(fig)
    #st.dataframe(df7)

        

with st.form(key ='Form1'):
    with st.sidebar:
        
        select_language = st.sidebar.radio('λ°μ΄ν° λΆμ κ²°κ³Ό', ('κΈλ¦¬ & μ§κ°', 'KBO μΌκ΅¬ μμ & μΉλ₯ ', 'λ€λ₯Έ λ°μ΄ν° λΆμ'))
        
        
if select_language =='κΈλ¦¬ & μ§κ°':  
  tab1, tab2 = st.tabs(["π Chart", "π Data"])
   
  with tab1:
        tab1.subheader("μ°¨νΈλ‘ λ³΄κΈ°")
        plotting_demo()
        
  with tab2:
        tab2.subheader("λ°μ΄ν°λ‘ λ³΄κΈ°")
        st.dataframe(aa)
  
  

        
elif select_language =='KBO μΌκ΅¬ μμ & μΉλ₯ ':
 tab1, tab2 = st.tabs(["π Chart", "π Data"])

 with tab1:
    tab1.subheader("μ°¨νΈλ‘ λ³΄κΈ°")
    bar_chart()

 with tab2:
    tab2.subheader("λ°μ΄ν°λ‘ λ³΄κΈ°")
    st.dataframe(bb)
  
