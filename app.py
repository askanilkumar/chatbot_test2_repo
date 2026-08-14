"""
Support Chatbot Demo — Streamlit + local guardrail, no external API.

Built for a live CI/CD demo: push code -> Cloud Build tests, builds, and
deploys -> Cloud Run. Replies are canned/local on purpose (no OpenAI call)
so the demo never depends on an external service being up or fast during
class — the only thing that can fail live is your own pipeline, which is
the point.
"""
import streamlit as st

from guardrail import is_blocked

st.set_page_config(page_title="Support Chatbot Demo", page_icon="🤖")

st.title("🤖 Support Chatbot Demo")
st.caption("Live CI/CD demo — every reply below is generated locally, no external API call.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, text in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(text)

prompt = st.chat_input("Ask me anything...")
if prompt:
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    if is_blocked(prompt):
        reply = (
            "I can't help with that request — it looks like an attempt to "
            "access internal instructions."
        )
    else:
        reply = (
            f'Thanks for your question — a real backend would answer: "{prompt}". '
            "(This demo uses a canned reply so it never depends on an external "
            "API during class.)"
        )

    st.session_state.messages.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.markdown(reply)
