import streamlit as st
import google.generativeai as genai

st.title("AI Chatbot with Google GenAI😊")
st.subheader("This is a Data Science tutor chatbot🤖 which answers all the data science🧑‍💻 related queries. 🗨️Chat and explore more about Data Science😊")

#Read the API Key

f = open(".gemini1.txt")

key=f.read()

#Configure the API Key

genai.configure(api_key=key)

#Init a gemini model
model = genai.GenerativeModel (model_name="gemini-1.5-pro-latest",
                               system_instruction="""You are a helpful AI Teaching Assistant.
                               Given a Data Science topic help the user understand it. 
                               You also answer any followup questions as well.
                               If a question is not related to data science, the response should be,
                            'That is beyond my knowledge.*""")
#If there is no chat_history in session, init one

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

#Init the chat object

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history