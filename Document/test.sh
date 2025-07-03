#!/bin/bash

echo "🔍 Running Project Health Check for Sustainable Smart City Assistant..."

# Load environment variables
if [ -f .env ]; then
  echo "✅ .env file found. Loading environment variables..."
  export $(grep -v '^#' .env | xargs)
else
  echo "❌ .env file not found. Please create one based on .env.example."
  exit 1
fi

# Check Python version
echo -n "🐍 Checking Python version... "
python3 --version

# Check if required commands are available
commands=("uvicorn" "streamlit" "curl")
for cmd in "${commands[@]}"; do
  if ! command -v $cmd &> /dev/null; then
    echo "❌ $cmd not found. Please install it before running the app."
    exit 1
  else
    echo "✅ $cmd is installed."
  fi
done

# Test FastAPI backend (assumes running on default port 8000)
echo "🌐 Testing FastAPI backend endpoint..."
curl -s http://localhost:8000/docs > /dev/null

if [ $? -eq 0 ]; then
  echo "✅ FastAPI backend is reachable at http://localhost:8000"
else
  echo "⚠️ FastAPI backend not reachable. Is it running?"
fi

# Test Streamlit app (optional check for port 8501)
echo "🌐 Testing Streamlit frontend endpoint..."
curl -s http://localhost:8501 > /dev/null

if [ $? -eq 0 ]; then
  echo "✅ Streamlit frontend is reachable at http://localhost:8501"
else
  echo "⚠️ Streamlit frontend not reachable. Is it running?"
fi

# Test IBM Granite LLM key presence
if [ -z "$GRANITE_API_KEY" ]; then
  echo "❌ GRANITE_API_KEY is missing in .env"
else
  echo "✅ GRANITE_API_KEY found."
fi

# Test Pinecone API key presence
if [ -z "$PINECONE_API_KEY" ]; then
  echo "❌ PINECONE_API_KEY is missing in .env"
else
  echo "✅ PINECONE_API_KEY found."
fi

echo "✅ All basic checks complete. Ready to run!"
