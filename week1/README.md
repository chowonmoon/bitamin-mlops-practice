# 1주차 - 재현 가능한 ML 개발환경 (연습)

## 체크포인트 1: conda 가상환경 생성 및 activate
**명령어**
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda create -n churn-mlops python=3.10 -y
conda activate churn-mlops

**결과**: 프롬프트가 (base) → (churn-mlops)로 변경 확인
**막힌 점**: conda create 시 CondaToSNonInteractiveError 발생 → conda tos accept로 해결

## 체크포인트 2: requirements.txt 작성 및 설치
**명령어**
nano requirements.txt   (pandas, scikit-learn, joblib)
pip install -r requirements.txt

**결과**: pip list에 세 패키지 및 의존 패키지 전부 설치 확인

## 체크포인트 3: baseline 모델 실행
**명령어**: python train.py
**결과**: Accuracy: 0.8160 (ConvergenceWarning 발생했으나 결과 출력에는 지장 없음)

## 체크포인트 4: Dockerfile 작성 및 이미지 빌드
**명령어**
docker build -t churn-mlops-week1 .
docker images

**결과**: churn-mlops-week1:latest (630MB) 확인

## 체크포인트 5: 컨테이너에서 baseline 모델 실행
**명령어**: docker run churn-mlops-week1
**결과**: Accuracy: 0.8160 (로컬과 동일한 결과, 컨테이너 재현성 확인)

---

## 심화 1: Docker Hub push
**명령어**
docker tag churn-mlops-week1 moonchowon/churn-mlops-week1
docker login
docker push moonchowon/churn-mlops-week1

**결과**: 전체 레이어 Pushed 완료

## 심화 2: .dockerignore 적용
**명령어**
nano .dockerignore   (__pycache__/, *.pyc, .git, .gitignore, README.md)
docker build -t churn-mlops-week1-v2 .

**결과**: 용량 동일(630MB) - 원래 불필요 파일이 없어 체감 차이 없었으나 설정 자체는 정상 반영

## 심화 3: environment.yml 내보내기 및 복원
**명령어**
conda env export > environment.yml
conda env create -n churn-mlops-restored -f environment.yml
conda env list

**결과**: churn-mlops, churn-mlops-restored 둘 다 목록에 표시 → 동일 환경 복제 검증 완료
