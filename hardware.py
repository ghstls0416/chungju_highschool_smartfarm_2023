import RPI.GPIO as GPIO
import Adafruit_DHT
import time

# 핀 배치들을 변수로 저장해둠
pin_led_first_floor = 1
pin_led_second_floor = 2
pin_heater = 3
pin_pump = 4
pin_water_level_sensor = 5
pin_ph_sensor = 6


# pip install Adafruit_DHT로 DHT 온습도센서 사용 모듈을 설치


# 스마트팜 하드웨어와 소통하는 클래스를 정의
class smartFarm_Device:
    
    def __init__(self):
        '''클래스 초기화'''
        self.start_device()
            

    def start_device(self):
        '''모든 장비들을 초기화하고 장비를 시작함'''
        pass

    def off_device(self):
        '''펌프를 끄고 장비를 정지함'''
        pass

    def get_temp_and_humidity(self)->list[float, float] :
        '''온도 및 습도 측정해 반환하는 함수'''
        pass

    def get_ec(self)->float :
        '''EC(전기전도도) 측정해 반환하는 함수'''
        pass
    def get_ph(self)->float :
        '''ph 측정해 반환하는 함수'''
        pass

    def set_pump_state(self, state:str) :
        '''펌프 작동 상태 설정하는 함수'''
        pass

    def get_pump_state(self)->str :
        '''펌프 작동 상태 반환하는 함수 ('on'/'off')'''
        pass
    def get_water_level(self)->float :
        '''3층 물통 수위 측정해 반환하는 함수'''
        pass
    def set_light_state(self, level:int, state:str) :
        '''1층 혹은 2층 LED 전원 상태를 지정하는 함수'''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.setup(relay_pin, GPIO.OUT)
        pass

    def _set_light_on(self):
        GPIO.output(relay_pin, GPIO.HIGH)
        GPIO.output(led_pin, GPIO.HIGH)
        pass
    def _sel_light_off(self):
        GPIO.output(relay_pin, GPIO.LOW)
        GPIO.output(led_pin, GPIO.LOW)
        pass
    def get_light_state(self)->list[str] :
        '''1층과 2층 LED 전원 상태를 얻어오는 함수 ['on'/'off', 'on'/'off']'''
        pass
    def set_heater_state(self, state:str) :
        '''전체 히터의 상태를 지정하는 함수'''
        pass
    def get_heater_state(self)->str :
        '''히터의 상태를 반환하는 함수 ('on'/'off')'''
        pass
