import requests
import json
from duckduckgo_search import DDGS


# 🔍 Get latest data ONLY
def search_web(query):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)

        latest_info = ""
        for r in results:
            latest_info += f"{r['body']}\n"

        return latest_info


# 🤖 Generate answer (NO OLD DATA)
def generate_stream(question):
    latest_data = search_web(question)

    prompt = f"""
Answer the question using ONLY the latest information below.

Rules:
- Do NOT use old knowledge
- Do NOT guess
- Keep answer short and accurate
- If data is missing, say "No latest data found"

Latest Information:
{latest_data}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": 0.0   # 🔥 very accurate
            }
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            yield data.get("response", "")
