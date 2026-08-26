# 3주차 - WandB 실험 관리 (연습)

## 사전 세팅
- WandB 회원가입, API Key 발급, `pip install wandb`, `wandb login` 완료

## 체크포인트 1: WandB 프로젝트 생성
`wandb.init(project="churn-mlops-practice", ...)` 코드로 프로젝트 자동 생성

## 체크포인트 2: config와 metric이 기록된 run 생성
`wandb.init()`에 config(모델, 하이퍼파라미터), `wandb.log()`에 metric(accuracy 등) 기록

## 체크포인트 3: 최소 6개 run 실행
| Run | 모델 | 하이퍼파라미터 |
|---|---|---|
| logistic-regression-baseline | LogisticRegression | max_iter=1000 |
| logistic-regression-iter2000 | LogisticRegression | max_iter=2000 |
| logistic-regression-iter3000 | LogisticRegression | max_iter=3000 |
| random-forest-depth5 | RandomForestClassifier | max_depth=5 |
| random-forest-depth10 | RandomForestClassifier | max_depth=10 |
| random-forest-depth20 | RandomForestClassifier | max_depth=20 |

참고: 이번 연습에서는 ROC-AUC 계산을 생략했으나, 실제 세션에서는 통과 기준에 필요한 지표(Accuracy/Precision/Recall/F1/ROC-AUC 등)를 처음부터 코드에 전부 포함시켜 한 번의 실행으로 누락 없이 기록해야 함

## 체크포인트 4: 대시보드에서 하이퍼파라미터별 성능 비교

| Run | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| random-forest-depth20 | 0.870 | 0.783 | 0.468 | 0.586 |
| random-forest-depth10 | 0.863 | 0.767 | 0.435 | 0.555 |
| random-forest-depth5 | 0.858 | 0.797 | 0.369 | 0.504 |
| logistic-regression-iter3000 | 0.815 | 0.600 | 0.176 | 0.272 |
| logistic-regression-iter2000 | 0.817 | 0.613 | 0.186 | 0.285 |
| logistic-regression-baseline | 0.816 | 0.598 | 0.193 | 0.292 |

WandB 프로젝트 링크: https://wandb.ai/chowonmoon-dongduk-women-s-university/churn-mlops-practice

## 체크포인트 5: best model 선정
**선정 모델**: random-forest-depth20 (RandomForestClassifier, max_depth=20)

**선정 근거**: Accuracy(0.870)와 Recall(0.468) 모두 6개 run 중 최고치. 이탈 예측에서는 이탈 고객을 놓치지 않는 것이 중요해 Recall이 핵심 지표인데, RandomForest 계열이 LogisticRegression 계열보다 전반적으로 Recall이 높았고 그중에서도 max_depth=20이 가장 우수함. Precision(0.783), F1(0.586)도 6개 run 중 최고 수준으로 준수.

`churn_model.joblib`으로 저장 완료

