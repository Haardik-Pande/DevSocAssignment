import google.generativeai as genai
import json

API_KEY = "myapikey(removedduetosecurityconcerns)" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

with open('text.txt', 'r', encoding='utf-8') as file:
    questions = [line.strip() for line in file if line.strip()]

responses = []

for question in questions:
    response = model.generate_content(question)
    responses.append({
        "prompt": question,
        "response": response.text
    })

with open('responses.json', 'w', encoding='utf-8') as f:
    json.dump(responses, f, indent=2, ensure_ascii=False)

print("All responses saved to 'responses.json'")
