from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
classifier = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str
    
"""@app.post("/predict")
def predict(data: TextInput):
    result = classifier(data.text)[0]
    return {"label":result['label'], "score": round(result['score'], 2)}"""
    
@app.get("/predict")
def predict():
    # Simulate a failure
    raise Exception("Simulated crash")

@app.get("/health")
def health_check():
    return {"status": "ok"}