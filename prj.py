import streamlit as st
import pickle
import time

#how to start go streamlit run prj.py

st.title("Twitter sentiment Analysis")

model=pickle.load(open('twitter_sentiment.pkl','rb'))


tweet=st.text_input("Enter your tweet")

Submit=st.button('predict')

if Submit:
    start=time.time()
    prediction =model.predict([tweet])
    end=time.time()
    st.write('prediction time taken: ',round(end-start, 2), 'seconds')
    print(prediction[0])
    st.write("predicted sentiment is:",prediction[0])