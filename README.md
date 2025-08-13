# HCAR : Hygiene and Cleanliness Activity Recognition using Smartwatch

---

## ⏱️ Hygiene and Cleanliness Activities
<img src="https://github.com/user-attachments/assets/6ca6c93e-4964-4aaf-bf86-a4cc0154c2f3">

## ⏱️ Results
<img src="https://github.com/user-attachments/assets/b56f9fbb-e3c0-4c6e-9dd7-ae4ca248cc52">

---

## 📑 프로젝트 소개
### 👤 On-device 실시간 위생 및 청결 행동 인식
1. HCAR (Hygiene and Cleanliness Activity Recognition system) 개발
   - IMU, Audio 데이터를 통한 
   
3. **데이터 전처리 및 분류**  
   - 수집된 IMU 데이터를 전처리 후 **Multi-input CNN 모델**에 입력  
   - **휠체어를 포함한 7가지 이동 수단 클래스**로 분류  
     *(Still, Walking, Manual Wheelchair, Power Wheelchair, Metro, Bus, Car)*  

4. **결과 저장**  
   - Raw 데이터 및 예측 결과를 기기 내 로컬 스토리지에 저장

---

> **특징**  
> - 스마트폰 단독(On-device)으로 네트워크 연결 없이 실시간 이동 수단 인식 가능  
> - 4종 IMU 센서 융합으로 높은 분류 정확도 확보  
> - 휠체어 포함 교통수단 분류 가능 → 교통약자 이동 패턴 분석에도 활용 가능  
> - TensorFlow Lite 변환을 통한 경량화로 모바일 환경 최적화  
> - 데이터 수집부터 예측까지 전 과정을 **5초 이내**에 수행  

---

## 🛠 사용 기술 스택
- **Language** : Python  
- **Models** : TensorFlow, TensorFlow Lite  
- **Architecture** : Multi-input CNN  
- **Device** : Samsung Galaxy S22+

실시간 인식 앱 링크: https://github.com/changkey-bit/On-device_HCAR_RealTime
데모 비디오 링크: https://youtu.be/3KFxsJ4kiP0
