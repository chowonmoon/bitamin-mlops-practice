from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_predict():
    sample_data = {
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
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    result = response.json()
    assert "prediction" in result
    assert result["prediction"] in ["이탈", "유지"]
    assert 0 <= result["probability"] <= 1
