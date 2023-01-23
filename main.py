import openai

# Configurar credenciales de acceso a la API de OpenAI
openai.api_key = "sk-"

# Define la pregunta a hacerme
question = f"""
            Podrías decirme qué cambios se están haciendo en lo siguiente:
            
            """

# Llama al modelo y obtiene la respuesta
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=(question),
    max_tokens=1024,
    n =1,
    stop=None,
    temperature=0.5
)

# Imprime la respuesta
print(response["choices"][0]["text"])