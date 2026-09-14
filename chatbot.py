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
        div[data-testid="stFileUploaderFileData"] { display: none !important; }
        .stFileUploader small { display: none !important; }
        .stFileUploader label { display: none !important; }
        div[data-testid="stWidgetLabel"] { display: none !important; }
        
        /* Universal selector overrides to hide all default layout clutter */
        div[data-testid="stFileUploaderDropzone"] * { display: none !important; }
        
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
        
        .stFileUploader button * { display: inline-block !important; }
        .stFileUploader { padding-top: 0px !important; }
        footer {visibility: hidden;}
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
    # Deep scrub saved history items to ensure clean loading layouts
    clean_display = re.sub(r'<think>.*?</think>', '', clean_display, flags=re.DOTALL)
    clean_display = re.sub(r'<think>.*', '', clean_display, flags=re.DOTALL)
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(clean_display.strip())

# 5. SIDE-BY-SIDE ENTRY MATRIX (Pinned to the absolute bottom viewport layout)
st.markdown("<div class='bottom-chatbar-frame'>", unsafe_allow_html=True)

injected_context = ""
col1, col2 = st.columns([0.07, 0.93])

with col1:
    ...

st.markdown("</div>", unsafe_allow_html=True)


with col1:
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
            answer_container = st.empty()

            # 🛠️ AUTO-SCROLLER INJECTOR: Pushes viewport down smoothly while token streaming runs
            js_scroller = st.components.v1.html("""
                <script>
                    window.parent.document.querySelector('section.main').scrollTo({
                        top: window.parent.document.querySelector('section.main').scrollHeight,
                        behavior: 'smooth'
                    });
                </script>
            """, height=0)

            def response_streamer():

                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        stream = client.chat.completions.create(
                            model='qwen/qwen3.6-27b',  # 👑 Smartest reasoning model
                            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.cyber_history],
                            temperature=temperature,
                            max_tokens=400,
                            stream=True
                        )
                        
                        full_response_text = ""
                        last_displayed_length = 0
                        
                        for chunk in stream:
                            if chunk.choices and len(chunk.choices) > 0:
                                # 🚀 Security Patch: Targeting index zero list layout explicitly
                                first_choice = chunk.choices[0]
                                delta = first_choice.delta if hasattr(first_choice, 'delta') else first_choice
                                content = getattr(delta, 'content', None)
                                if content is not None:
                                    full_response_text += content
                                    
                                    # Strip out everything inside <think> tags instantly using regex patterns
                                    clean_text = re.sub(r'<think>.*?</think>', '', full_response_text, flags=re.DOTALL)
                                    clean_text = re.sub(r'<think>.*', '', clean_text, flags=re.DOTALL)
                                    
                                    # Only stream out the newly added content tokens to prevent repeating characters
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
        except Exception as e:
            st.error(f"[SYSTEM_LAUNCH_ERROR]: Cloud connection dropped. Details: {e}")
