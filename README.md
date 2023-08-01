# chugnju_highschool_smartfarm_2023
충주고 3학년 학생들의 스마트팜 제작 프로젝트 레포지토리  

# 하드웨어
## 하드웨어 구성 요소
 1. 온습도센서 4개
 2. ESP32-CAM 1개 -> 전원 공급해 자체 구동하고 이미지 서버에 스트리밍 하도록
 3. EC센서 1개
 4. PH센서 1개
 5. 펌프 1개
 6. A, B, C통 배관 조작 장치 각각 1개씩
 7. 수위센서 1개
 8. LED strip 8개 -> 릴레이로 조작
 9. 온도 조절등(등은 아닌데 그런 장치) 4개 -> 릴레이로 조작

## hardware.py (라즈베리파이 GPIO 모듈로 하드웨어 조작) 
- get_temp_and_humidity() : 온도 및 습도 측정해 반환하는 함수
- get_ec() : EC(전기전도도) 측정해 반환하는 함수
- get_ph() : ph 측정해 반환하는 함수
- set_pump_state() : 펌프 작동 상태 설정하는 함수
- get_pump_state() : 펌프 작동 상태 반환하는 함수
- get_water_level() : 3층 물통 수위 측정해 반환하는 함수
- set_light_state()
- get_light_state()
- set_heater_state()
- get_heater_state() 

# 서버 호스팅/웹사이트
# server.py(flask 라이브러리로 서버 운영)

# webpage(html/css 스택으로 웹페이지 UI 제작)
