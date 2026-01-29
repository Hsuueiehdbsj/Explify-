#!/bin/bash

echo "🚀 Explify Setup Script"
echo "======================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found: Python $python_version"

# Create virtual environment
echo ""
echo "🔨 Creating virtual environment..."
python3 -m venv explify_env

# Activate virtual environment
echo "✅ Activating virtual environment..."
source explify_env/bin/activate

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✨ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Activate the environment: source explify_env/bin/activate"
echo "   2. Set up your API key:"
echo "      - Copy .env.example to .env"
echo "      - Add your Gemini API key to .env"
echo "   3. Run the app: streamlit run explify_app.py"
echo ""
echo "🎉 Happy Explifying!"
