import streamlit as st
import os
import pandas as pd
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Screening", layout="centered")
st.title("📄 AI Resume Screening System")

def extract_text_from_docx(file):
    doc = Document(file)
    return " ".join([p.text for p in doc.paragraphs])

jd = st.text_area("Paste Job Description")

uploaded_files = st.file_uploader(
    "Upload Resume Files (.docx)",
    type=["docx"],
    accept_multiple_files=True
)

if st.button("Screen Resumes") and uploaded_files:
    resumes = []
    for file in uploaded_files:
        text = extract_text_from_docx(file)
        resumes.append(text)

    vectorizer = TfidfVectorizer(max_features=3000)
    resume_vectors = vectorizer.fit_transform(resumes)
    jd_vec = vectorizer.transform([jd])

    scores = cosine_similarity(resume_vectors, jd_vec).flatten()

    result_df = pd.DataFrame({
        "Resume": [f.name for f in uploaded_files],
        "Match %": scores * 100
    })

    st.dataframe(result_df.sort_values("Match %", ascending=False))
