#!/bin/bash

# Telegram GigaChat Istanbul Guide Bot - Setup Script
# This script creates a virtual environment and installs dependencies

echo "📦 Setting up Telegram GigaChat Istanbul Guide Bot..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python $(python3 --version) found"

# Create virtual environment
echo "\n🔧 Creating virtual environment..."
python3 -m venv venv

echo "✓ Virtual environment created"

# Activate virtual environment
echo "\n🚀 Activating virtual environment..."
source venv/bin/activate

echo "✓ Virtual environment activated"

# Upgrade pip
echo "\n📥 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "\n📚 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "\n✅ Setup complete!"
echo "\n🎉 To activate the virtual environment, run:"
echo "   source venv/bin/activate"
echo "\n🤖 To start the bot, run:"
echo "   python main.py"
echo "\n💡 Make sure .env file is configured with your tokens!"
