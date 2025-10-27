import pickle
import uvicorn

from fastapi import FastAPI
from typing import Dict, Any

#load model
#with open("pipeline_v1.bin", "rb") as pipe_in:
with open("pipeline_v2.bin", "rb") as pipe_in:
    pipeline = pickle.load(pipe_in)

#predict single observation
def predict_single(observation):
    score = pipeline.predict_proba(observation)[0, 1]
    return float(score)

predict_churn_telco = FastAPI(title="predict_churn_telco")

@predict_churn_telco.post("/predict_churn_telco")
def predict(observation: Dict[str, Any]):
    score = predict_single(observation)
    return {"score": score, "is_churn": bool(score >= 0.5)}

def main():
    uvicorn.run("main:predict_churn_telco", host="0.0.0.0", port=4444)
    #uvicorn.run("main:predict_churn_telco", host="127.0.0.1", port=4444)

if __name__ == "__main__":
    main()