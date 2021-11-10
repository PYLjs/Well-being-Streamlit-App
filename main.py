import streamlit as st
import pandas as pd
import numpy as np
import pickle


df=pd.read_csv('wellbeing.csv')
model=pickle.load(open('wellbeing.pkl','rb'))

def preprocess(FRUITS_VEGGIES,DAILY_STRESS,PLACES_VISITED,CORE_CIRCLE,SUPPORTING_OTHERS,SOCIAL_NETWORK,ACHIEVEMENT,DONATION,BMI_RANGE,TODO_COMPLETED,FLOW,DAILY_STEPS,LIVE_VISION,SLEEP_HOURS,LOST_VACATION,DAILY_SHOUTING,SUFFICIENT_INCOME,PERSONAL_AWARDS,TIME_FOR_PASSION,WEEKLY_MEDITATION,AGE,GENDER):
    if AGE=="Less than 20":
        AGE=int(0)
    elif AGE=="21 to 35":
        AGE=int(1)
    elif AGE =="36 to 50":
        AGE=int(2)
    else:
        AGE=int(3)

    if GENDER =="Male":
        GENDER=int(0)
    else:
        GENDER=int(1)



    user_input = [FRUITS_VEGGIES,DAILY_STRESS,PLACES_VISITED,CORE_CIRCLE,SUPPORTING_OTHERS,SOCIAL_NETWORK,ACHIEVEMENT,DONATION,BMI_RANGE,TODO_COMPLETED,FLOW,DAILY_STEPS,LIVE_VISION,SLEEP_HOURS,LOST_VACATION,DAILY_SHOUTING,SUFFICIENT_INCOME,PERSONAL_AWARDS,TIME_FOR_PASSION,WEEKLY_MEDITATION,AGE,GENDER]
    user_input = np.array(user_input)
    user_input = user_input.reshape(1, -1)

    prediction = model.predict(user_input)

    return prediction


html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Well-Being and Life Balance App</h1> 
    </div> 
    """

st.markdown(html_temp, unsafe_allow_html=True)
st.image("life-balance.jpg")
st.subheader('by Paul-Yuthi Lajus ')

GENDER = st.selectbox('Your gender:',('Male','Female'))
AGE = st.selectbox('How old are you?',('Less than 20','21 to 35','36 to 50','51 or more'))
FRUITS_VEGGIES = st.slider('How many fruits or vegetables do you eat everyday? (From 0 to 5+)',0,5,0)
DAILY_STRESS = st.slider('How much stress do you typically experience everyday?',0,5,0)
PLACES_VISITED = st.slider('How many new places do you visit each year? (Average from 0 to 10+)',0,10,0)
CORE_CIRCLE = st.slider('How many people are very close to you? (From 0 to 10+)',0,10,0)
SUPPORTING_OTHERS = st.slider('How many people do you help achieve a better life? (From 0 to 10+)',0,10,0)
SOCIAL_NETWORK = st.slider('With how many people do you interact with during a typical day? (Average from 0 to 10+)',0,10,0)
ACHIEVEMENT = st.slider('How many remarkable achievements are you proud of? (From 0 to 10+)',0,10,0)
DONATION = st.slider('How many times do you donate your time or money to good causes each year? (Average from 0 to 5+)',0,5,0)
BMI_RANGE = st.selectbox('What is your body mass index range? (1 if healthy weight, 2 if under or overweight)',(1,2))
TODO_COMPLETED = st.slider('How well do you complete your weekly to-do lists?',0,10,0)
FLOW = st.slider('In a typical day, how many hours do you experience Flow (=state of deep concentration) ? (From 0 to 5+)',0,5,0)
DAILY_STEPS = st.slider('How many steps (in thousands) do you typically walk everyday? (Average from 1 to 10+)',1,10,1)
LIVE_VISION = st.slider('For how many years ahead is your life vision very clear for? (From 0 to 10+)',0,10,0)
SLEEP_HOURS = st.slider('About how long (in hours) do you typically sleep? (From 1 to 10+)',1,10,1)
LOST_VACATION = st.slider('How many days of vacation do you typically lose every year? (From 0 to 10+)',0,10,0)
DAILY_SHOUTING = st.slider('How often do you shout or sulk at somebody?',0,10,0)
SUFFICIENT_INCOME = st.selectbox('How sufficient is your income to cover basic life expenses? (1 if insufficient, 2 if sufficient)',(1,2))
PERSONAL_AWARDS = st.slider('How many recognitions have you received in your life? (From 0 to 10+)',0,10,0)
TIME_FOR_PASSION = st.slider('How many hours do you spend everyday doing what you are passionate about? (Average from 0 to 10+)',0,10,0)
WEEKLY_MEDITATION = st.slider('In a typical week, how many times do you have the opportunity to think about yourself? (Average from 0 to 10+)',0,10,0)


pred = preprocess(FRUITS_VEGGIES,DAILY_STRESS,PLACES_VISITED,CORE_CIRCLE,SUPPORTING_OTHERS,SOCIAL_NETWORK,ACHIEVEMENT,DONATION,BMI_RANGE,TODO_COMPLETED,FLOW,DAILY_STEPS,LIVE_VISION,SLEEP_HOURS,LOST_VACATION,DAILY_SHOUTING,SUFFICIENT_INCOME,PERSONAL_AWARDS,TIME_FOR_PASSION,WEEKLY_MEDITATION,AGE,GENDER)

st.subheader('Résultat de la prévision')
if st.button("Predict"):
    st.write(f"Your well-being percentage is {pred}%")
    st.write("The average for 15 971 people is [54.894622]%")
