import streamlit as st
from groq import Groq  # Free high-performance cloud AI host
import time  # Added for rate-limit pause intervals
import re  # Added to cleanly filter out hidden reasoning blocks

# 1. PREMIUM APPARATUS LAYOUT
st.set_page_config(
    page_title="NEO-NET GLOBAL CORE // v6.0", 
    page_icon="🔮", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CYBERPUNK HUD DESIGN STYLING WITH NATIVE BOTTOM CHATBAR PINNING
st.markdown("""
    <style>
        .stApp { background-color: #0d0f12 !important; color: #ffffff !important; }
        section[data-testid="stSidebar"] { background-color: #11151c !important; }
        section[data-testid="stSidebar"] * { color: #ffffff !important; }
        
        /* 🎨 STYLING FOR THE NATIVE BOTTOM FIXED CHAT INPUT BAR */
        div[data-testid="stChatInput"] {
            background-color: #1a1f26 !important;
            border: 2px solid #bd00ff !important;
            border-radius: 24px !important;
            padding: 4px 12px !important;
        }
        
        div[data-testid="stChatInput"] textarea {
            color: #00f0ff !important; 
            background-color: transparent !important;
            font-size: 16px !important;
        }
        
        /* Chat bubble styles */
        div[data-testid="stChatMessage"] { background-color: #13171f !important; border-left: 4px solid #00f0ff !important; border-radius: 4px 12px 12px 4px !important; margin-bottom: 15px !important; padding: 20px !important; }
        div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] span, div[data-testid="stChatMessage"] li { color: #ffffff !important; font-size: 16px !important; }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) { border-left: 4px solid #bd00ff !important; background-color: #17131f !important; }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) p, div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) span { color: #00f0ff !important; }
        .glow-title { color: #00f0ff; text-shadow: 0 0 12px rgba(0, 240, 255, 0.6); font-family: 'Courier New', monospace; font-weight: bold; font-size: 2.5rem; }
        
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR CONTROL MATRIX (Isolated Per User Session Tab)
with st.sidebar:
    st.markdown("<h2 style='color: #bd00ff; font-family: monospace;'>[ GLOBAL_CTRL ]</h2>", unsafe_allow_html=True)
    st.caption("DEPLOYMENT STATE: MULTI-USER LIVE PRODUCTION")
    st.divider()
    
    temperature = st.slider("Creativity (Temp)", 0.1, 1.0, 0.7, 0.1)
    
    st.divider()
    if st.button("⚡ FLUSH MEMORY", use_container_width=True):
        st.session_state.cyber_history = [
            {"role": "assistant", "content": "🧠 **[NEO-NET GLOBAL CORE ACTIVE]** Local vault cleared. System session initialized successfully."}
        ]
        st.rerun()

# 4. INITIALIZE DISPLAY CANVAS
st.markdown("<h1 class='glow-title'>⚡ NEO-NET GLOBAL // INTERFACE</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: monospace; color: #64748b;'>CLOUD REASONING ENGINE PIPELINE: ACTIVE</p>", unsafe_allow_html=True)
st.divider()

# Check for hidden cloud secret configuration
if "GROQ_API_KEY" not in st.secrets:
    st.error("❌ SYSTEM ERROR: Missing GROQ_API_KEY in cloud dashboard settings configuration.")
    st.stop()

# Initialize public server engine connection using hidden environment variable
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# Multi-User Isolation: Store chat arrays directly into isolated browser tab session state
if "cyber_history" not in st.session_state:
    st.session_state.cyber_history = [
        {"role": "assistant", "content": "🧠 **[NEO-NET GLOBAL CORE ACTIVE]** System is now completely live. Cloud routing pipeline established successfully."}
    ]

# Render chat logs
for message in st.session_state.cyber_history:
    avatar = "🔮" if message["role"] == "user" else "⚙️"
    clean_display = message["content"]
    clean_display = re.sub(r'<think>.*?</think>', '', clean_display, flags=re.DOTALL)
    clean_display = re.sub(r'<think>.*', '', clean_display, flags=re.DOTALL)
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(clean_display.strip())

# 5. LIVE AUTO-SCROLLER UTILITY ENGINE (Monitors elements and forces scroll updates)
st.components.v1.html("""
    <script>
        const scrollTarget = window.parent.document.querySelector('.main .block-container');
        const scrollContainer = window.parent.document.querySelector('.main');
        
        if (scrollTarget && scrollContainer) {
            const observer = new MutationObserver(() => {
                scrollContainer.scrollTo({
                    top: scrollContainer.scrollHeight,
                    behavior: 'smooth'
                });
            });
            observer.observe(scrollTarget, { childList: true, subtree: true });
        }
    </script>
""", height=0)

# 6. NATIVE STREAMLIT FIXED BOTTOM INPUT CONTAINERBAR
user_prompt = st.chat_input("Send a message tokens pipeline...")

if user_prompt:
    with st.chat_message("user", avatar="🔮"):
        st.markdown(f"**[TRANS_IN]:** {user_prompt}")
    st.session_state.cyber_history.append({"role": "user", "content": user_prompt})

    with st.chat_message("assistant", avatar="⚙️"):
        try:
            answer_container = st.empty()
            
            def response_streamer():
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        stream = client.chat.completions.create(
                            model='qwen/qwen3.6-27b',  
                            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.cyber_history],
                            temperature=temperature,
                            max_tokens=400,
                            stream=True
                        )
                        
                        full_response_text = ""
                        last_displayed_length = 0
                        
                        for chunk in stream:
                            if chunk.choices and len(chunk.choices) > 0:
                                first_choice = chunk.choices[0]
                                delta = first_choice.delta if hasattr(first_choice, 'delta') else first_choice
                                content = getattr(delta, 'content', None)
                                if content is not None:
                                    full_response_text += content
                                    
                                    clean_text = re.sub(r'<think>.*?</think>', '', full_response_text, flags=re.DOTALL)
                                    clean_text = re.sub(r'<think>.*', '', clean_text, flags=re.DOTALL)
                                    
                                    if len(clean_text) > last_displayed_length:
                                        new_content = clean_text[last_displayed_length:]
                                        last_displayed_length = len(clean_text)
                                        yield new_content
                        return
                        
                    except Exception as err:
                        if "429" in str(err) and attempt < max_retries - 1:
                            time.sleep(2.5)  
                            continue
                        yield f"\n\n⚠️ [STREAM_INTERRUPTION]: Cloud core dropped packages. Details: {str(err)}"
                        return
                            
            full_reply = answer_container.write_stream(response_streamer())
            st.session_state.cyber_history.append({"role": "assistant", "content": full_reply})
            st.rerun()  
        except Exception as e:
            st.error(f"[SYSTEM_LAUNCH_ERROR]: Cloud connection dropped. Details: {e}")
