# 📊 AI Data Analytics Chatbot  

An **AI-powered data analytics assistant** that can **analyze datasets, generate insights, and create visualizations** based on natural language queries.  
Upload your data (CSV, Excel, etc.), and simply ask questions like:  
- *“Show me a bar chart of sales by region.”*  
- *“What’s the correlation between revenue and ad spend?”*  
- *“Summarize key trends in this dataset.”*  

The chatbot uses **LLMs, LangChain, and visualization libraries** to automatically provide **answers, graphs, and dashboards**.  

---

## 🚀 Features  
- 🗂️ Upload datasets (CSV, Excel, JSON).  
- 💬 Chat with your data using **natural language queries**.  
- 📈 Auto-generate charts (bar, line, pie, scatter, heatmaps).  
- 📊 Statistical insights (correlation, regression, summary stats).  
- ⚡ LLM-powered reasoning & explanations.  
- 🌐 Deployable locally or on cloud (Streamlit/FastAPI).  

---

## 🛠️ Tech Stack  
- **Python** 🐍  
- **LLMs**: Openrouter api
- **LangChain** for RAG & query parsing  
- **Pandas, NumPy** for data processing  
- **Matplotlib, Plotly, Seaborn** for visualizations  
- **Streamlit / Flask / FastAPI** for UI and deployment  
- **Vector DB** (FAISS / Chroma / Pinecone) for knowledge retrieval  

---

## 📦 Installation  

```bash
# Clone repo
git clone https://github.com/srinadhs/ai-data-analytics-chatbot.git
cd ai-data-analytics-chatbot

# Create environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
