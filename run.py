import pyautogui as gui

# 1. Leagueclient.exe 켜져있는지 감지하고 GUI window 실행, if not - alert
is_running = False
rep_data = []
from checkwindow import check_window
if check_window("League of Legends", (1600,900)):
  import gui_window
else:
  gui.alert(title="실행 불가",text="1. 클라이언트가 실행 중이 아니거나 \n2. 최소화되었거나 \n3. 해상도가 1600*900 이 아님")
  exit()
# 3. GUI에서 체크한 n1, n2, n3번째 체크박스에 체크

# 4. 문구입력창 감지 후 GUI에서 입력해둔 문구 입력
# 5. 리폿버튼 감지 후 클릭
# 6. 기다리기...(client lag)
# 7. if [체크박스 감지됨] 이라면 2~6번 반복, if not - loop 종료 후 alert 출력