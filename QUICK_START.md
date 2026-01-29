# ⚡ Explify Quick Start Guide

Get up and running with Explify in 3 minutes!

## 🎯 What is Explify?

Explify is a beautiful, dark-themed web app that uses Google's Gemini 1.5 Flash AI to instantly summarize:
- 📄 **Text** - Articles, documents, notes
- 🖼️ **Images** - Photos, screenshots, diagrams  
- 🎥 **Videos** - MP4, MOV files

## 🚀 Option 1: Local Development (Fastest)

### Prerequisites
- Python 3.10 or higher
- A Google Gemini API key ([Get one FREE](https://makersuite.google.com/app/apikey))

### Steps

1. **Extract the zip file**
   ```bash
   unzip explify-project.zip
   cd explify
   ```

2. **Run the automated setup**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Activate the environment**
   ```bash
   source explify_env/bin/activate
   ```

4. **Configure your API key**
   
   **Method A: Environment file** (Recommended)
   ```bash
   cp .env.example .env
   # Edit .env and add: GEMINI_API_KEY=your_key_here
   ```
   
   **Method B: In-app entry**
   - Just run the app and enter the key in the sidebar

5. **Launch Explify!**
   ```bash
   streamlit run explify_app.py
   ```

6. **Open your browser**
   - Streamlit will automatically open http://localhost:8501
   - Or manually visit that URL

### Manual Installation (Alternative)

```bash
# Create virtual environment
python3 -m venv explify_env
source explify_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set API key
cp .env.example .env
# Edit .env: GEMINI_API_KEY=your_key_here

# Run
streamlit run explify_app.py
```

---

## ☁️ Option 2: Deploy to Streamlit Cloud (Recommended for Production)

### Why Streamlit Cloud?
- ✅ **Free hosting** for public apps
- ✅ **Auto-deployment** from GitHub
- ✅ **No server management**
- ✅ **Instant sharing** with custom URL

### Quick Deploy Steps

1. **Push to GitHub**
   ```bash
   # Create new repo on GitHub, then:
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/explify.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/explify`
   - Main file: `explify_app.py`
   - Click "Deploy"

3. **Add your API key as a secret**
   - While deploying, click "⚙️ Settings"
   - Go to "Secrets"
   - Add:
     ```toml
     GEMINI_API_KEY = "your_api_key_here"
     ```
   - Save and wait for auto-restart

4. **Share your app!**
   - Your app will be live at: `https://YOUR_APP.streamlit.app`

📖 **Detailed deployment guide**: See `DEPLOYMENT_GUIDE.md`

---

## 🎮 Using Explify

### 1. Text Summarization
- Click the **"📄 Text"** tab
- Paste any text (articles, documents, notes)
- Click **"⚡ Explify Text"**
- Get an instant, scannable summary with emojis and bullets!

### 2. Image Analysis
- Click the **"🖼️ Image"** tab
- Upload a JPG or PNG image
- Click **"⚡ Explify Image"**
- Get a detailed description and insights

### 3. Video Summarization
- Click the **"🎥 Video"** tab
- Upload an MP4, MOV, or AVI video
- Click **"⚡ Explify Video"**
- Wait 30-60 seconds (depending on video size)
- Get a comprehensive video summary!

### 🎨 Adjust Creativity
Use the **"Creativity Level"** slider in the sidebar:
- **Low (0.0-0.3)**: Factual, focused summaries
- **Medium (0.4-0.7)**: Balanced approach (default)
- **High (0.8-1.0)**: Creative, expressive summaries

---

## 🔧 Troubleshooting

### "API Key Invalid"
- Double-check your key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Make sure there are no extra spaces
- Try entering it directly in the sidebar

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Port already in use"
```bash
streamlit run explify_app.py --server.port 8502
```

### Video Upload Issues
- Maximum recommended size: 100MB
- Supported formats: MP4, MOV, AVI
- Processing takes 30-120 seconds

---

## 📁 Project Files Overview

```
explify/
├── explify_app.py           # Main application (START HERE)
├── requirements.txt         # Python dependencies
├── README.md               # Full documentation
├── DEPLOYMENT_GUIDE.md     # Streamlit Cloud guide
├── setup.sh                # Automated setup script
├── .env.example            # API key template
└── .gitignore              # Git ignore rules
```

---

## 🎓 Next Steps

1. ✅ **Test all three modes** (Text, Image, Video)
2. 🎨 **Experiment with creativity levels**
3. 🌐 **Deploy to Streamlit Cloud** for easy sharing
4. 📱 **Share your app URL** with friends/colleagues
5. 🔧 **Customize the code** (it's all in `explify_app.py`!)

---

## 💡 Tips & Tricks

- **Best Image Results**: Clear, well-lit photos work best
- **Video Tips**: Shorter videos (<5 min) process faster
- **Text Length**: Works with anything from a paragraph to full articles
- **Mobile Friendly**: Access your deployed app on any device
- **Dark Mode Native**: Optimized for comfortable viewing

---

## 🆘 Need Help?

- 📖 Check `README.md` for detailed documentation
- 🚀 See `DEPLOYMENT_GUIDE.md` for hosting questions
- 💬 Ask on [Streamlit Forum](https://discuss.streamlit.io/)
- 🤖 Gemini API docs: [ai.google.dev](https://ai.google.dev/docs)

---

## 🎉 You're Ready!

You now have everything you need to run Explify locally or deploy it to the cloud. 

**Start exploring multimodal AI summaries now!** ⚡

---

Made with ⚡ by Explify | Powered by Google Gemini 1.5 Flash
