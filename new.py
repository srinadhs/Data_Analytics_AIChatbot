import streamlit as st
import pandas as pd
import os
import io
import chardet
from dotenv import load_dotenv
from pypdf import PdfReader
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import docx
import requests

# ─── Load API Key ─────────────────────────────
load_dotenv()
import os
API_KEY = os.getenv("OPENROUTER_API_KEY")
# ─── LLM Query ────────────────────────────────
def ask_llm(prompt, model="mistralai/mixtral-8x7b-instruct"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.7}
    try:
        r = requests.post(url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        # Show full error instead of hiding it
        return f"❌ API Request Failed: {str(e)}\n\nResponse: {getattr(e, 'response', None)}"

# ─── File Readers ─────────────────────────────
def read_pdf(file):
    file.seek(0)
    text = ""
    try:
        reader = PdfReader(file)
        for page in reader.pages:
            if page_text := page.extract_text():
                text += page_text + "\n"
    except:
        file.seek(0)
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text += pytesseract.image_to_string(img) + "\n"
    return text.strip()

def read_docx(file):
    file.seek(0)
    document = docx.Document(file)
    return "\n".join(p.text for p in document.paragraphs)

def read_text(file):
    file.seek(0)
    return file.read().decode("utf-8", errors="ignore")

def read_csv(file):
    file.seek(0)
    raw_data = file.read()
    encoding = chardet.detect(raw_data)["encoding"] or "utf-8"
    file.seek(0)
    return pd.read_csv(io.BytesIO(raw_data), encoding=encoding)

def read_excel(file):
    file.seek(0)
    return pd.read_excel(file)

# ─── Streamlit UI ─────────────────────────────
st.set_page_config(page_title="📊 AI Data Analyst", layout="wide")
st.title("📊 AI Data Analyst")
st.markdown("Upload any file and chat with your data.")

uploaded_file = st.file_uploader("Upload your file", type=None)
file_content, df = None, None

if uploaded_file:
    ext = uploaded_file.name.split(".")[-1].lower()
    readers = {
        "pdf": read_pdf,
        "docx": read_docx,
        "txt": read_text,
        "csv": read_csv,
        "xls": read_excel,
        "xlsx": read_excel
    }
    if ext in readers:
        if ext in ["csv", "xls", "xlsx"]:
            df = readers[ext](uploaded_file)
        else:
            file_content = readers[ext](uploaded_file)
    else:
        st.error("❌ Unsupported file format.")

# ─── Display Content ──────────────────────────
if file_content:
    st.subheader("📄 Extracted Text")
    st.text_area("Text from file", file_content, height=300)

if df is not None:
    st.subheader("📊 Data Preview")
    st.dataframe(df)

# ─── Chat Interface ───────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask about your file...")
if user_input:
    if df is not None:
        context = df.head().to_csv(index=False)
        prompt = f"You are a professional data analyst AI chatbot created by Sreenadh S sample project using OpenRouter API. Introduce yourself first. Here is sample data:\n{context}\n\nQuestion: {user_input}"
    else:
        prompt = f"You are a professional data analyst AI chatbot created by Sreenadh S sample project using OpenRouter API. Introduce yourself first. Here is extracted text:\n{file_content}\n\nQuestion: {user_input}"
    answer = ask_llm(prompt)
    st.session_state.chat_history.append((user_input, answer))
    st.rerun()

for q, a in st.session_state.chat_history:
    st.markdown(f"**🧑 User:** {q}")
    st.markdown(f"**🤖 AI:** {a}")
