# AI Agent to Test Websites Automatically Using Natural Language

## 📌 Project Overview
This project implements an AI-powered web testing agent that converts natural language test instructions into structured actions and executes them on websites automatically.

The system is designed to simplify automated testing by allowing users to describe test cases in plain English instead of writing test scripts manually.

---

## 🛠️ Tech Stack
- Python
- Flask (Backend & UI)
- LangGraph (Agent workflow)
- LangChain Community Toolkit
- Playwright (Browser Automation)
- Gradio (Optional UI)

---

# 🏗 Project Structure

ai-agent-web-testing/
│
├── agent/
│   ├── __init__.py
│   ├── langgraph_agent.py   # LangGraph agent configuration
│   └── parser.py            # Natural language instruction parser
│
├── templates/
│   └── index.html            # Flask-based UI
│
├── app.py                    # Main Flask application
├── requirements.txt          # Project dependencies
└── .gitignore


---

## 🚀 Features (Current)
- Accepts natural language test instructions
- Baseline LangGraph agent setup
- Modular architecture for easy extension
- Clean Flask UI for user input

---

## 🔜 Future Enhancements
- Advanced instruction parsing
- Playwright-based browser execution
- Test result reporting (PASS/FAIL)
- UI enhancements and dashboard view

---

## 👩‍💻 Developed By
**Kaya Dhankar**  
B.Tech CSE (AI) 
