"""
Explify ⚡ - The Multimodal AI Explainer
A Streamlit app for summarizing Text, Images, and Videos using Google Gemini 1.5 Flash
"""

import streamlit as st
import google.generativeai as genai
from PIL import Image
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Explify ⚡",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for The Explify Vibe
st.markdown("""
<style>
    /* Force Dark Mode & Remove Padding */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Hero Header with Gradient */
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
        letter-spacing: -2px;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #9ca3af;
        text-align: center;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
    }
    
    /* Glassmorphism Card */
    .glass-card {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(168, 85, 247, 0.2);
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px 0 rgba(168, 85, 247, 0.1);
    }
    
    /* Gradient Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(168, 85, 247, 0.6);
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1e293b;
        border-radius: 12px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 8px;
        color: #9ca3af;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #a855f7 0%, #06b6d4 100%);
        color: white;
    }
    
    /* Results Card */
    .result-container {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
        border: 2px solid #a855f7;
        box-shadow: 0 8px 32px rgba(168, 85, 247, 0.3);
    }
    
    /* Sidebar Styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background-color: #1e293b;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #1e293b;
        color: #fafafa;
        border: 1px solid #475569;
        border-radius: 8px;
    }
    
    /* File Uploader */
    .stFileUploader {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 1rem;
        border: 2px dashed #475569;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #a855f7 0%, #06b6d4 100%);
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background-color: rgba(6, 182, 212, 0.1);
        border-left: 4px solid #06b6d4;
        border-radius: 8px;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1);
        border-left: 4px solid #ef4444;
        border-radius: 8px;
    }
    
    /* Loading Spinner */
    .stSpinner > div {
        border-top-color: #a855f7 !important;
    }
</style>
""", unsafe_allow_html=True)

# System Prompt
SYSTEM_PROMPT = """You are Explify, an AI assistant that creates engaging, concise summaries. 
Your summaries should:
- Capture the main points and hidden details
- Use emojis strategically for visual interest
- Format with bullet points and bold text for scannability
- Maintain a friendly, energetic tone
- Be thorough but not overwhelming

Make every summary feel like a VIP briefing - quick, insightful, and visually appealing."""

# Initialize session state
if 'api_configured' not in st.session_state:
    st.session_state.api_configured = False

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    # API Key Input
    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        value=os.getenv("GEMINI_API_KEY", ""),
        help="Enter your Google Gemini API key"
    )
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            st.session_state.api_configured = True
            st.success("✅ API Key Configured")
        except Exception as e:
            st.error(f"❌ Invalid API Key: {str(e)}")
            st.session_state.api_configured = False
    else:
        st.warning("⚠️ Please enter your API key")
        st.session_state.api_configured = False
    
    st.markdown("---")
    
    # Creativity Slider
    temperature = st.slider(
        "🎨 Creativity Level",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher = more creative, Lower = more focused"
    )
    
    st.markdown("---")
    
    # About Section
    st.markdown("""
    ### 💡 About Explify
    
    Explify uses **Google Gemini 1.5 Flash** to provide instant, intelligent summaries of:
    - 📄 Text documents
    - 🖼️ Images
    - 🎥 Videos
    
    Drop your content and get clarity in seconds!
    
    ---
    
    **Tips:**
    - Higher creativity = more expressive summaries
    - Videos are processed via Gemini File API
    - All uploads are automatically deleted after processing
    """)

# Main Interface
st.markdown('<h1 class="hero-title">Explify ⚡</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-subtitle">Drop content. Get clarity. Instant AI summaries for everything.</p>',
    unsafe_allow_html=True
)

# Check if API is configured
if not st.session_state.api_configured:
    st.error("🚨 Please configure your Gemini API Key in the sidebar to get started!")
    st.stop()

# Tabs
tab1, tab2, tab3 = st.tabs(["📄 Text", "🖼️ Image", "🎥 Video"])

# Helper function to generate content
def generate_summary(model_input, input_type="text"):
    """Generate summary using Gemini"""
    try:
        model = genai.GenerativeModel(
            gemini-1.5-flash-latest or gemini-pro,
            generation_config={
                'temperature': temperature,
                'top_p': 0.95,
                'top_k': 40,
                'max_output_tokens': 2048,
            }
        )
        
        if input_type == "text":
            prompt = f"{SYSTEM_PROMPT}\n\nSummarize this text:\n\n{model_input}"
            response = model.generate_content(prompt)
        elif input_type == "image":
            response = model.generate_content([SYSTEM_PROMPT + "\n\nDescribe and summarize this image in detail:", model_input])
        elif input_type == "video":
            response = model.generate_content([SYSTEM_PROMPT + "\n\nSummarize this video content:", model_input])
        
        return response.text
    except Exception as e:
        raise Exception(f"Generation failed: {str(e)}")

# TAB 1: Text
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    text_input = st.text_area(
        "Enter your text",
        height=200,
        placeholder="Paste any text here - articles, documents, notes, anything you want summarized...",
        key="text_area"
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        explify_text_btn = st.button("⚡ Explify Text", key="text_btn", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if explify_text_btn:
        if not text_input.strip():
            st.error("❌ Please enter some text to summarize!")
        else:
            with st.spinner("🔮 Explifying your text..."):
                try:
                    summary = generate_summary(text_input, "text")
                    st.markdown('<div class="result-container">', unsafe_allow_html=True)
                    st.markdown("### ✨ Summary")
                    st.markdown(summary)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

# TAB 2: Image
with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    uploaded_image = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"],
        key="image_uploader",
        help="Supported formats: JPG, JPEG, PNG"
    )
    
    if uploaded_image:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image = Image.open(uploaded_image)
            st.image(image, use_container_width=True, caption="Uploaded Image")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        explify_image_btn = st.button("⚡ Explify Image", key="image_btn", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if explify_image_btn:
        if not uploaded_image:
            st.error("❌ Please upload an image first!")
        else:
            with st.spinner("🔮 Analyzing your image..."):
                try:
                    image = Image.open(uploaded_image)
                    summary = generate_summary(image, "image")
                    st.markdown('<div class="result-container">', unsafe_allow_html=True)
                    st.markdown("### ✨ Image Analysis")
                    st.markdown(summary)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

# TAB 3: Video
with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    uploaded_video = st.file_uploader(
        "Upload a video",
        type=["mp4", "mov", "avi"],
        key="video_uploader",
        help="Supported formats: MP4, MOV, AVI"
    )
    
    if uploaded_video:
        st.video(uploaded_video)
        st.info(f"📹 Video uploaded: {uploaded_video.name} ({uploaded_video.size / 1024 / 1024:.2f} MB)")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        explify_video_btn = st.button("⚡ Explify Video", key="video_btn", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if explify_video_btn:
        if not uploaded_video:
            st.error("❌ Please upload a video first!")
        else:
            with st.spinner("🔮 Processing your video... This may take a minute..."):
                temp_file_path = None
                gemini_file = None
                
                try:
                    # Save uploaded file temporarily
                    temp_file_path = f"/tmp/{uploaded_video.name}"
                    with open(temp_file_path, "wb") as f:
                        f.write(uploaded_video.getbuffer())
                    
                    # Upload to Gemini
                    st.info("⬆️ Uploading video to Gemini...")
                    gemini_file = genai.upload_file(temp_file_path, mime_type=uploaded_video.type)
                    
                    # Wait for processing
                    st.info("⏳ Processing video on Gemini servers...")
                    while gemini_file.state.name == "PROCESSING":
                        time.sleep(2)
                        gemini_file = genai.get_file(gemini_file.name)
                    
                    if gemini_file.state.name == "FAILED":
                        raise Exception("Video processing failed on Gemini servers")
                    
                    # Generate summary
                    st.info("✍️ Generating summary...")
                    summary = generate_summary(gemini_file, "video")
                    
                    # Display results
                    st.markdown('<div class="result-container">', unsafe_allow_html=True)
                    st.markdown("### ✨ Video Summary")
                    st.markdown(summary)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.success("✅ Video processed successfully!")
                    
                except Exception as e:
                    st.error(f"❌ Error processing video: {str(e)}")
                
                finally:
                    # Cleanup: Delete file from Gemini
                    if gemini_file:
                        try:
                            gemini_file.delete()
                            st.info("🗑️ Video deleted from Gemini servers")
                        except:
                            pass
                    
                    # Cleanup: Delete temporary file
                    if temp_file_path and os.path.exists(temp_file_path):
                        try:
                            os.remove(temp_file_path)
                        except:
                            pass

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #6b7280; font-size: 0.875rem;">Made with ⚡ by Explify | Powered by Google Gemini 1.5 Flash</p>',
    unsafe_allow_html=True
)
