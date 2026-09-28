import ollama
import streamlit as st
st.title("✨ Welcome to my ChatBot App!!! 🤖")
st.set_page_config(
    page_title="My ChatBot",
    page_icon="🤖",
    layout="wide"
)
st.markdown("### 🧠📚 Chat • Learn • Create • Explore ✨")
with st.sidebar:
   st.header= ("Chat Settings")
   if st.button("Clear Chat🗑️"):
      st.session_state.messages = []
   personalities = {
      "👶kid" : "Answer the questions like your are explaining to a 5 year old kid in two lines only",
      "🫂Friend" :"Ans the questions in a friendly and casual manner. Give answer in two lines only",
      "✍️Study assistant" : "Answer the question ",
      "🧑‍🏫English Tutor" : " ",
      "👑Story Generator" : ""
   }
   personality = st.selectbox("Select a personality",personalities.keys())
   uploaded_file = st.file_uploader("Upload a text file...")
   try:
     if uploaded_file:
      st.success("File uploaded successfully")
      content = uploaded_file.read().decode("utf-8")
      if st.button("Display"):
        st.text(content)
   except: 
      st.error("File Type not supported🤦")     
if "messages" not in st.session_state:
   st.session_state.messages = []
for msg in st.session_state.messages:
   with st.chat_message(msg["role"]):
      st.write(msg["content"])
question = st.chat_input("You: ")
if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.chat_message("user"):
      st.write(question)
    with st.spinner("Wait, model is loading...🚀"):
     response = ollama.chat(
        model = "llama3.2:3b",
        messages= [
           {"role":"system", "content": personalities[personality]}]
           + st.session_state.messages )
    st.session_state.messages.append(
        {"role": "assistant",
            "content": response["message"]["content"]
        }
    ) 
    with st.chat_message("assistant"):
     ( "AI",response["message"]["content"])



