# 📄 AI Resume Screening System

An AI-powered resume screening application that evaluates and ranks candidates based on how well their resumes match a given job description. The system uses NLP techniques and machine learning to simulate real-world Applicant Tracking Systems (ATS).

---

## 🚀 Project Overview

Recruiters often receive a large number of resumes for a single job opening. Manually reviewing each resume is time-consuming and prone to bias.  
This project automates the resume screening process by:

- Reading real resumes in **Word (.docx) format**
- Comparing them with a **job description**
- Generating a **match percentage**
- Ranking candidates based on relevance
- Providing **explainable AI output** (matched & missing skills)

---

## 🎯 Objectives

- Automate resume screening using NLP
- Rank candidates based on job relevance
- Extract key skills from resumes
- Provide transparent and explainable results
- Mimic real-world ATS behavior

---

## 📂 Dataset

- Source: **Kaggle**
- Content: **20 full resumes**
- Format: **Word documents (.docx)**
- Type: Unlabeled, real-world resume text

---

## 🧠 Methodology

### 1. Resume Text Extraction
- Extract text from Word (.docx) resumes using `python-docx`

### 2. Text Preprocessing
- Lowercasing
- Removing punctuation and numbers
- Stopword removal

### 3. Feature Extraction
- TF-IDF Vectorization to convert text into numerical features

### 4. Resume–Job Matching
- Cosine Similarity to measure semantic similarity between resumes and job description

### 5. Candidate Ranking
- Rank resumes based on similarity scores

### 6. Explainable AI
- Identify matched and missing skills for each resume

---

## 📊 Output

- Match percentage for each resume
- Ranked list of candidates
- Skills found in each resume
- Missing skills compared to job description

---

## 🖥️ Application Interface

- Upload multiple resume files (.docx)
- Paste job description
- Click “Screen Resumes”
- View ranked results in tabular format

---

## 🛠️ Technologies Used

- Python
- Natural Language Processing (NLP)
- Scikit-learn
- NLTK
- TF-IDF Vectorization
- Cosine Similarity
- Streamlit
- python-docx
- Pandas

---

## 📁 Project Structure

