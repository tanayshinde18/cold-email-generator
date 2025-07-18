# 📧 Cold Email Generator with LangChain, Streamlit & ChromaDB

Welcome to the **Cold Email Generator** — an AI-powered Streamlit application that:

- Scrapes a job/career page URL  
- Extracts relevant job listings using LLMs  
- Queries your portfolio (stored in a vector database)  
- Generates **tailored cold emails** you can send to potential clients or employers!

---


## 📌 Features

✅ Scrapes job descriptions from career pages  
✅ Extracts structured job information using LLMs  
✅ Matches job requirements with your portfolio (stored in ChromaDB)  
✅ Generates customized cold emails using your capabilities  
✅ Streamlit-powered clean and interactive frontend  
✅ Easy `.env`-based configuration for API keys & secure environment

---

## 🧠 Tech Stack & Concepts

- **🔗 LangChain**: Framework for building applications with LLMs (used to prompt LLaMA model to extract info and generate emails)
- **🧠 Groq API (LLaMA-3)**: Fast inference API for Meta’s open-source LLMs
- **📊 ChromaDB**: Simple, local vector database to store and query your portfolio based on semantic similarity
- **📇 Pandas**: Reads your portfolio file (CSV) during initialization
- **🌐 Streamlit**: Frontend framework to make the LLM tool interactive and user-friendly

---

## 🧰 Project Structure

```
cold-email-generator/
├── app/
│   └── resources/
│       └── my_portfolio.csv        # Your personal portfolio CSV
├── vectorstore/                    # Vector database created by ChromaDB
├── chains.py                       # Contains the LLM prompts and logic
├── portfolio.py                    # Loads and queries vector database
├── utils.py                        # Text cleaning, optional utilities
├── main.py                         # Streamlit app entry point
├── .env.example                    # Template for safe API key configuration
├── .gitignore                      # Excludes sensitive files from Git
└── README.md                       # This file
```

---

## 🚀 How to Use (Run Locally)

### 1. 🔃 Clone the Repository

```bash
git clone https://github.com/yourusername/cold-email-generator.git
cd cold-email-generator
```

### 2. 🐍 Create Virtual Environment & Install Dependencies

```bash
python -m venv env
# For Windows
env\Scripts\activate
# For Mac/Linux
source env/bin/activate

pip install -r requirements.txt
```

### 3. ⚙️ Add Environment Variables

Create a `.env` file in the root folder using `.env.example` as a template and add your Groq API key:

```bash
GROQ_API_KEY=your_actual_key_here
```

### 4. 🏁 Run Streamlit Application

```bash
streamlit run main.py
```

---

## ⚡ How to Create Your GROQ API Key

1. Visit [Groq Console](https://console.groq.com/keys)  
2. Sign up or log in  
3. Click **"Create API Key"**  
4. Copy the key and add it to your `.env`:

```env
GROQ_API_KEY=your_key_here
```

> 🔐 **Important**: Never share your `.env` file or commit it to GitHub!

---

## 🧾 Example: Portfolio Format (`my_portfolio.csv`)

Your CSV must contain the following columns:

```text
Techstack,Links
"AI, Python, Streamlit", https://yourportfolio.com/project-1
"Data, FastAPI, ML", https://yourportfolio.com/project-2
```

Each row maps your skills to a project link, which will be included in the generated email.

---

## 📬 Workflow Summary

1. User enters a job/career page URL in the app  
2. Web page is scraped & cleaned using **WebBaseLoader** & `clean_text`  
3. LangChain prompt sends the cleaned content to Groq LLM to extract job roles  
4. Skills in each role are used to find matching projects from your portfolio (via ChromaDB)  
5. A final prompt generates a tailored cold email using your matched projects  
6. The email is shown with Markdown formatting

---

## ✔️ Tips for Best Results

- Keep your portfolio CSV clean, rich with diverse skill keywords
- Avoid submitting invalid or blank job URLs
- Use faster LLM models like `llama-3.1-8b-instant`
- Run in environments with good internet & compute for lower latency

---

## 🚧 Future Improvements

- ✅ File upload support for resumes or portfolio PDFs  
- ✅ Support for multiple Groq models and OpenAI fallback  
- ✅ Save generated emails to local file/db  
- ✅ Add email formatting (Rich HTML, plain text toggle)  
- ✅ Deploy to Streamlit Cloud or similar  
- ✅ Allow live prompt tweaking from UI  
- ✅ Multilingual support for global outreach

---

Made with ❤️ using LangChain, Groq, and Streamlit
