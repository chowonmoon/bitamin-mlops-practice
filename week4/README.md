# 4주차 - FastAPI 모델 서빙 (연습)

## 체크포인트 1: FastAPI 서버 기동 및 Swagger 접속
**명령어**: `uvicorn main:app --reload`
**결과**: `http://127.0.0.1:8000/docs`에서 Swagger 화면 정상 확인 (GET / Read Root 엔드포인트 표시)

## 체크포인트 2: 고객 정보 입력용 Pydantic 스키마 정의
`schema.py`에 `CustomerData` 클래스로 고객 정보 10개 항목(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary) 정의
**결과**: Swagger의 Schemas 섹션에 `CustomerData` 정상 표시

## 체크포인트 3: churn_model.joblib 로드 및 /predict 구현
`main.py`에서 서버 시작 시 모델을 1회만 로드(`joblib.load`), `/predict` 엔드포인트에서 입력 데이터를 학습 시와 동일하게 전처리 후 예측 수행
**결과**: 서버 정상 기동 (`Application startup complete`)

## 체크포인트 4: Swagger에서 예측 요청 성공
Swagger "Try it out"으로 두 가지 상반된 조건의 가상 고객 테스트
**결과**:
- 안정적 고객(신용점수 650, 활성 고객 등) → 유지, 확률 0.04
- 위험 신호 고객(신용점수 400, 비활성 고객 등) → 이탈, 확률 0.86

## 체크포인트 5: Postman으로 동일 요청 테스트
Postman에서 동일한 POST 요청 재현
**결과**: 200 OK, Swagger와 동일한 응답 확인 (`{"prediction": "유지", "probability": 0.04}`)

---

## API 명세

### POST /predict

**입력 예시**
```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Male",
  "Age": 40,
  "Tenure": 5,
  "Balance": 50000,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 60000
}
```

**출력 예시**
```json
{
  "prediction": "유지",
  "probability": 0.04
}
```

- `prediction`: "이탈" 또는 "유지"
- `probability`: 이탈 확률 (0~1)# 4주차 - FastAPI 모델 서빙 (연습)

## 체크포인트 1: FastAPI 서버 기동 및 Swagger 접속
**명령어**: `uvicorn main:app --reload`
**결과**: `http://127.0.0.1:8000/docs`에서 Swagger 화면 정상 확인 (GET / Read Root 엔드포인트 표시)

## 체크포인트 2: 고객 정보 입력용 Pydantic 스키마 정의
`schema.py`에 `CustomerData` 클래스로 고객 정보 10개 항목(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary) 정의
**결과**: Swagger의 Schemas 섹션에 `CustomerData` 정상 표시

## 체크포인트 3: churn_model.joblib 로드 및 /predict 구현
`main.py`에서 서버 시작 시 모델을 1회만 로드(`joblib.load`), `/predict` 엔드포인트에서 입력 데이터를 학습 시와 동일하게 전처리 후 예측 수행
**결과**: 서버 정상 기동 (`Application startup complete`)

## 체크포인트 4: Swagger에서 예측 요청 성공
Swagger "Try it out"으로 두 가지 상반된 조건의 가상 고객 테스트
**결과**:
- 안정적 고객(신용점수 650, 활성 고객 등) → 유지, 확률 0.04
- 위험 신호 고객(신용점수 400, 비활성 고객 등) → 이탈, 확률 0.86

## 체크포인트 5: Postman으로 동일 요청 테스트
Postman에서 동일한 POST 요청 재현
**결과**: 200 OK, Swagger와 동일한 응답 확인 (`{"prediction": "유지", "probability": 0.04}`)

---

## API 명세

### POST /predict

**입력 예시**
```json
{
  "CreditScore": 650,
  "Geography": "France",
  "Gender": "Male",
  "Age": 40,
  "Tenure": 5,
  "Balance": 50000,
  "NumOfProducts": 2,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 60000
}
```

**출력 예시**
```json
{
  "prediction": "유지",
  "probability": 0.04
}
```

- `prediction`: "이탈" 또는 "유지"
- `probability`: 이탈 확률 (0~1)
