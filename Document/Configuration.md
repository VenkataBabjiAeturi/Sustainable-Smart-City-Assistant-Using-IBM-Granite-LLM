# ⚙️ Configuration Guide

This document describes how to configure the **Sustainable Smart City Assistant** project for local development and deployment. The project consists of multiple components, including backend services (FastAPI), frontend (Streamlit), environment variables, and integrations like IBM Watsonx Granite LLM and Pinecone.

---

## 📁 Environment Configuration

All sensitive keys and service configurations should be stored in a `.env` file located in the root directory. This file is excluded from version control using `.gitignore`.

Create a `.env` file based on the provided `.env.example`:

```env
# IBM Watsonx Granite LLM API Key
GRANITE_API_KEY=your_granite_api_key

# Pinecone Vector DB
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment  # e.g., us-west1-gcp
PINECONE_INDEX_NAME=smartcity-index

# Optional Logging Level
LOG_LEVEL=info
