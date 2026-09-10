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

if "cyber_history" not in st.session_state:
    st.session_state.cyber_history = [
        {"role": "assistant", "content": "🧠 **[NEO-NET GLOBAL CORE ACTIVE]** System is now completely live. Cloud routing pipeline established successfully."}
    ]

for message in st.session_state.cyber_history:
    avatar = "🔮" if message["role"] == "user" else "⚙️"
    # Filter history view to hide residual tags for older stored content
    clean_display = message["content"]
    if "</think>" in clean_display:
        clean_display = clean_display.split("</think>")[-1].strip()
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(clean_display)

if user_prompt := st.chat_input("Input transmission token..."):
    full_processed_prompt = user_prompt + injected_context if injected_context else user_prompt
    with st.chat_message("user", avatar="🔮"):
        st.markdown(f"**[TRANS_IN]:** {user_prompt}")
    st.session_state.cyber_history.append({"role": "user", "content": full_processed_prompt})

    with st.chat_message("assistant", avatar="⚙️"):
        try:
            think_container = st.empty()
            answer_container = st.empty()
            
            def response_streamer():
                try:
                    stream = client.chat.completions.create(
                        model='qwen/qwen3.6-27b',
                        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.cyber_history],
                        temperature=temperature,
                        stream=True
                    )
                    
                    in_think_block = False
                    think_buffer = ""
                    initial_buffer = ""
                    buffer_limit = 15  # Buffer up to 15 characters to intercept structural tags cleanly
                    
                    for chunk in stream:
                        if not chunk.choices or len(chunk.choices) == 0:
                            continue
                            
                        delta = chunk.choices[0].delta if hasattr(chunk.choices[0], 'delta') else chunk.choices[0]
                        content = getattr(delta, 'content', None)
                        
                        if content is None:
                            continue
                            
                        # Step A: Feed the initial safety character buffer to stop layout flashes
                        if len(initial_buffer) < buffer_limit and not in_think_block and not think_buffer:
                            initial_buffer += content
                            if "<think>" in initial_buffer:
                                in_think_block = True
                                think_buffer = initial_buffer.replace("<think>", "").strip()
                                initial_buffer = ""
                            continue
                        
                        # Process chunks once the buffer is checked
                        current_chunk = content if not initial_buffer else (initial_buffer + content)
                        initial_buffer = "" # Flush the safety buffer flag
                        
                        if "<think>" in current_chunk:
                            in_think_block = True
                            current_chunk = current_chunk.replace("<think>", "")
                        
                        if "</think>" in current_chunk:
                            in_think_block = False
                            current_chunk = current_chunk.replace("</think>", "")
                            
                            # Step B: Secure Privacy Barrier - Only render logs if you are the host on localhost
                            if is_local_user:
                                with st.expander("⚙️ [SYSTEM_LOG // REASONING_PROCESS]", expanded=False):
                                    st.code(think_buffer.strip())
                            think_container.empty()
                            continue

                        if in_think_block:
                            think_buffer += current_chunk
                            # Only display live status panels locally
                            if is_local_user:
                                think_container.markdown(f"🤖 *Thinking...*\n```text\n{think_buffer}\n```")
                        else:
                            yield current_chunk
                            
                except Exception as stream_err:
                    yield f"\n\n⚠️ [STREAM_INTERRUPTION]: Cloud stream encountered a pocket drop. Details: {str(stream_err)}"
                            
            full_reply = answer_container.write_stream(response_streamer())
            st.session_state.cyber_history.append({"role": "assistant", "content": full_reply})
        except Exception as e:
            st.error(f"[SYSTEM_LAUNCH_ERROR]: Cloud connection dropped. Details: {e}")
