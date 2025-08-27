# 📊 AI Data Analyst Chatbot  

An **AI-powered data analyst chatbot** built with **Streamlit** and **OpenRouter API**.  
This app lets you **upload files (CSV, Excel, PDF, DOCX, TXT)** and interact with them using **natural language queries**.  
The chatbot can **analyze datasets, extract text, summarize content, and answer data-related questions**.  

---

## 🚀 Features  
- 🗂️ **Upload & parse multiple file formats**: CSV, Excel, PDF, DOCX, TXT  
- 📄 **Extract text** from documents (including OCR for scanned PDFs)  
- 📊 **Preview tabular data** in a dataframe  
- 💬 **Chat with your file** using natural language  
- ⚡ Powered by **OpenRouter LLMs** (default: `mistralai/mixtral-8x7b-instruct`)  
- 🧠 Remembers **chat history** during the session  

---

## 🛠️ Tech Stack  
- **Frontend**: Streamlit  
- **Backend**: Python  
- **AI Models**: OpenRouter API (Mixtral, Mistral, LLaMA, GPT, etc.)  
- **Libraries**:  
  - `pandas` – data analysis  
  - `pypdf`, `fitz`, `pytesseract`, `PIL` – PDF & OCR processing  
  - `python-docx` – Word documents  
  - `chardet` – encoding detection  
  - `openpyxl` – Excel parsing  
  - `dotenv` – API key management  
  - `requests` – API calls  

---

## 📦 Installation  

```bash
# Clone the repository
git clone https://github.com/srinadhs/ai-data-analyst-chatbot.git
cd ai-data-analyst-chatbot

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
