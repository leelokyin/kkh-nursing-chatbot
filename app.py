import streamlit as st
import streamlit.components.v1 as components
 
# Page config
st.set_page_config(page_title="KKH Nursing Chatbot", layout="wide")
 
# Load custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
 
# Layout columns
left, center, right = st.columns([1, 3, 1])
 
# --- LEFT SIDEBAR ---
with left:
    st.markdown("## 🧰 Controls")
    st.button("🧹 Clear Model Cache")
 
# --- CENTER HEADER ---
with center:
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("data/KKH Logo.jpg", width=80)
    with col2:
        st.markdown("""
            <div class='header'>
                <h3>KK Women's and Children's Hospital</h3>
                <p class='subtext'>🧠 Your 24/7 Nurse Assistant Bot 🧠</p>
            </div>
        """, unsafe_allow_html=True)
 
# --- CENTER CHATBOT ---
with center:
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    components.html("""
    <div id="webchat" style="width: 100%; height: 600px;"></div>
    <script src="https://cdn.botpress.cloud/webchat/v3.0/inject.js"></script>
 
    <style>
      #webchat .bpWebchat {
        position: unset;
        width: 100%;
        height: 100%;
        max-height: 100%;
        max-width: 100%;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      }
    </style>
 
    <script>
      window.botpress.on("webchat:ready", () => {
        window.botpress.open();
      });
 
      window.botpress.init({
        "botId": "0614e7e1-d08e-413a-a762-e05937abd30a",
        "clientId": "aaa1f595-76aa-4e2c-91e5-8ec43416aa5a",
        "selector": "#webchat"
      });
 
      // Helper to inject and send message
      function sendBotpressMessage(text) {
        const event = new CustomEvent("send-message", { detail: { text } });
        window.parent.document.dispatchEvent(event);
        const input = window.botpress.WebChat.getMessageTextArea();
        input.value = text;
        const keyboardEvent = new KeyboardEvent('keydown', { key: 'Enter', bubbles: true });
        input.dispatchEvent(keyboardEvent);
      }
 
      // Expose globally
      window.sendBotpressMessage = sendBotpressMessage;
    </script>
    """, height=620)
    st.markdown("</div>", unsafe_allow_html=True)
 
# --- RIGHT QUICK PROMPTS ---
with right:
    st.markdown("### 💬 Quick Prompts")
 
    def quick_prompt_block(title, prompts):
        with st.expander(title, expanded=False):
            for prompt in prompts:
                st.markdown(
                    f"<div class='prompt-btn' onclick='sendBotpressMessage(\"{prompt}\")'>{prompt}</div>",
                    unsafe_allow_html=True
                )
 
    quick_prompt_block("Clinical Scenarios", [
        "What is the protocol for managing febrile seizures?",
        "What to do for a child with suspected meningitis?",
        "How to manage a child with asthma attack?",
        "What is the protocol for managing dehydration?",
        "Steps for managing asthma attack"
    ])
 
    quick_prompt_block("Quiz Topics", [
        "Test me on general health questions",
        "Test me 5 questions on diseases one by one",
        "Test me 5 questions on doctor treatments one by one",
        "Test me on nutrition MCQ questions?",
        "Test me on dehydration",
        "Test me on signs of asthma attack",
        "Test me on the good source of dietary fibre?"
    ])
 
    quick_prompt_block("Calculator", [
        "Calculate fluid for 15kg child",
        "Calculate IV drip rate for 250ml over 2 hours",
        "Convert 500mg to mL for 1:10 solution",
        "Convert 2.5L to mL",
        "Calculate fluid for 20kg child",
        "How much fluid for 20kg?",
        "Calculate IV drip rate for 500ml over 4 hours",
        "Convert 100mg to mcg",
        "Convert 1.5L to mL"
    ])
