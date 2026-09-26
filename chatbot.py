import streamlit as st
from groq import Groq  # Free high-performance cloud AI host
import time  # Added for rate-limit pause intervals
import re  # Added to cleanly filter out hidden reasoning blocks
temperature = 0.7

# 1. PREMIUM APPARATUS LAYOUT (NO SIDEBAR)
st.set_page_config(
    page_title="NEO-NET GLOBAL CORE // v6.0", 
    page_icon="🔮", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======= REMOVED FROM INITIALIZATION STEP =======
# All 'col_ctrl1, col_ctrl2 = st.columns()' blocks are deleted completely.
# The '⚡ FLUSH MEMORY' button sits on its own main row right below the dividers.


# 2. CYBERPUNK HUD DESIGN STYLING (OPTIMIZED READABILITY PATCH)
st.markdown("""
    <style>
        /* Base application background */
        /* 🚀 Completely deletes sidebar access nodes from view */
[data-testid="collapsedControl"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* 🚀 Sets the uniform ChatGPT dark gray canvas layer */
.stApp { background-color: #171717 !important; }


        
        /* 1. PRIMARY HEADERS & TITLES */
        .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
            color: #00f0ff !important;
            font-family: 'Courier New', monospace;
        }
        
        /* 2. BODY TEXT & PARAGRAPHS (Off-white to prevent glare) */
        /* 🚀 Softens text overlays with low-contrast off-white tokens */
        .stApp p, .stApp span, .stApp li, .stApp td, .stApp h1, .stApp h2, .stApp h3 { 
        color: #ECECEC !important; 
        font-size: 16px !important;
        
        }
        
        /* 3. BOLD TEXT / DEFINITION TERMS (Pure white pop) */
        .stApp strong, .stApp b, .stApp th {
            color: #ffffff !important;
            font-weight: 600 !important;
        }
        
        /* 4. MUTED SECONDARY TEXT (Captions, labels) */
        /* 🚀 Flags secondary layers down to clean mid-gray visibility */
        .stApp label, .stApp small, .stApp caption { 
        color: #B4B4B4 !important; 
        }

        
        /* Sidebar layout styling */
        section[data-testid="stSidebar"] { background-color: #11151c !important; }
        section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }
        
        /* Main Chat Input Container */
        /* 🚀 Elements take on layered surface depths */
        /* 🚀 Re-skins input console to reflect uniform gray theme elements */
       div[data-testid="stChatInput"] {
           background-color: #212121 !important; 
           border: 1px solid #2F2F2F !important;
           border-radius: 12px !important;
        }
       div[data-testid="stChatInput"] textarea {
           color: #ECECEC !important; /* Low contrast active typing font */
        }


            font-size: 16px !important;
            font-weight: 500 !important;
        }
        
                /* Main Chat Bubble (Background color set to #B00099) */
        div[data-testid="stChatMessage"] { 
            background-color: #B00099 !important;   
            border-left: 4px solid #0A84FF !important; /* 🚀 Intelligence Blue Accent Utility Indicator */
            border-radius: 8px !important; 
            margin-bottom: 15px !important; 
            padding: 16px !important; 
        }

        
        /* 🚀 White Box Overlay containing the Text Blocks */
        div[data-testid="stChatMessage"] div.stMarkdown,
        div[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
            background-color: #ffffff !important;   /* White text background container */
            border: 2px solid #ffffff !important;   /* Surrounds the text with white */
            padding: 12px 16px !important;
            border-radius: 8px !important;
            display: block !important;
        }
        
        /* Forces all text items inside the white background block to be solid black */
        div[data-testid="stChatMessage"] p, 
        div[data-testid="stChatMessage"] span, 
        div[data-testid="stChatMessage"] li, 
        div[data-testid="stChatMessage"] td, 
        div[data-testid="stChatMessage"] th { 
            color: #000000 !important; 
        }
        
        /* Alternating Bubble (User response container block for contrast) */
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) { 
            background-color: #3b0033 !important;  /* Muted dark wine color for the user bubble */
            border-left: 4px solid #bd00ff !important; 
        }

        
        /* Forces user bubble text to also stay solid black */
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) p, 
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) span { 
            color: #000000 !important; 
        }

        
        /* User response alternating bubbles (Light purple background for contrast) */
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) { 
            border-left: 4px solid #bd00ff !important; 
            background-color: #f3e8ff !important;  /* 🚀 Soft light purple so you can tell user vs assistant apart */
        }
        
        /* Forces user bubble text to also stay solid black */
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) p, 
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) span { 
            color: #000000 !important; 
        }

        
        /* User response alternating bubbles */
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) { border-left: 4px solid #bd00ff !important; background-color: #17131f !important; }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) p, div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatar"]):nth-child(even) span { color: #a855f7 !important; }
        
        .glow-title { color: #00f0ff !important; text-shadow: 0 0 12px rgba(0, 240, 255, 0.6); font-weight: bold; font-size: 2.5rem; }
        
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# 3 Removed sidebar controls

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
# Initialize session history with a custom built-in system persona instruction block
if "cyber_history" not in st.session_state:
    st.session_state.cyber_history = [
        {"role": "system", "content": "You are NEO-NET CORE, a custom-built, elite AI assistant optimized for highly advanced tasks, complex software engineering, logic, and reasoning."},
        {"role": "assistant", "content": "🧠 **[CUSTOM CORE DEPLOYED]** Highly advanced computing architecture linked. Ask me your most complex logical, mathematical, or software engineering questions."}
    ]


# Render chat logs
# Render chat logs (hide the custom internal system rule block from printing on screen)
for message in st.session_state.cyber_history:
    if message["role"] == "system":
        continue
    avatar = "🔮" if message["role"] == "user" else "⚙️"

    clean_display = message["content"]
    clean_display = re.sub(r'<think>.*?</think>', '', clean_display, flags=re.DOTALL)
    clean_display = re.sub(r'<think>.*', '', clean_display, flags=re.DOTALL)
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(clean_display.strip())

# 5. LIVE AUTO-SCROLLER UTILITY ENGINE (Using native 2026 st.html wrapper to run mutation monitoring safely)
st.html("""
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
""")

# 6. BOTTOM CONSOLE DOCK WITH SIDE-BY-SIDE BUTTON AND TEXTBAR
bottom_container = st.container()
with bottom_container:
    # 🚀 Restored to its original full-width stacked configuration structure
    uploaded_file = st.file_uploader("", type=["txt", "py", "md"], label_visibility="collapsed")
    
    # ...[context verification processes run cleanly here]...
    
    user_prompt = st.chat_input("Send a message...")



if user_prompt:
    full_processed_prompt = user_prompt + injected_context if injected_context else user_prompt
    with st.chat_message("user", avatar="🔮"):
        st.markdown(f"**[TRANS_IN]:** {user_prompt}")
    st.session_state.cyber_history.append({"role": "user", "content": full_processed_prompt})

    with st.chat_message("assistant", avatar="⚙️"):
        try:
            answer_container = st.empty()
            
            def response_streamer():
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        stream = client.chat.completions.create(
                            model='openai/gpt-oss-120b',
                            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.cyber_history],
                            temperature=temperature,
                            max_tokens=5000,  # 🚀 INCREASED: Gives the model plenty of room to reply
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
                        if "404" in str(err) or "decommissioned" in str(err):
                            try:
                                stream = client.chat.completions.create(
                                    model='openai/gpt-oss-120b',
                                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.cyber_history],
                                    temperature=temperature,
                                    max_tokens=5000,  # 🚀 INCREASED here too
                                    stream=True
                                )
                                full_response_text = ""
                                last_displayed_length = 0
                                for chunk in stream:
                                    if chunk.choices and len(chunk.choices) > 0:
                                        content = chunk.choices[0].delta.content
                                        if content:
                                            full_response_text += content
                                            if len(full_response_text) > last_displayed_length:
                                                yield full_response_text[last_displayed_length:]
                                                last_displayed_length = len(full_response_text)
                                return
                            except Exception:
                                pass
                        if "429" in str(err) and attempt < max_retries - 1:
                            time.sleep(3.0)
                            continue
                        yield f"\n\n⚠️ [STREAM_INTERRUPTION]: Cloud core dropped packages. Details: {str(err)}"
                        return
                            
            full_reply = answer_container.write_stream(response_streamer())
            st.session_state.cyber_history.append({"role": "assistant", "content": full_reply})
            st.rerun()  
        except Exception as e:
            st.error(f"[SYSTEM_LAUNCH_ERROR]: Cloud connection dropped. Details: {e}")
