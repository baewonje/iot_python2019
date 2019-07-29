import threading
import time
import ctypes
import datetime
import urllib.request
import json
schedule_cycle = 5
g_Radiator = False
g_Gas_Valve = False
g_Balcony_windows = False
g_Door = False
g_AI_Mode = False

def terminate_ai_mode():
    """Terminates a python Thread from another thread.
    :param thread: a threadint.Thread instance
    """
    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent Thread id")
    elif res > 1:
        # """ if it returns a number greater than one, you're in trouble,
        # and you shoud call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsynceExc failed")

def update_scheduler():
    while True:
        time.sleep(schedule_cycle)
        print(f"스케줄러 작동.. {schedule_cycle}초 주기")
        get_Realtime_Weather_Info()

def print_main_menu():
        print("메뉴를 선택하세요")
        print("1. 장비 상태 조회")
        print("2. 인공지능 모드 변경")
        print("3. 종료")

def print_device_status(device_name,device_status):
    print("%s 상태: "%device_name, end="")
    if device_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print('')
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브',g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_windows)
    print_device_status('출입문 상태',g_Door)

def get_Request_URL(url):
    # (1) 기상 정보(동네예보정보 조회 서비스) / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)  # request 날리는 함수

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('UTF-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Weather_URL(yyyymmdd, day_time):
    access_key = "WjF8b7ubtxqL4v%2BGGDiKHmlzdYuzak5z548vypCpbJXcB3TCRFmBo6VwfregwjGpyAh11Skos%2FIwufWMUB827g%3D%3D"
    x_coodinate = "89"
    y_coodinate = "91"
    # (1)기상 정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"  # ForecastTimeData 서비스를 이용할 것

    parameters = "?_type=json&ServiceKey=" + access_key  # 메뉴얼을 보고 요청 메세지를 완성할 것
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + str(day_time)
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def Make_Weather_Json(day_time):
    json_weather_result = []
    # (1) 기상 정보(동네예보정보 조회서비스) json 파일을 생성하는 함수
    yyyymmdd = time.strftime('%Y%m%d', time.localtime(time.time()))
    jsonData = get_Weather_URL(yyyymmdd, day_time)
    index = 0
    for i in jsonData['response']['body']['items']['item']:
        # jsonData를 parsing 하여 json_weather_result에 저장된 예제 샘플을 참고하여 데이터를 저장한다.
        if (jsonData['response']['header']['resultMsg'] == 'OK'):
            category = jsonData['response']['body']['items']['item'][index]["category"]
            fcstValue = jsonData['response']['body']['items']['item'][index]["fcstValue"]
            if category == 'RN1':
                if fcstValue >0:
                    g_Balcony_windows = False
                    print("닫힘")
                else:
                    g_Balcony_windows = True
                    print("열림")
            if category == 'T1H':
                if fcstValue > 23:
                    g_Balcony_windows = False
                    g_Radiator = True
                    print("난방기 작동,창문 닫힘")
                else:
                    g_Balcony_windows = True
                    g_Radiator = False
                    print("난방기 정지,창문 열림")
            index += 1

def get_Realtime_Weather_Info():  # 시간 정보를 보정하여 Make_Weather_Json() 을 호출한다.
    if int(time.strftime('%M')) < 30:
        an_hour_later = str(int(datetime.datetime.today().hour) - 1)
        Make_Weather_Json(an_hour_later)
    else:
        now_time = time.strftime('%H%M', time.localtime(time.time()))
        Make_Weather_Json(now_time)

while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))
    if(menu_num == 1):
        check_device_status()
    elif(menu_num == 2):
        print("현재 인공지능 모드: ", end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode == True:
            ai_scheduler = threading.Thread(target=update_scheduler)
            ai_scheduler.daemon = True
            ai_scheduler.start()
            print("작동완료")
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("정지 완료")
    elif(menu_num == 3):
        break
