import streamlit as st
from ai import generate_ai_response

with st.sidebar:
    selected_language = st.selectbox(
        "Select language",
        ("English", "French", "German", "Italian", "Japanese", "Korean", "Portuguese", "Spanish")
    )
    traits = st.multiselect(
        "Select traits of your assistant",
        ["Funny",
         "Charasmatic",
         "Rude",
         "Optimistic",
         "Pessimistic",
         "Creative",
         "Ambitious",
        ]
    )

# initial message
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant",
         "content": "Hello! I'm here to assist with all of your weather needs!"},
    ]

# display  messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# get user input
user_prompt = st.chat_input()

if user_prompt is not None:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Working..."):
            ai_response, context = generate_ai_response(
                language=selected_language,
                traits=traits,
                user_prompt=user_prompt
            )
            st.write(ai_response)

    new_ai_responses = {"role": "assistant", "content": ai_response}
    st.session_state.messages.append(new_ai_responses)


    