import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. 데이터 로드
df = pd.read_csv("Churn_Modelling.csv")

# 2. 학습에 쓰지 않을 컬럼 제거
df = df.drop(columns=["RowNumber", "CustomerId", "Surname"])

# 3. 범주형 변수 인코딩
for col in ["Geography", "Gender"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# 4. 입력(X)과 타깃(y) 분리
X = df.drop(columns=["Exited"])
y = df["Exited"]

# 5. 학습/테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. 모델 학습
model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

# 7. 평가
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")
