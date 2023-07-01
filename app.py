import streamlit as st
import pickle

c=pickle.load(open('c.pkl','rb'))
model = pickle.load(open('model1.pkl','rb'))
st.title("SMS Classifier")
inp_msg = st.text_input("enter the msg")
if st.button('Predict'):
    ct = c.transform([inp_msg])
    result = model.predict(ct)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("HAM")
