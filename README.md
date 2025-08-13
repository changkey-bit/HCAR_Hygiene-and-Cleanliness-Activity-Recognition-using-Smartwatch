# HCAR : Hygiene and Cleanliness Activity Recognition using Smartwatch

---

## <img src="https://img.shields.io/badge/youtube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"> 
Demo Video 
[![HCAR Demo Video](https://img.youtube.com/vi/3KFxsJ4kiP0/0.jpg)](https://youtu.be/3KFxsJ4kiP0)


## ⏱️ Hygiene and Cleanliness Activities
<img src="https://github.com/user-attachments/assets/6ca6c93e-4964-4aaf-bf86-a4cc0154c2f3">

## ⏱️ Results
<img src="https://github.com/user-attachments/assets/b56f9fbb-e3c0-4c6e-9dd7-ae4ca248cc52">

---

## 📑 프로젝트 소개
### 👤 On-device 실시간 위생 및 청결 행동 인식 시스템
1. **HCAR 시스템 개발**  
   - IMU와 오디오 데이터를 활용하여 스마트워치에서 실시간 행동 인식 수행  

2. **데이터 수집**  
   - **Phase 1**: 4명의 피험자가 통제된 환경에서 일정 시간 동일 행동 반복 수행  
   - **Phase 2**: 10명의 피험자가 실생활 환경에서 위생 및 청결 행동 수행  
   - 총 수집 데이터:  
     - 통제 환경: 약 2,144분  
     - 실생활 환경: 약 4,578분  

3. **개인화 모델 학습**  
   - 각 개인별 데이터를 Train / Validation / Test로 분리  
   - Train 데이터 양을 점진적으로 늘려 최적 데이터량 도출  
   - 행동 당 **420초**의 학습 데이터 사용 시, 90% 이상의 인식 성능 확인  
   - Validation 데이터: Train 직후 10초 구간  
   - Test 데이터: 전체 데이터의 마지막 30%  

4. **실시간 인식 및 저장**  
   - 이벤트 발생 시 IMU(50Hz)와 Audio(16kHz) 동시 수집  
   - 실시간 추론 후 Raw 데이터 및 예측 결과를 기기 로컬 스토리지에 저장  

---

> **특징**  
> - **다중 모달 데이터**(IMU + Audio)를 활용한 행동 인식  
> - **On-device 학습 및 추론**을 통한 개인정보 보호  
> - **개인화(Personalization)** 적용으로 사용자의 특성을 반영한 성능 향상  
> - 실시간 데이터 수집·처리·추론까지 원스톱 수행  

---

## 🛠 사용 기술 스택
- **Language** : Python  
- **Models** : TensorFlow, TensorFlow Lite, Scikit-Learn, ONNX  
- **Architecture** : Multi-CNN + Random Forest  
- **Device** : Samsung Galaxy Watch 4, Galaxy Watch Ultra  

---

🔗 **실시간 인식 앱** : [On-device_HCAR_RealTime](https://github.com/changkey-bit/On-device_HCAR_RealTime)  
🎥 **데모 비디오** : [YouTube 링크](https://youtu.be/3KFxsJ4kiP0)
