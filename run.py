#외부 라이브러리
import pyautogui as gui
import time

#모듈
from checkwindow import check_window
import gui_window

#상수
GAME_TITLE = "League of Legends"
CLIENT_RES = (1600,900)

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
if gui_done:
  gui.alert(title="TFT Autoreport", text="자동 리폿을 시작합니다.")
  time.sleep(0.5)
  gui.getWindowsWithTitle(GAME_TITLE)[0].activate()
  
  checkbox_images = list(gui.locateAllOnScreen("./image/checkbox.png"))
  print(checkbox_images[0])
  # gui.click(checkbox_image, duration=0.1)

# 3. 문구입력창 감지 후 GUI에서 입력해둔 문구 입력
# 4. 리폿버튼 감지 후 클릭
# 5. 기다리기...(client lag)
# 6. if [체크박스 감지됨] 이라면 2~6번 반복, if not - loop 종료 후 alert 출력