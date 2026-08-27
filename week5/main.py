from fastapi import FastAPI
from schema import CustomerData
import joblib
import pandas as pd

app = FastAPI()

# 서버 시작 시 딱 한 번만 모델 로드
model = joblib.load("churn_model.joblib")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/predict")
def predict(data: CustomerData):
    # 1. 받은 데이터를 DataFrame으로 변환 (학습 때와 같은 형식으로)
    input_df = pd.DataFrame([data.model_dump()])
    
    # 2. 범주형 컬럼을 학습 때와 동일하게 숫자로 변환
    input_df["Geography"] = input_df["Geography"].map({"France": 0, "Germany": 1, "Spain": 2})
    input_df["Gender"] = input_df["Gender"].map({"Female": 0, "Male": 1})
    
    # 3. 예측
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    
    # 4. 결과 반환
    return {
        "prediction": "이탈" if prediction == 1 else "유지",
        "probability": round(float(probability), 4)
    }
