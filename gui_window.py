import tkinter as tk
import tkinter.messagebox

def gui_main():
    #리폿항목 초기화
    report_data = []

    # Tkinter 창
    window = tk.Tk()
    window.title("TFT Autoreport")
    window.geometry("350x600")
    window.resizable(width=False, height=False)

    #빈공간 넣는 함수
    def insert_margin_y(parent, pad_amount):
        empty_label = tk.Label(parent, text="")
        empty_label.pack(pady=pad_amount)

    # 라디오 프레임

    radioframe_title = tk.Label(window, text="리폿할 녀석")
    radioframe_title.pack()

    radioframe = tk.Frame(window, 
                 borderwidth=2, 
                 relief="ridge", 
                 padx=10,
                 pady=10)
    radioframe.pack()



    #라디오 버튼 생성


    radio_var = tk.StringVar()
    radio_var.set("1등")
    options = ["1등", "2등", "3등", "4등", "5등", "6등", "7등", "8등"]
    opt_index = 0

    for option in options:
        radio_btn = tk.Radiobutton(radioframe, text=option, variable=radio_var, value=option)
        radio_btn.grid(row=0 if opt_index < 4 else 1,
                        column=opt_index if opt_index < 4 else opt_index - 4,
                        padx=5, pady=5, sticky="w")
        opt_index += 1

    insert_margin_y(window, 5)
    
    #체크박스 프레임
    checkboxframe_title = tk.Label(window, text="리폿할 항목")
    checkboxframe_title.pack()

    checkboxframe = tk.Frame(window, 
                 borderwidth=2, 
                 relief="ridge", 
                 padx=10,
                 pady=10)
    checkboxframe.pack()
    

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

    checkbox_1 = tk.Checkbutton(checkboxframe, text="욕설", variable=var_check_1, command=on_checkbox_click)
    checkbox_1.pack(pady=5)
    checkbox_2 = tk.Checkbutton(checkboxframe, text="혐오 발언", variable=var_check_2, command=on_checkbox_click)
    checkbox_2.pack(pady=5)
    checkbox_3 = tk.Checkbutton(checkboxframe, text="부정행위(핵 사용)", variable=var_check_3, command=on_checkbox_click)
    checkbox_3.pack(pady=5)
    checkbox_4 = tk.Checkbutton(checkboxframe, text="불쾌감을 주거나 부적절한 이름 사용", variable=var_check_4, command=on_checkbox_click)
    checkbox_4.pack(pady=5)

    # 체크박스 상태 확인 라벨 

    label = tk.Label(checkboxframe, textvariable=label_var)
    label.config(fg="red")
    label.pack()

    insert_margin_y(window, 5)

    # 텍스트 상자

    textarea_label = tk.Label(window, text="리폿 내용(최대 250자)")
    textarea_label.pack()

    textarea = tk.Text(window, height=8, width=40)
    textarea.pack()

    #버튼

    def button_onclick():
        #체크박스 체크된지 확인
        if var_check_1.get() or var_check_2.get() or var_check_3.get() or var_check_4.get():
            #리폿내용 가져오기
            var_textarea = textarea.get("1.0", "end-1c")[:250]

            report_data.append(var_check_1.get())
            report_data.append(var_check_2.get())
            report_data.append(var_check_3.get())
            report_data.append(var_check_4.get())
            report_data.append(var_textarea)

            report_data.append(radio_var.get())

        #창 닫기
            window.destroy()
        else:
            tkinter.messagebox.showerror("오류", "리폿 항목을 체크해주세요")

    button = tk.Button(window, text="자동 리폿 시작", command=button_onclick, width=25, height=4, bd=3)
    button.pack(pady=10)

    # 프로그램 실행
    window.mainloop()
    
    # 프로그램 종료
    if report_data != []:
        return report_data