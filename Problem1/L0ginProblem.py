#로그인을 하기위해 ID / PW를 얻어라!
#이정도는 코드만 읽기만 하면 되겠죠?(답이 훤이 보인다~~)
code = b'\nimport tkinter as tk\nfrom tkinter import messagebox as msgbox\n\nform = tk.Tk()\nform.title("\xeb\xa1\x9c\xea\xb7\xb8\xec\x9d\xb8")\nform.geometry("195x150")\nform.resizable(False, False)\n\narr = {\n    \'id\': \'admin\',\n    \'pw\': \'admin123\'\n}\n\nflag = \'6e6214e19140a7933f4b648953a3f1e0e2486fdcd66e49d993ff6052ede339b8\'\n\ndef Login_Check():\n    if arr[\'id\'] == ID_Entry.get() and arr[\'pw\'] == PW_Entry.get():\n        msgbox.showinfo("flag", flag)\n    else:\n        msgbox.showwarning("\xec\x95\x88\xeb\x82\xb4", "\xed\x8c\xa8\xec\x8a\xa4\xec\x9b\x8c\xeb\x93\x9c\xea\xb0\x80 \xed\x8b\x80\xeb\xa6\xbd\xeb\x8b\x88\xeb\x8b\xa4.", icon = \'error\')\n\n\nID_Label = tk.Label(form, text=\'\xec\x95\x84\xec\x9d\xb4\xeb\x94\x94\')\nID_Label.grid(row=0, column=0)\n\nID_Entry = tk.Entry(form)\nID_Entry.grid(row=0, column=1)\n\nPW_Label = tk.Label(form, text=\'\xec\x95\x94\xed\x98\xb8\')\nPW_Label.grid(row=1, column=0)\n\nPW_Entry = tk.Entry(form)\nPW_Entry.grid(row=1, column=1)\n\nCheck_Button = tk.Button(form, text="\xed\x99\x95\xec\x9d\xb8", width=20, command=Login_Check)\nCheck_Button.grid(row=2, column=1)\n\nform.mainloop()'

exec(code.decode())
