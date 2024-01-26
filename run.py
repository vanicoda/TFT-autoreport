#외부 라이브러리
import pyautogui as gui
import time
import pyperclip

#모듈
from checkwindow import check_window
import gui_window

#상수
GAME_TITLE = "League of Legends"
CLIENT_RES = (1600,900)
CHECKBOX_IMAGE_PATH = "./image/checkbox.png" # 참고 : 24x24 이미지임
REPORT_IMAGE_PATH = "./image/repbtn.png" # 참고 : 148x30 이미지

####################################################

# 1. Leagueclient.exe 켜져있는지 감지하고 GUI window 실행, if not - alert
rep_data = []
gui_done = False

if check_window(GAME_TITLE,CLIENT_RES):
  rep_data = gui_window.gui_main()
  print(rep_data)
  gui_done = True
else:
  gui.alert(title="실행 불가",text="1. 클라이언트가 실행 중이 아니거나 \n2. 최소화되었거나 \n3. 해상도가 1600*900 이 아님")
  exit()

# 2. GUI에서 체크한 n1, n2, n3번째 체크박스에 체크

def report_process():
  try:
    gui.alert(title="TFT Autoreport", text="자동 리폿을 시작합니다.")
    time.sleep(0.1)
    gui.getWindowsWithTitle(GAME_TITLE)[0].activate()
    time.sleep(0.3)  

    #이미지서칭
    checkbox_images = list(gui.locateAllOnScreen(CHECKBOX_IMAGE_PATH))

    first_checkbox_top = checkbox_images[0].top
    first_checkbox_left = checkbox_images[0].left
    
    print(first_checkbox_top, first_checkbox_left)
    
    checkboxes_top = []
    for i in range(4):
      checkboxes_top.append(first_checkbox_top + (i*55)) #참고 : 체크박스 세로간격이 55px임

    print(checkboxes_top)

    # 체크박스 클릭
    for i in range(4):
      if rep_data[i]:
        gui.click(x=first_checkbox_left + 12, y=checkboxes_top[i] + 12, duration=0.15)

    # 리폿 내용 입력(복붙)
    time.sleep(0.5)
    gui.click(x=first_checkbox_left + 24, y=checkboxes_top[3] + 50) #대충 이쯤에 리폿내용 적는 상자
    time.sleep(0.5)
    pyperclip.copy(rep_data[4])
    gui.hotkey("ctrl", "v")
    time.sleep(0.5)

    # 리폿 버튼 클릭
    repbtn = gui.locateOnScreen(REPORT_IMAGE_PATH)
    gui.click(x=repbtn.left + 74, y=repbtn.top + 15)
    

  except Exception as e:
    gui.alert(title="오류", text=f"이미지 인식 오류거나, 다른 오류가 발생한듯? \n오류내용: <{e}>")

if gui_done:
  report_process()


# 3. 문구입력창 감지 후 GUI에서 입력해둔 문구 입력
# 4. 리폿버튼 감지 후 클릭
# 5. 기다리기...(client lag)
# 6. if [체크박스 감지됨] 이라면 2~6번 반복, if not - loop 종료 후 alert 출력