from typing import Union

from fastapi import FastAPI

from uce.main.openaitest import document, deduccion

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/deduccion",status_code=200)
def deduccion_endpoint(doc: document):
    response = deduccion(doc.prompt)
    return {
        "Respuesta":response[0],
        "Tokens usados": response[1]
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=9066)

#para cambiar el puerto
#if __name__ == "__main__":
#    app.host()