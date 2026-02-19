# 💰 AI Financial Advisor Chatbot

An AI-powered Financial Advisor Chatbot built using **Python**, **Streamlit**, and **Gemini API**.  
The application provides real-time financial guidance through a conversational interface with session-based memory handling.

---

## 🚀 Features

- 💬 Real-time financial query handling using LLM integration  
- 🧠 Session-based conversation memory  
- 🏗 Modular architecture (services, prompts, memory, UI)  
- ⚡ Optimized API response handling  
- ☁️ Cloud deployment ready (AWS EC2 supported)  
- 🔐 Environment-based configuration management  

---

## 🛠 Tech Stack

- Python  
- Streamlit  
- Gemini API (LLM Integration)  
- Git & GitHub  
- AWS EC2  

---

## 📂 Project Structure

```
Finance_Chatbot/
│
├── app.py
├── services/
│   └── gemini_service.py
├── prompts/
│   └── financial_prompts.py
├── memory/
│   └── session_memory.py
├── config/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/pradeep-dev-ai/Finance_Chatbot.git
cd Finance_Chatbot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory and add:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in your browser:

```
http://localhost:8501
```

---

## ☁️ Deployment on AWS EC2

1. Launch an Ubuntu EC2 instance  
2. Open port **8501** in the security group  
3. Install Python, pip, and Git  
4. Clone the repository  
5. Run:

```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

Access the application:

```
http://your-public-ip:8501
```

---

## 📌 Use Cases

- Financial guidance and investment basics  
- Budget planning queries  
- AI-powered financial insights  
- Interactive conversational assistance  

---

## 📈 Future Improvements

- User authentication system  
- Database integration  
- Multi-user support  
- Docker containerization  
- Domain and HTTPS setup  

---

## 👨‍💻 Author

**Kurmala Pradeep Gupta**  
AI/ML Enthusiast | Python Developer  

GitHub: https://github.com/pradeep-dev-ai
