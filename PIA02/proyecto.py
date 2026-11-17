
from google import genai

# Cliente Gemini: utiliza GEMINI_API_KEY
client = genai.Client(
    http_options={"timeout": 30000}
)

# Modelo seleccionado
modelo = "gemini-3.5-flash-lite"

# Primera consulta
#prompt = (
#    "Explica brevemente qué es el aprendizaje automático "
#    "y pon un ejemplo sencillo de su aplicación."
#)

# Segunda consulta
prompt = (
    "Indica tres aplicaciones prácticas de la inteligencia artificial "
    "en una empresa de alojamiento turístico y explica brevemente "
    "para qué serviría cada una."
)

print("PROMPT:")
print(prompt)

respuesta = client.models.generate_content(
    model=modelo,
    contents=prompt
)

print("\nRESPUESTA DE GEMINI:")
print(respuesta.text)
