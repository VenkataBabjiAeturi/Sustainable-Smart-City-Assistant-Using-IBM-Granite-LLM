# 🔁 Project Workflow – Sustainable Smart City Assistant

This document describes the functional workflow of the **Sustainable Smart City Assistant**. It explains how each module processes inputs and generates meaningful outputs, using a mix of LLMs, data pipelines, and analytics.

---

## 🧭 High-Level System Flow

```text
User Input (Text/CSV/Feedback) 
      ↓
Frontend (Streamlit UI)
      ↓
FastAPI Backend (Routing & Preprocessing)
      ↓
⎧ IBM Granite LLM (NLP Tasks)
⎨ Pinecone Vector DB (Policy Search)
⎩ ML Models (Forecasting, Anomaly Detection)
      ↓
Processed Output Returned to Frontend
      ↓
Displayed to User via Streamlit UI
