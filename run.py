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

# 1. 창 감지, 해상도 체크 후 열려있으면 gui window 오픈 
rep_data = []
gui_done = False

if check_window(GAME_TITLE,CLIENT_RES):
  rep_data = gui_window.gui_main()
  print(rep_data)
  gui_done = True
else:
  gui.alert(title="실행 불가",text="1. 클라이언트가 실행 중이 아니거나 \n2. 최소화되었거나 \n3. 해상도가 1600*900 이 아님")
  exit()

# 2. gui window에서 가져온 값으로 리폿하는 함수

def report_process():
  try:
    time.sleep(0.1)
    
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
    time.sleep(0.1)

  except Exception as e:
    gui.alert(title="오류", text=f"이미지 인식 오류거나, 다른 오류가 발생한듯? \n오류내용: <{e}>")
    raise Exception("리폿 과정에서 오류가 발생하였습니다.")

# 함수 실행
  
if gui_done and False:
  gui.getWindowsWithTitle(GAME_TITLE)[0].activate()
  loop_count = gui.prompt('몇 번 반복해서 리폿할까요?')
  all_ok = gui.confirm(title="마지막으로 확인", text=f"{rep_data[5]}번 플레이어를 {loop_count}번 리폿합니다. 확실한가요?")

  if all_ok == "OK" :
    for i in range(loop_count):
      report_process()
  else:
    gui.alert(title="취소됨", text="다시 실행해주세요.")
    exit()

# todos
#1. 전체 로직 변경 (단순반복으로)
#2. 이미지 서칭 실패하면 고정 좌표로 클릭(confirm 띄우고)
#3. gui 종료버튼으로 눌렀을때는 전체 종료하기
#4. 중간에 키보드로 escape하는 방법 만들기