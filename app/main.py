import os
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
model_name = os.getenv("MODEL_NAME", "distilbert/distilbert-base-uncased-finetuned-sst-2-english")
classifier = pipeline("sentiment-analysis", model=model_name)

class TextInput(BaseModel):
    text: str
    
@app.post("/predict")
def predict(data: TextInput):
    result = classifier(data.text)[0]
    return {"label":result['label'], "score": round(result['score'], 2)}
    
"""@app.get("/predict")
def predict():
    # Simulate a failure
    raise Exception("Simulated crash")"""

@app.get("/health")
def health_check():
    return {"status": "ok"}