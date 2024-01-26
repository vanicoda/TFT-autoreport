import pygetwindow as gw

def check_window(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        return True
    except IndexError:
        return False
