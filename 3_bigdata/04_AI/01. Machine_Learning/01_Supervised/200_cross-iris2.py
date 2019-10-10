# 목적: 교차검증(Cross Validation) 라이브러리 활용

import pandas as pd
from sklearn import svm, model_selection
# 붗꽃의 CSV 데이터 읽어 들이기 ---(*1)
csv = pd.read_csv('iris.csv')
# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할하기 ---(*2)
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]

# 머신 러닝 모델 생성 ---(*3)
clf = svm.SVC(gamma='auto')

# 크로스 밸리데이션 생성하기 ---(*4)
scores = model_selection.cross_val_score(clf, data, label, cv = 5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())