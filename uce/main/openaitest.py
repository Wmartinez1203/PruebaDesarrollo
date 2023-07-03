import openai
from pydantic import BaseModel

class document(BaseModel):
    prompt: str = ''
def deduccion(prompt: str) -> list:
    openai.organization = "org-ZWY7hnVw2WOKBgUCbZnaiRrz"
    openai.api_key = "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"
    print("[PROCESANDO SU PETICION]".center(40, "-"))

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": """Eres un profesor de programación para niños de 5 años, genera una explicacion para el tema que se te proporciona
        E.G: Programación        
        -Es como armar un rompecabezas donde cada pieza forma el sistema completo"""},
        {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print("[TERMINE DE PROCESAR]".center(40, "-"))
    return [content, total_tokens]
