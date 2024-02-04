import tkinter as tk
import threading
import pygame
from game import Main
from Settings import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

def main():
    pygame.init()
    Game = Main(size=SIZE, title=TITLE, icon=ICON)
    Game.init()
    Game.main()


t2 = threading.Thread(target=main)

def window():
    root = tk.Tk()
    # root.overrideredirect(True)
    # root.attributes('-alpha', 0.92)
    root.title('战地风云')
    root.geometry('1028x640+100+50')
    root.resizable(height=False, width=False)
    ico = tk.PhotoImage(file='icon.png')
    root.iconphoto(False, ico)
    choose_frame = tk.Frame(root, bg='#C0FBFF', width=180, height=640)
    choose_frame.grid(row=0, column=0)
    main_frame1 = tk.Frame(root, bg='#FFF9E4', width=848, height=640)
    main_frame2 = tk.Frame(root, bg='#FFF9E4', width=848, height=640)
    main_frame3 = tk.Frame(root, bg='#FFF9E4', width=848, height=640)
    count = 1
    avatar_image = Image.open(f'avatar/army{count}.jpg')
    avatar_tk = ImageTk.PhotoImage(avatar_image)
    title_image = Image.open('Launcher_UI/title.png')
    title_tk = ImageTk.PhotoImage(title_image)
    tk.Label(main_frame1, image=avatar_tk).grid(row=0, column=0, padx=50, pady=20, columnspan=2)
    tk.Label(main_frame1, image=title_tk).grid(row=0, column=2, padx=10, pady=20)
    tk.Label(main_frame1, bg='#FFF9E4', width=5).grid(row=1, column=0)
    input_box = tk.Frame(main_frame1, bg='#FFF9E4', width=700, height=250)
    input_box.grid(row=1, column=1, columnspan=2, pady=20)
    input_box.grid_propagate(False)
    username = tk.StringVar()
    password = tk.StringVar()
    tk.Label(input_box, width=9, height=2, bg='#FFF9E4').grid(row=0, column=0)
    tk.Label(input_box, text='账号:', font=('黑体',35), bg='#FFF9E4').grid(row=1, column=1, padx=10, pady=20)
    tk.Entry(input_box, textvariable=username, width=60, bg='#FFF9E4').grid(row=1, column=2, pady=20)
    tk.Label(input_box, text='密码:', font=('黑体',35), bg='#FFF9E4').grid(row=2, column=1, padx=10, pady=20)
    tk.Entry(input_box, textvariable=password, width=60, bg='#FFF9E4').grid(row=2, column=2, pady=20)
    def start_game():
        global t2
        if username.get() == 'lushen' and password.get() == '123456':
            t2.start()
        else:
            messagebox.showwarning(title='提示', message='用户名或密码错误，请重新输入')
    tk.Button(main_frame1, text='启动', font=('黑体',35), width=28, bd=0, bg='#7CF1FF', command=start_game).grid(row=2, column=0, columnspan=3)
    main_frame1.grid(row=0, column=1)
    img1 = Image.open('Launcher_UI/startUI.png')
    img2 = Image.open('Launcher_UI/SettingsUI.png')
    img3 = Image.open('Launcher_UI/personalize.png')
    ui1 = ImageTk.PhotoImage(img1)
    ui2 = ImageTk.PhotoImage(img2)
    ui3 = ImageTk.PhotoImage(img3)
    def b1():
        main_frame1.grid(row=0, column=1)
        main_frame2.grid_forget()
        main_frame3.grid_forget()
    def b2():
        main_frame2.grid(row=0, column=1)
        main_frame1.grid_forget()
        main_frame3.grid_forget()
    def b3():
        main_frame3.grid(row=0, column=1)
        main_frame2.grid_forget()
        main_frame1.grid_forget()
    bt1 = tk.Button(choose_frame, image=ui1, bd=0, command=b1)
    bt2 = tk.Button(choose_frame, image=ui2, bd=0, command=b2)
    bt3 = tk.Button(choose_frame, image=ui3, bd=0, command=b3)
    x = 49
    y = 31
    bt1.pack(padx=x, pady=y)
    bt2.pack(padx=x, pady=y)
    bt3.pack(padx=x, pady=y)
    main_frame1.grid_propagate(False)
    main_frame2.grid_propagate(False)
    main_frame3.grid_propagate(False)
    root.mainloop()





t1 = threading.Thread(target=window)
t1.start()


