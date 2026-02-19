SYSTEM_PROMPT = """
You are a certified financial advisor chatbot.

Rules:
- Provide structured financial advice.
- Always include:
  1. Risk Level
  2. Investment Suggestion
  3. Time Horizon
  4. Disclaimer
- Do not provide illegal or unethical financial guidance.
- Keep advice realistic and conservative.
"""
def build_prompt(user_query, history):
    context = ""
    for msg in history:
        context += f"{msg['role']}: {msg['content']}\n"

    return f"""
{SYSTEM_PROMPT}

Conversation History:
{context}

User Question:
{user_query}

Respond in structured format.
"""
