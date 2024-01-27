#외부 라이브러리
import pyautogui as gui
import time
import pyperclip
import random

#모듈
from checkwindow import check_window
import gui_window

#상수
GAME_TITLE = "League of Legends"
CLIENT_RES = (1600,900)
CHECKBOX_IMAGE_PATH = "./image/checkbox.png" # 참고 : 24x24 이미지임
FIRST_EXC_COORD = (240, 200) # 참고: 플레이어 간격이 75px
FIRST_CHECKBOX_COORD = (545, 365) #참고 : 체크박스 세로간격이 55px, 이것만 왼쪽 위 기준임
REP_TEXTBOX_COORD = (700, 600) 
REP_BTN_COORD = (800, 666) 

####################################################

# 1. 창 감지, 해상도 체크 후 열려있으면 gui window 오픈 
rep_data = []
gui_done = False

if check_window(GAME_TITLE,CLIENT_RES):
  rep_data = gui_window.gui_main()
  print(rep_data)
  gui_done = True
else:
  gui.alert(title="실행 불가",text="1. 클라이언트가 실행 중이 아니거나 \n2. 최소화되었거나 \n3. 해상도가 1600*900 이 아닙니다")
  exit()

# 2. gui window에서 가져온 값으로 리폿하는 함수
  
def report_process_2():
  #리폿버튼(느낌표) 클릭
  gui.moveTo(x=FIRST_EXC_COORD[0], y=FIRST_EXC_COORD[1] + ((int(rep_data[5][0]) - 1) * 75)) 
  time.sleep(0.5)
  gui.click()

  #이미지서칭
  try:
    checkbox_images = list(gui.locateAllOnScreen(CHECKBOX_IMAGE_PATH))
  except:
    print('이미지 인식 실패')
    checkbox_images = None

  if checkbox_images is not None:

    first_checkbox_top = checkbox_images[0].top
    first_checkbox_left = checkbox_images[0].left

    print(f"체크박스 {len(checkbox_images)}개 발견됨")
    print("첫번째 체크박스 좌표 : ",first_checkbox_top, first_checkbox_left)

  else:
    print("체크박스 이미지를 인식할 수 없습니다. 고정 좌표로 진행합니다")

  # 체크박스 클릭
    
  for i in range(4):
    if rep_data[i]:
      gui.click(x=first_checkbox_left + 12 if checkbox_images != None else FIRST_CHECKBOX_COORD[0] + 12,
               y=first_checkbox_top + (i*55) + 12 if checkbox_images != None else FIRST_CHECKBOX_COORD[1] + 12 + (i * 55), 
               duration=0.15)
  time.sleep(0.1)
  
  # 리폿 내용 입력(복붙) - 조건부. 리폿내용 없으면 여기는 스킵.
  if not rep_data[4] == "":
    time.sleep(0.1)
    gui.click(x=REP_TEXTBOX_COORD[0], y= REP_TEXTBOX_COORD[1])
    time.sleep(0.3)
    pyperclip.copy(rep_data[4])
    gui.hotkey("ctrl", "v")
    time.sleep(0.3)
  
  # 리폿 버튼 클릭
  gui.click(x = REP_BTN_COORD[0], y= REP_BTN_COORD[1])
  time.sleep(0.1 + (random.random() / 2))

# 3-1. gui 정상종료시 리폿 프로세스 시작(함수 실행)
  
if gui_done and rep_data != None:
  gui.getWindowsWithTitle(GAME_TITLE)[0].activate()

  loop_count = 0

  try:
    loop_count = int(gui.prompt(title="반복 횟수", text="몇 번 반복해서 리폿할까요? 숫자만 입력해주세요."))
  except Exception as e:
    gui.alert(title="오류", text=f"오류가 발생하거나 실행을 취소하여 프로그램을 종료합니다. \n 오류내용:{e}")
    exit()

  all_ok = gui.confirm(title="마지막으로 확인", 
                       text=f"{rep_data[5]} 플레이어를 {loop_count}번 리폿합니다. {'진짜!진짜!정말로!!' if loop_count >= 5 else ''} 확실한가요?")

  if all_ok == "OK" :
    gui.alert(title="시작",
               text=f"리폿을 시작합니다.\n이미지 인식 실패 시에 고정 좌표로 진행됩니다.\n클라이언트 창을 화면 맨 왼쪽 위로 옮겨주세요.\n일시중지는 Ctrl+Alt+Delete 를 눌러주세요.")
    for i in range(loop_count):
      report_process_2()

    gui.alert(title="완료", text="리폿이 완료되었습니다. 프로그램을 종료합니다.")
    exit()
  else:
    gui.alert(title="취소됨", text="다시 실행해주세요.")
    exit()

# 3-2. 닫기로 gui 닫았을 때 프로그램 전체 종료
if gui_done and rep_data == None:
  gui.alert(title="종료", text="프로그램을 종료합니다.")
  exit() 
