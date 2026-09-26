import streamlit as st
st.title("My First streamlit App!!!")
st.write("Welcome to my AL applications!")
name = st.text_input("Enter your name:")
if st.button("submit"):
    st.write("Hello",name)
st.markdown("*Streamlit* is **really** ***cool***.")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")