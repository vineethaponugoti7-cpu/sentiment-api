import pickle
from fastapi import FastAPI
from pydantic import BaseModel

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = FastAPI(title="Sentiment Analysis API")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running. Use POST /predict."}

@app.post("/predict")
def predict(input: TextInput):
    features = vectorizer.transform([input.text])
    prediction = model.predict(features)[0]
    return {"text": input.text, "sentiment": prediction}