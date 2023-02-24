from tkinter import *
from qsnctf import *
import webbrowser

root = Tk()

root.title("社会主义核心价值观编码 V1.0.0 By：青少年CTF")
root.iconbitmap('logo.ico')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 450
height = 315
# round去掉小数
window_size = f'{width}x{height}+{round((screen_width-width)/2)}+{round((screen_height-height)/2)}'
root.geometry(window_size)
root.resizable(False, False)


def exit_file():
    exit()


def aboutme():
    webbrowser.open('https://www.qsnctf.com/about')


def qqqun():
    webbrowser.open('https://jq.qq.com/?_wv=1027&k=xlBrvpTB')


def qsnctf():
    webbrowser.open('https://www.qsnctf.com/')


# Menu
root['bg'] = "#f0f0f0"
m = Menu(root, background='#f0f0f0', relief='groove', tearoff=False)
filemenu = Menu(m, relief='groove', tearoff=False)
filemenu.add_command(label='退出', command=exit_file)
m.add_cascade(label='程序', menu=filemenu)
about = Menu(m, relief='groove', tearoff=False)
about.add_command(label='关于我们', command=aboutme)
about.add_command(label='QQ群', command=qqqun)
about.add_command(label='青少年CTF', command=qsnctf)
m.add_cascade(label='关于', menu=about)


frame0 = Frame(root)
# 解码
L1 = Label(frame0, text="需要解码的内容：")
E1 = Entry(frame0, bd=1, width=48)


# 编码
L2 = Label(frame0, text="需要编码的内容：")
E2 = Entry(frame0, bd=1, width=48)


def encode():
    code = E2.get()
    text = Chinese_socialism_encode(code)
    insert_text("编码结果：" + text)


def decode():
    code = E1.get()
    text = Chinese_socialism_decode(code)
    insert_text("解码结果：" + text)


frame1 = Frame(root)

B1 = Button(frame1, text="解码", command=decode)
B2 = Button(frame1, text="编码", command=encode)


frame2 = Frame(root)

t1 = Text(frame2, width=62, height=16)


L1.grid(row=1, column=1)
L2.grid(row=2, column=1)
E1.grid(row=1, column=2)
E2.grid(row=2, column=2)

frame0.grid(row=1, column=1)
frame1.grid(row=3, column=1, sticky=E)
frame2.grid(row=4, column=1, sticky=E)


t1.grid(row=1, column=1)

B1.grid(row=1, column=1)
B2.grid(row=1, column=2)


def insert_text(text):
    t1.insert(END, text+"\n")


root['menu'] = m
root.mainloop()
