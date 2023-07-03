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
        {"role": "system", "content": """Eres una calculador factoial y das el factorial del numero que te dan si te dan un texto imprimes "sintax error"
        """},
        {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print("[TERMINE DE PROCESAR]".center(40, "-"))
    return [content, total_tokens]
