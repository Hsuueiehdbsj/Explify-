# Explify Project Structure

explify/
├── explify_app.py           # Main Streamlit application (437 lines)
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation and usage guide
├── DEPLOYMENT_GUIDE.md     # Comprehensive Streamlit Cloud deployment guide
├── setup.sh                # Automated setup script for local development
├── .env.example            # Template for environment variables
└── .gitignore              # Git ignore rules

## Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Run the app
streamlit run explify_app.py
```

### Streamlit Cloud Deployment
See DEPLOYMENT_GUIDE.md for detailed instructions.

## Features
- 📄 Text summarization
- 🖼️ Image analysis
- 🎥 Video processing (with Gemini File API)
- 🎨 Dark theme with glassmorphism design
- 🌈 Purple-Cyan gradient accents

## Tech Stack
- Python 3.10+
- Streamlit 1.31.0
- Google Generative AI (Gemini 1.5 Flash)
- PIL for image processing
