
from google import genai

client = genai.Client()

print("MODELOS DISPONIBLES:\n")

for modelo in client.models.list():
    metodos = modelo.supported_actions or []
    if "generateContent" in metodos:
        print(modelo.name)
