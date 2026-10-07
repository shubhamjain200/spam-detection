import streamlit as st
import joblib
model=joblib.load("sentiment.pkl")
st.set_page_config(layout='wide')
st.title("Spam detection Project")
st.sidebar.image("926015_passport_photo.PNG")
st.sidebar.title("About us")
st.sidebar.text("we are developing ml projects based on NLP in LN AI Academy")
st.sidebar.title("About Projects")
st.sidebar.text("This project reprents whether msg is spam or ham")
st.sidebar.title("Contact us")
st.sidebar.text("+916283008506")
sample_review=st.selectbox("Sample reviews of spam and ham",options=['Congratulations! You have won ₹10,00,000. Claim your prize now!'
                                                                     ,'You have won a FREE iPhone! Claim your gift immediately.',
                                                                     'WINNER! You have been selected for a lottery prize of ₹50,000',
                                                                     'FREE recharge available! Click this link to claim',
                                                                     'The train will arrive at 8:30 PM',
                                                                     'I am on my way home. See you soon.',
                                                                     'Good morning! Have a great day'])
if st.button("Predict",key="b1"):
    pred=model.predict([sample_review])
    prob=model.predict_proba([sample_review])
    if pred[0]==0:
        st.error(f"Ham {prob[0][0]:.2f}")
    else:
        st.success(f"Spam{prob[0][1]:.2f}")
        st.balloons()
sample_review2=st.text_input("Review")
if st.button("Predict",key="b2"):
    pred=model.predict([sample_review])
    prob=model.predict_proba([sample_review])
    if pred[0]==0:
        st.error(f"Ham {prob[0][0]:.2f}")
    else:
        st.success(f"Spam{prob[0][1]:.2f}")
        st.balloons()