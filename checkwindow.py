import pygetwindow as gw

def check_window(title, resol):
    try:
        window = gw.getWindowsWithTitle(title)[0] # 타이틀로 실행여부 확인
        current_resol = (window.width, window.height) # 해상도 확인
        return current_resol == resol
    except IndexError:
        return False