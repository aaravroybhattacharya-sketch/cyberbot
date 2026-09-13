import streamlit as st
from groq import Groq  
import time  # Added for rate-limit pause intervals


# 1. PREMIUM APPARATUS LAYOUT
st.set_page_config(
    page_title="NEO-NET GLOBAL CORE // v6.0", 
    page_icon="🔮", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CYBERPUNK HUD DESIGN STYLING WITH SIDE-BY-SIDE INTEGRATION
st.markdown("""
    <style>
        .stApp { background-color: #0d0f12 !important; color: #ffffff !important; }
        section[data-testid="stSidebar"] { background-color: #11151c !important; }
        section[data-testid="stSidebar"] * { color: #ffffff !important; }
        input { background-color: #1a1f26 !important; color: #00f0ff !important; border: 2px solid #00f0ff !important; border-radius: 4px !important; }
        
        /* High-visibility input text styling */
        div[data-testid="stChatInput"] textarea { color: #00f0ff !important; background-color: #1a1f26 !important; font-size: 16px !important; }
        div[data-testid="stChatInput"] { border: 2px solid #00f0ff !important; border-radius: 4px !important; }
        
        /* Chat bubble styles */
        div[data-testid="stChatMessage"] { background-color: #13171f !important; border-left: 4px solid #00f0ff !important; border-radius: 4px 12px 12px 4px !important; margin-bottom: 15px !important; padding: 20px !important; }
        div[data-testid="stChatMessage"] p, div[data-testid="stChatMessage"] span, div[data-testid="stChatMessage"] li { color: #ffffff !important; font-size: 16px !important; }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) { border-left: 4px solid #bd00ff !important; background-color: #17131f !important; }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) p, div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) span { color: #00f0ff !important; }
        .glow-title { color: #00f0ff; text-shadow: 0 0 12px rgba(0, 240, 255, 0.6); font-family: 'Courier New', monospace; font-weight: bold; font-size: 2.5rem; }
        
        /* Clean minimalist upload overrides for the chat row */
        div[data-testid="stFileUploaderDropzone"] { padding: 0 !important; border: none !important; background: transparent !important; min-height: unset !important; }
        div[data-testid="stFileUploaderDropzone"] svg { display: none !important; }
        div[data-testid="stFileUploaderDropzone"] div { display: none !important; }
        div[data-testid="stFileUploaderFileData"] { display: none !important; }
        .stFileUploader small { display: none !important; }
        .stFileUploader label { display: none !important; }
        
        /* 🛠️ Comprehensive Fix: Scrub any lingering hidden text nodes */
        div[data-testid="stWidgetLabel"] { display: none !important; }
        
        /* 🛠️ Comprehensive Fix: Universal selector overrides to hide all default layout clutter */
div[data-testid="stFileUploaderDropzone"] * { 
    display: none !important; 
}

.stFileUploader button {
    background: #1a1f26 !important;
    border: 2px solid #bd00ff !important;
    color: #00f0ff !important;
    font-size: 20px !important;
    font-weight: bold !important;
    border-radius: 4px !important;
    width: 100% !important;
    height: 48px !important;
    box-shadow: none !important;
    display: flex !important; 
    justify-content: center !important;
    align-items: center !important;
}

/* Explicitly force the inner text nodes (+ symbol) inside the button block to render */
.stFileUploader button * { 
    display: inline-block !important; 
}

.stFileUploader { 
    padding-top: 0px !important; 
}

    </style>
""", unsafe_allow_html=True)

# 3. SIDEBAR CONTROL MATRIX
with st.sidebar:
    st.markdown("<h2 style='color: #bd00ff; font-family: monospace;'>[ GLOBAL_CTRL ]</h2>", unsafe_allow_html=True)
    st.caption("DEPLOYMENT STATE: PRODUCTION PUBLIC LINK")
    st.divider()
    
    temperature = st.slider("Creativity (Temp)", 0.1, 1.0, 0.7, 0.1)
    
    st.divider()
    if st.button("⚡ FLUSH MEMORY", use_container_width=True):
        st.session_state.cyber_history = []
        st.rerun()

# Check if the app is being run locally by you or via the public web URL
is_local_user = st.context.headers.get("Host", "").startswith("localhost") or st.context.headers.get("Host", "").startswith("127.0.0.1")

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

# Bug Fix: Auto-clear deadlocked memory loops if URL contains parameter instructions
if st.query_params.get("clear") == "true":
    st.session_state.cyber_history = []
    st.query_params.clear()

if "cyber_history" not in st.session_state:

    st.session_state.cyber_history = [
        {"role": "assistant", "content": "🧠 **[NEO-NET GLOBAL CORE ACTIVE]** System is now completely live. Cloud routing pipeline established successfully."}
    ]

# Render chat logs
for message in st.session_state.cyber_history:
    avatar = "🔮" if message["role"] == "user" else "⚙️"
    clean_display = message["content"]
    if "</think>" in clean_display:
        clean_display = clean_display.split("</think>")[-1].strip()
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(clean_display)

# 5. SIDE-BY-SIDE ENTRY MATRIX
injected_context = ""
col1, col2 = st.columns([0.07, 0.93])

with col1:
    # Compact file uploader stripped down to a dedicated row button
    uploaded_file = st.file_uploader("+", type=["txt", "py", "md"], label_visibility="collapsed")
    if uploaded_file is not None:
        try:
            file_contents = uploaded_file.read().decode("utf-8")
            st.toast(f"📥 {uploaded_file.name} context cached!", icon="✔️")
            injected_context = f"\n\n[FILE DATA ({uploaded_file.name})]:\n```\n{file_contents}\n```\n"
        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    user_prompt = st.chat_input("")

if user_prompt:
    full_processed_prompt = user_prompt + injected_context if injected_context else user_prompt
    with st.chat_message("user", avatar="🔮"):
        st.markdown(f"**[TRANS_IN]:** {user_prompt}")
    st.session_state.cyber_history.append({"role": "user", "content": full_processed_prompt})

    with st.chat_message("assistant", avatar="⚙️"):
        try:
            think_container = st.empty()
            answer_container = st.empty()
                    def response_streamer():
                # Smart Implementation: Retry loop protects from sudden 429 rate cuts
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        stream = client.chat.completions.create(
                            model='llama-3.3-70b-versatile',  # Upgraded to the absolute smartest model
                            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.cyber_history],
                            temperature=temperature,
                            max_tokens=400,  # Tight token reserve prevents model size calculation errors
                            stream=True
                        )
                        for chunk in stream:
                            if chunk.choices and len(chunk.choices) > 0:
                                content = chunk.choices.delta.content if hasattr(chunk.choices, 'delta') else chunk.choices.delta.content
                                if content is not None:
                                    yield content
                        return  # Break loop if streaming completes successfully
                    except Exception as err:
                        if "429" in str(err) and attempt < max_retries - 1:
                            time.sleep(2)  # Wait 2 seconds for the network rate limit windows to clear
                            continue
                        yield f"\n\n⚠️ [STREAM_INTERRUPTION]: Cloud core dropped packages. Details: {str(err)}"
                        return

                            
            full_reply = answer_container.write_stream(response_streamer())
            st.session_state.cyber_history.append({"role": "assistant", "content": full_reply})
        except Exception as e:
            st.error(f"[SYSTEM_LAUNCH_ERROR]: Cloud connection dropped. Details: {e}")
