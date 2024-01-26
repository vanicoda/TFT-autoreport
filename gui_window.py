import tkinter as tk

# Tkinter 창
window = tk.Tk()
window.title("TFT Autoreport")
window.geometry("350x450")

# 체크박스 변수 및 라벨 변수
var_check_1 = tk.BooleanVar()
var_check_2 = tk.BooleanVar()
var_check_3 = tk.BooleanVar()
var_check_4 = tk.BooleanVar()
label_var = tk.StringVar(value="리폿할 항목을 선택해주세요")

# 체크박스
def on_checkbox_click():
    label_text = ""
    if var_check_1.get():
        label_text += "욕설 "
    if var_check_2.get():
        label_text += "혐오발언 "
    if var_check_3.get():
        label_text += "부정행위 "
    if var_check_4.get():
        label_text += "부적절이름"

    label_var.set(label_text)

checkbox_1 = tk.Checkbutton(window, text="욕설", variable=var_check_1, command=on_checkbox_click)
checkbox_1.pack(pady=5)
checkbox_2 = tk.Checkbutton(window, text="혐오 발언", variable=var_check_2, command=on_checkbox_click)
checkbox_2.pack(pady=5)
checkbox_3 = tk.Checkbutton(window, text="부정행위(핵 사용)", variable=var_check_3, command=on_checkbox_click)
checkbox_3.pack(pady=5)
checkbox_4 = tk.Checkbutton(window, text="불쾌감을 주거나 부적절한 이름 사용", variable=var_check_4, command=on_checkbox_click)
checkbox_4.pack(pady=5)

# 체크박스 상태 확인 라벨 

label = tk.Label(window, textvariable=label_var)
label.config(fg="red")
label.pack()


# 텍스트 상자

textarea_label = tk.Label(window, text="리폿 내용(최대 250자)")
textarea_label.pack(pady=30)

textarea = tk.Text(window, height=8, width=40)
textarea.pack()

#버튼
# !!! 체크박스 체크된지 확인(if not - alert), 입력한 문구 변수에 저장 후 textbox disable 시키기 !!!

def button_onclick():
    #리폿항목 가져오기
    print(var_check_1.get())
    print(var_check_2.get())
    print(var_check_3.get())
    print(var_check_4.get())
    #리폿내용 가져오기
    var_textarea = textarea.get("1.0", "end-1c")[:250]
    print(var_textarea)
    #창 닫기
    window.destroy()

button = tk.Button(window, text="자동 리폿 시작", command=button_onclick)
button.pack(pady=10)

# 프로그램 실행
window.mainloop()