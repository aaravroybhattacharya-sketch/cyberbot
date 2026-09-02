import streamlit as st
from groq import Groq  # Free high-performance cloud AI host

# 1. PREMIUM APPARATUS LAYOUT
st.set_page_config(
    page_title="NEO-NET GLOBAL CORE // v6.0", 
    page_icon="🔮", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CYBERPUNK HUD DESIGN STYLING
st.markdown("""
    <style>
        .stApp { background-color: #0d0f12 !important; color: #ffffff !important; }
        section[data-testid="stSidebar"] { background-color: #11151c !important; }
        section[data-testid="stSidebar"] * { color: #ffffff !important; }
        input { background-color: #1a1f26 !important; color: #00f0ff !important; border: 2px solid #00f0ff !important; border-radius: 4px !important; }
        div[data-testid="stChatInput"] textarea { color: #00f0ff !important; background-color: #1a1f26 !important; }
        div[data-testid="stChatMessage"] { background-color: #13171f !important; border-left: 4px solid #00f0ff !important; border-radius: 4px 12px 12px 4px !important; margin-bottom: 15px !important; padding: 20px !important; }
        div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] span, div[data-testid="stChatMessage"] li { color: #ffffff !important; font-size: 16px !important; }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) { border-left: 4px solid #bd00ff !important; background-color: #17131f !important; }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) p, div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) span { color: #00f0ff !important; }
        .glow-title { color: #00f0ff; text-shadow: 0 0 12px rgba(0, 240, 255, 0.6); font-family: 'Courier New', monospace; font-weight: bold; font-size: 2.5rem; }
        div[data-testid="stFileUploadDropzone"] { background-color: #1a1f26 !important; border: 2px dashed #bd00ff !important; }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR CONTROL MATRIX
with st.sidebar:
    st.markdown("<h2 style='color: #bd00ff; font-family: monospace;'>[ GLOBAL_CTRL ]</h2>", unsafe_allow_html=True)
    st.caption("DEPLOYMENT STATE: PRODUCTION PUBLIC LINK")
    st.divider()
    
    # Secure API data lock input slot for the cloud server key
    groq_api_key = st.text_input("🔑 ENTER MODEL ACCESS KEY:", type="password", help="Enter your Groq key.")
    
    st.divider()
    st.markdown("<b style='color: #bd00ff;'>📥 FILE ANALYZER:</b>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload files (.txt, .py, .md)", type=["txt", "py", "md"])
    
    injected_context = ""
    if uploaded_file is not None:
        try:
            file_contents = uploaded_file.read().decode("utf-8")
            st.success(f"✔️ {uploaded_file.name} cached!")
            injected_context = f"\n\n[FILE DATA ({uploaded_file.name})]:\n```\n{file_contents}\n```\n"
        except Exception as e:
            st.error(f"Error: {e}")
            
    st.divider()
    temperature = st.slider("Creativity (Temp)", 0.1, 1.0, 0.7, 0.1)
    
    st.divider()
    if st.button("⚡ FLUSH MEMORY", use_container_width=True):
        st.session_state.cyber_history = []
        st.rerun()

# 4. INITIALIZE DISPLAY CANVAS
st.markdown("<h1 class='glow-title'>⚡ NEO-NET GLOBAL // INTERFACE</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family: monospace; color: #64748b;'>CLOUD REASONING ENGINE PIPELINE: STANDBY</p>", unsafe_allow_html=True)
st.divider()

if not groq_api_key:
    st.warning("⚠️ ACCESS LINK DECRYPTED: Waiting for authorization sequence. Provide a model access key in the left dashboard node to wake up the engine network.")
    st.stop()

# Initialize public server engine connection
client = Groq(api_key=groq_api_key)

if "cyber_history" not in st.session_state:
    st.session_state.cyber_history = [
        {"role": "assistant", "content": "🧠 **[NEO-NET GLOBAL CORE ACTIVE]** System is now completely live. Cloud routing pipeline established successfully."}
    ]

for message in st.session_state.cyber_history:
    avatar = "🔮" if message["role"] == "user" else "⚙️"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if user_prompt := st.chat_input("Input transmission token..."):
    full_processed_prompt = user_prompt + injected_context if injected_context else user_prompt
    with st.chat_message("user", avatar="🔮"):
        st.markdown(f"**[TRANS_IN]:** {user_prompt}")
    st.session_state.cyber_history.append({"role": "user", "content": full_processed_prompt})

    with st.chat_message("assistant", avatar="⚙️"):
        try:
            def response_streamer():
                stream = client.chat.completions.create(
                    model='llama-3.2-3b-preview',  # Meta Llama 3.2 streaming over lightning cloud servers
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.cyber_history],
                    temperature=temperature,
                    stream=True
                )
                for chunk in stream:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
            full_reply = st.write_stream(response_streamer())
            st.session_state.cyber_history.append({"role": "assistant", "content": full_reply})
        except Exception as e:
            st.error(f"[SYSTEM_LAUNCH_ERROR]: Cloud connection dropped. Details: {e}")
