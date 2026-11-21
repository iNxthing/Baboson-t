from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
 
app = FastAPI(title="Baboso")
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 
Preguntas = [
    {
        "id": "p1",
        "text": "Te le vantas de la cama y te quedas mirando un Punto Fijo?",
        "options": [
            {"id": "a", "text": "Si", "score": 8},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p2",
        "text": "Cuando te estan hablando te les quedas viendo sin entender una mierda?",
        "options": [
            {"id": "a", "text": "Si", "score": 15},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p3",
        "text": "Has abierto la nevera varias veces y aun asi sabiendo que no hay nada sigues abriendola?",
        "options": [
            {"id": "a", "text": "Si", "score": 12},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p4",
        "text": "Has entrado a una habitacion y se te olvido que carajos ibas a hacer??",
        "options": [
            {"id": "a", "text": "Si", "score": 18},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p5",
        "text": "Has tratado de 'enfriar' un helado soplandolo porque esta muy 'Frio'? ",
        "options": [
            {"id": "a", "text": "Si", "score": 20},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p6",
        "text": "Te has puesto a buscar el celular mientras lo tenías en la mano?",
        "options": [
            {"id": "a", "text": "Si", "score": 14},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p7",
        "text": "SI?",
        "options": [
            {"id": "a", "text": "Si", "score": 17},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p8",
        "text": "Haz intentado Cerrar la nevera lentamente para ver como se apaga el foco de adentro?",
        "options": [
            {"id": "a", "text": "Si", "score": 16},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p9",
        "text": "Haz hecho burbujas en el baso con un pitillo(pajita , popote , vamos bro como se diga en tu pais)?",
        "options": [
            {"id": "a", "text": "Si", "score": 19},
            {"id": "b", "text": "No", "score": 0},
        ],
    },
    {
        "id": "p10",
        "text": "Haz intentado probar si el pegamento pega?",
        "options": [
            {"id": "a", "text": "Si", "score": 12},
            {"id": "b", "text": "No", "score": 0},
        ],
    }
]
 
 
class RespuestaIngresada(BaseModel):
    questionId: str
    optionId: str
 
 
class ResultadoIngresada(BaseModel):
    answers: list[RespuestaIngresada]   # <- antes "respuestas"; el front manda "answers"
 
 
class RegresarResultado(BaseModel):
    percentage: int
    title: str
    description: str
 
 
@app.get("/api/quiz/questions")
def obrener_preguntas():
    return Preguntas
 
 
@app.post("/api/quiz/result")
def enviar_resultado(datos: ResultadoIngresada):
    score = 0
    max_score = 0
 
    for respuesta in datos.answers:            # <- iterar sobre answers
        pregunta_id = respuesta.questionId     # <- de respuesta, no de datos
        opcion_id = respuesta.optionId         # <- de respuesta, no de datos
 
        for pregunta in Preguntas:
            if pregunta["id"] == pregunta_id:
                for opcion in pregunta["options"]:
                    if opcion["id"] == opcion_id:
                        score += opcion["score"]
                max_score += max(o["score"] for o in pregunta["options"])
 
    porcentaje = round(score / max_score * 100) if max_score else 0
 
    def definir_titulo(p):
        if p <= 25:
            return "Mente maestra (o estás mintiendo)."
        if p <= 50:
            return "Distraído funcional."
        if p <= 75:
            return "Baboso certificado."
        return "Peligro público."

    def definir_descripcion(p):
        if p <= 25:
            return "No te pasa ni una."
        if p <= 50:
            return "Tu cerebro tiene lag de vez en cuando, pero sobrevives."
        if p <= 75:
            return "Es un milagro que no te hayas extinguido todavía."
        return "Necesitas supervisión de un adulto responsable las 24 horas."

    return {
        "percentage": porcentaje,
        "title": definir_titulo(porcentaje),
        "description": definir_descripcion(porcentaje),
    }
