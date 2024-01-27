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
  #리폿버튼 클릭
  gui.moveTo(x=400, y=265 + ((int(rep_data[5][0]) - 1) * 75)) # 참고: 플레이어 간격이 75px, 1등 리폿버튼 위치 : left 400 top 265
  time.sleep(0.5)
  gui.click()

  #이미지서칭
  checkbox_images = list(gui.locateAllOnScreen(CHECKBOX_IMAGE_PATH))

  print(f"체크박스 {len(checkbox_images)}개 발견됨")

  if checkbox_images != None:

    first_checkbox_top = checkbox_images[0].top
    first_checkbox_left = checkbox_images[0].left

    print(first_checkbox_top, first_checkbox_left)

  else:
    print("체크박스 이미지를 인식할 수 없습니다. 고정 좌표로 진행합니다")

  # 체크박스 클릭
    
  for i in range(4):
    if rep_data[i]:
      gui.click(x=first_checkbox_left + 12 if checkbox_images != None else 557,
               y=first_checkbox_top + (i*55) + 12 if checkbox_images != None else 377 + (i * 55), 
               duration=0.15) #참고 : 체크박스 세로간격이 55px, 첫번째 체크박스 top 545, left 365
  
  # 리폿 내용 입력(복붙) - 조건부. 리폿내용 없으면 실행안되게.
  if not rep_data[4] == "":
    time.sleep(0.1)
    gui.click(x=first_checkbox_left + 24, y= first_checkbox_top +215) #대충 이쯤에 리폿내용 적는 상자
    time.sleep(0.3)
    pyperclip.copy(rep_data[4])
    gui.hotkey("ctrl", "v")
    time.sleep(0.3)
  
  # 리폿 버튼 클릭
  gui.click(x = 960, y= 735)
  time.sleep(0.1 + (random.random() / 2)) # 0.1~0.6초 대기


def report_process():
  try:    
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

    # 리폿 내용 입력(복붙) - 이거 조건부로 고치기. 리폿내용 없으면 실행안되게.
    time.sleep(0.5)
    gui.click(x=first_checkbox_left + 24, y=checkboxes_top[3] + 50) #대충 이쯤에 리폿내용 적는 상자
    time.sleep(0.5)
    pyperclip.copy(rep_data[4])
    gui.hotkey("ctrl", "v")
    time.sleep(0.5)

    # 리폿 버튼 클릭
    repbtn = gui.locateOnScreen(CHECKBOX_IMAGE_PATH)
    gui.click(x=repbtn.left + 74, y=repbtn.top + 15)
    time.sleep(0.1)

  except Exception as e:
    gui.alert(title="오류", text=f"이미지 인식 오류거나, 다른 오류가 발생한듯? \n오류내용: <{e}>")
    raise Exception("리폿 과정에서 오류가 발생하였습니다.")

# 함수 실행
  
if gui_done and rep_data != None:
  gui.getWindowsWithTitle(GAME_TITLE)[0].activate()

  loop_count = 0

  try:
    loop_count = int(gui.prompt('몇 번 반복해서 리폿할까요? 숫자만 입력해주세요.'))
  except Exception as e:
    gui.alert(title="오류", text=f"제대로 된 숫자를 입력해주세요.\n오류가 발생하여 프로그램을 종료합니다. \n 오류내용:{e}")
    exit()

  all_ok = gui.confirm(title="마지막으로 확인", text=f"{rep_data[5]} 플레이어를 {loop_count}번 리폿합니다. 확실한가요?")

  if all_ok == "OK" :
    gui.alert(title="시작", text="리폿을 시작합니다.")
    for i in range(loop_count):
      report_process_2()
    
    gui.alert(title="완료", text="리폿이 완료되었습니다.")
    exit()
  else:
    gui.alert(title="취소됨", text="다시 실행해주세요.")
    exit()

#닫기로 gui 닫았을 때 프로그램 전체 종료
if gui_done and rep_data == None:
  gui.alert(title="종료", text="프로그램을 종료합니다.")
  exit()


  

# todos
# escape하는 방법 만들기. 안되면 최대 횟수 제한
# 유저 테스트
# 2번함수 잘 동작되면 원래꺼 삭제
# 다 하고 주석/코드 정리