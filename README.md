# Explify ⚡ - The Multimodal AI Explainer

A sleek, dark-themed Streamlit application that uses Google Gemini 1.5 Flash to provide instant AI summaries for text, images, and videos.

## 🎨 Design Features

- **Dark Mode Theme**: Deep charcoal backgrounds (#0e1117) with neon purple (#a855f7) and cyan (#06b6d4) accents
- **Glassmorphism**: Frosted glass effect on result cards with blur and transparency
- **Gradient Elements**: Buttons and text with smooth color transitions
- **Responsive Layout**: Clean, modern interface with hover effects and smooth animations

## ✨ Features

### 📄 Text Summarization
- Paste any text content for instant AI-powered summaries
- Adjustable creativity level for different summary styles

### 🖼️ Image Analysis
- Upload images (JPG, PNG) for detailed descriptions and insights
- Visual preview before analysis

### 🎥 Video Summarization
- Upload videos (MP4, MOV, AVI) for content summaries
- Automatic Gemini File API integration with:
  - Server-side video processing
  - Processing state monitoring
  - Automatic cleanup after generation

## 🚀 Installation

1. **Clone or download the project files**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up your API key:**
   - Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Option A: Create a `.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
   - Option B: Enter directly in the app sidebar

4. **Run the application:**
```bash
streamlit run explify_app.py
```

## 📋 Requirements

- Python 3.10 or higher
- Streamlit 1.31.0+
- Google Generative AI SDK
- PIL (Pillow) for image processing
- python-dotenv for environment variables

## 🎮 Usage

1. **Configure API Key**: Enter your Gemini API key in the sidebar
2. **Adjust Creativity**: Use the slider to control summary style (0.0-1.0)
3. **Choose Input Type**: Select from Text, Image, or Video tabs
4. **Upload/Enter Content**: Provide your content
5. **Click Explify**: Get your instant AI summary!

## 🔧 Technical Details

### Video Processing Flow
The app implements proper Gemini File API workflow:
1. Upload video file to Gemini servers
2. Poll processing state until completion
3. Generate content once video is active
4. Delete file from Gemini cloud to save quota
5. Clean up temporary local files

### Customization
Adjust these parameters in the code:
- `temperature`: Controls creativity (set via slider)
- `max_output_tokens`: Maximum summary length (default: 2048)
- `top_p` and `top_k`: Sampling parameters

## 🎨 Color Palette

- **Background**: `#0e1117` (Deep Charcoal)
- **Secondary BG**: `#1e293b` (Slate)
- **Accent Purple**: `#a855f7` (Neon Purple)
- **Accent Cyan**: `#06b6d4` (Bright Cyan)
- **Text**: `#fafafa` (Off White)

## 🔒 Security

- API keys are handled securely via password input
- Environment variables supported via `.env` file
- Temporary files automatically deleted after processing
- Uploaded videos removed from Gemini servers post-generation

## 📝 License

Free to use and modify for personal and commercial projects.

## 🙏 Credits

- **AI Model**: Google Gemini 1.5 Flash
- **Framework**: Streamlit
- **Design**: Custom glassmorphism with gradient accents

---

Made with ⚡ by Explify | Powered by Google Gemini 1.5 Flash
