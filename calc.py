from tkinter import *
import tkinter as tk
import threading
import time
import os
import sys

window = Tk()
window.title("仙术杯计算器(by椰蓉猫)")
window.geometry("1000x700")
window.resizable(width = False, height = False)



score_1 = 0 ##临时招募
score_2 = 0 ##结局
score_31 = 0 ##紧急
score_32 = 0 ##隐藏
score_4 = 0 ##藏品
score_5 = 0 ##隐藏怪
score_6 = 0 ##启示
score_7 = 0 ##上场积分
score_8 = 0 ##结算分数
score_0 = "" ##总分

text_v_result = tk.StringVar()
text_v_result.set(score_0)
text_v_result_1 = tk.IntVar()
text_v_result_1.set(score_1)
text_v_result_2 = tk.IntVar()
text_v_result_2.set(score_2)
text_v_result_31 = tk.IntVar()
text_v_result_31.set(score_31)
text_v_result_32 = tk.IntVar()
text_v_result_32.set(score_32)
text_v_result_4 = tk.IntVar()
text_v_result_4.set(score_4)
text_v_result_5 = tk.IntVar()
text_v_result_5.set(score_5)
text_v_result_6 = tk.IntVar()
text_v_result_6.set(score_6)
text_v_result_7 = tk.IntVar()
text_v_result_7.set(score_7)
text_v_result_8 = tk.IntVar()
text_v_result_8.set(score_7)
text_v_result_0 = tk.IntVar()
text_v_result_0.set(score_0)




##01
def com_setresult_1():
    global score_1_1,score_1_2,score_1_3,score_1
    score_1 = int(score_1_1) + int(score_1_2) + int(score_1_3)
    text_v_result_1.set(score_1)

title_1 = tk.Label(window,text='临时招募',font=('arial',15)).place(x=5,y=5)
result_1 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_1,state='readonly',relief='sunken').place(x=90,y=8)

score_1_1 = 0
def com_result_1_1(v):
    global score_1_1
    score_1_1 = int(v)*50
    com_setresult_1()

title_1_1 = tk.Label(window,text='6星(50)',font=('arial',11)).place(x=15,y=35)
scale_1_1 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_1_1).place(x=70,y=37)

score_1_2 = 0
def com_result_1_2(v):
    global score_1_2
    score_1_2 = int(v)*20
    com_setresult_1()

title_1_2 = tk.Label(window,text='5星(20)',font=('arial',11)).place(x=15,y=85)
scale_1_2 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_1_2).place(x=70,y=87)

score_1_3 = 0
def com_result_1_3(v):
    global score_1_3
    score_1_3 = int(v)*10
    com_setresult_1()

title_1_3 = tk.Label(window,text='4星(10)',font=('arial',11)).place(x=15,y=135)
scale_1_3 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_1_3).place(x=70,y=137)



##02
def com_setresult_2():
    global score_2
    while 1:
        score_2 = checkvar_2_1.get()*450+checkvar_2_2.get()*300+checkvar_2_3.get()*120+checkvar_2_4.get()*150+checkvar_2_5.get()*230
        text_v_result_2.set(score_2)
        time.sleep(0.1)

title_2 = tk.Label(window,text='结局',font=('arial',15)).place(x=5,y=185)
result_2 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_2,state='readonly',relief='sunken').place(x=55,y=188)

checkvar_2_1 = IntVar()
checkvar_2_2 = IntVar()
checkvar_2_3 = IntVar()
checkvar_2_4 = IntVar()
checkvar_2_5 = IntVar()

checkbut_2_1 = Checkbutton(window,text='骑士(450)',font=('arial',14),variable=checkvar_2_1,onvalue=1,offvalue=0).place(x=15,y=220)
checkbut_2_2 = Checkbutton(window,text='水月(300)',font=('arial',14),variable=checkvar_2_2,onvalue=1,offvalue=0).place(x=15,y=255)
checkbut_2_3 = Checkbutton(window,text='锈锤(120)',font=('arial',14),variable=checkvar_2_3,onvalue=1,offvalue=0).place(x=15,y=290)
checkbut_2_4 = Checkbutton(window,text='寒灾(150)',font=('arial',14),variable=checkvar_2_4,onvalue=1,offvalue=0).place(x=15,y=325)
checkbut_2_5 = Checkbutton(window,text='墓碑(230)',font=('arial',14),variable=checkvar_2_5,onvalue=1,offvalue=0).place(x=15,y=360)

thread_2 = threading.Thread(target=com_setresult_2)
thread_2.start()



#031
def com_setresult_3():
    global score_3_1,score_3_2,score_3_3,score_3_4,score_3_5,score_3_6,score_3_7,score_3_8,score_3_9,score_3_10,score_3_11,score_3_12,score_3_13,score_31
    score_31 = int(score_3_1) + int(score_3_2) + int(score_3_3) + int(score_3_4) + int(score_3_5) + int(score_3_6) + int(score_3_7) + int(score_3_8) + int(score_3_9) + int(score_3_10) + int(score_3_11) + int(score_3_12) + int(score_3_13)
    text_v_result_31.set(score_31)

title_3 = tk.Label(window,text='紧急',font=('arial',15)).place(x=300,y=5)
result_3 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_31,state='readonly',relief='sunken').place(x=350,y=8)

score_3_1 = 0
def com_result_3_1(v):
    global score_3_1
    score_3_1 = int(v)*40
    com_setresult_3()

title_3_1 = tk.Label(window,text='巢穴(40)',font=('arial',11)).place(x=310,y=35)
scale_3_1 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_1).place(x=440,y=37)

score_3_2 = 0
def com_result_3_2(v):
    global score_3_2
    score_3_2 = int(v)*40
    com_setresult_3()

title_3_2 = tk.Label(window,text='瞻前顾后(40)',font=('arial',11)).place(x=310,y=75)
scale_3_2 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_2).place(x=440,y=77)

score_3_3 = 0
def com_result_3_3(v):
    global score_3_3
    score_3_3 = int(v)*100
    com_setresult_3()

title_3_3 = tk.Label(window,text='领地意识(100)',font=('arial',11)).place(x=310,y=115)
scale_3_3 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_3).place(x=440,y=117)

score_3_4 = 0
def com_result_3_4(v):
    global score_3_4
    score_3_4 = int(v)*60
    com_setresult_3()

title_3_4 = tk.Label(window,text='狩猎场(60)',font=('arial',11)).place(x=310,y=155)
scale_3_4 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_4).place(x=440,y=157)

score_3_5 = 0
def com_result_3_5(v):
    global score_3_5
    score_3_5 = int(v)*40
    com_setresult_3()

title_3_5 = tk.Label(window,text='铳与秩序(40)',font=('arial',11)).place(x=310,y=195)
scale_3_5 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_5).place(x=440,y=197)

score_3_6 = 0
def com_result_3_6(v):
    global score_3_6
    score_3_6 = int(v)*50
    com_setresult_3()

title_3_6 = tk.Label(window,text='无漏溟痕乐园(50)',font=('arial',11)).place(x=310,y=235)
scale_3_6 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_6).place(x=440,y=237)

score_3_7 = 0
def com_result_3_7(v):
    global score_3_7
    score_3_7 = int(v)*120
    com_setresult_3()

title_3_7 = tk.Label(window,text='失控(120)',font=('arial',11)).place(x=310,y=275)
scale_3_7 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_7).place(x=440,y=277)

score_3_8 = 0
def com_result_3_8(v):
    global score_3_8
    score_3_8 = int(v)*90
    com_setresult_3()

title_3_8 = tk.Label(window,text='育生池(90)',font=('arial',11)).place(x=310,y=315)
scale_3_8 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_8).place(x=440,y=317)

score_3_9 = 0
def com_result_3_9(v):
    global score_3_9
    score_3_9 = int(v)*90
    com_setresult_3()

title_3_9 = tk.Label(window,text='好梦在何方(90)',font=('arial',11)).place(x=310,y=355)
scale_3_9 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_9).place(x=440,y=357)

score_3_10 = 0
def com_result_3_10(v):
    global score_3_10
    score_3_10 = int(v)*90
    com_setresult_3()

title_3_10 = tk.Label(window,text='余烬方阵(90)',font=('arial',11)).place(x=310,y=395)
scale_3_10 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_10).place(x=440,y=397)

score_3_11 = 0
def com_result_3_11(v):
    global score_3_11
    score_3_11 = int(v)*50
    com_setresult_3()

title_3_11 = tk.Label(window,text='机械之灾(50)',font=('arial',11)).place(x=310,y=435)
scale_3_11 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_11).place(x=440,y=437)

score_3_12 = 0
def com_result_3_12(v):
    global score_3_12
    score_3_12 = int(v)*150
    com_setresult_3()

title_3_12 = tk.Label(window,text='水火相容(150)',font=('arial',11)).place(x=310,y=475)
scale_3_12 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_12).place(x=440,y=477)

score_3_13 = 0
def com_result_3_13(v):
    global score_3_13
    score_3_13 = int(v)*80
    com_setresult_3()

title_3_13 = tk.Label(window,text='深度认知(80)',font=('arial',11)).place(x=310,y=515)
scale_3_13 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_13).place(x=440,y=517)



#032
def com_setresult_32():
    global score_32
    while 1:
        score_32 = checkvar_32_1.get()*30+checkvar_32_2.get()*50+checkvar_32_3.get()*100+checkvar_32_4.get()*50+checkvar_32_5.get()*100+checkvar_32_6.get()*80+checkvar_32_7.get()*50
        text_v_result_32.set(score_32)
        time.sleep(0.1)

title_32 = tk.Label(window,text='隐藏',font=('arial',15)).place(x=600,y=5)
result_32 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_32,state='readonly',relief='sunken').place(x=650,y=8)

checkvar_32_1 = IntVar()
checkvar_32_2 = IntVar()
checkvar_32_3 = IntVar()
checkvar_32_4 = IntVar()
checkvar_32_5 = IntVar()
checkvar_32_6 = IntVar()
checkvar_32_7 = IntVar()

checkbut_32_1 = Checkbutton(window,text='监工现场击杀鸭子(30)',font=('arial',14),variable=checkvar_32_1,onvalue=1,offvalue=0).place(x=610,y=40)
checkbut_32_2 = Checkbutton(window,text='真相通关(50)',font=('arial',14),variable=checkvar_32_2,onvalue=1,offvalue=0).place(x=610,y=75)
checkbut_32_3 = Checkbutton(window,text='真相无漏(100)',font=('arial',14),variable=checkvar_32_3,onvalue=1,offvalue=0).place(x=610,y=110)
checkbut_32_4 = Checkbutton(window,text='跳舞通关(50)',font=('arial',14),variable=checkvar_32_4,onvalue=1,offvalue=0).place(x=610,y=145)
checkbut_32_5 = Checkbutton(window,text='跳舞无漏全收(100)',font=('arial',14),variable=checkvar_32_5,onvalue=1,offvalue=0).place(x=610,y=180)
checkbut_32_6 = Checkbutton(window,text='鸭本运作通关(80)',font=('arial',14),variable=checkvar_32_6,onvalue=1,offvalue=0).place(x=610,y=215)
checkbut_32_7 = Checkbutton(window,text='狂信如火无漏(50)',font=('arial',14),variable=checkvar_32_7,onvalue=1,offvalue=0).place(x=610,y=250)

thread_32 = threading.Thread(target=com_setresult_32)
thread_32.start()



#04
def com_setresult_4():
    global score_4
    while 1:
        if entry_4.get() == '':
            score_4 = 0
        else:
            score_4 = int(entry_4.get())*10
        text_v_result_4.set(score_4)
        time.sleep(0.1)

title_4 = tk.Label(window,text='藏品',font=('arial',15)).place(x=5,y=400)
result_4 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_4,state='readonly',relief='sunken').place(x=55,y=403)

entry_4 = Entry(window, show = None,font = ('Arial',15))
entry_4.place(x=15,y=430)

thread_4 = threading.Thread(target=com_setresult_4)
thread_4.start()



#05
def com_setresult_5():
    global score_5
    while 1:
        if entry_5.get() == '':
            score_5 = 0
        else:
            score_5 = int(entry_5.get())*20
        text_v_result_5.set(score_5)
        time.sleep(0.1)

title_5 = tk.Label(window,text='隐藏怪',font=('arial',15)).place(x=5,y=460)
result_5 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_5,state='readonly',relief='sunken').place(x=75,y=463)

entry_5 = Entry(window, show = None,font = ('Arial',15))
entry_5.place(x=15,y=490)

thread_5 = threading.Thread(target=com_setresult_5)
thread_5.start()



#06
def com_setresult_6():
    global score_6
    while 1:
        if entry_6.get() == '':
            score_6 = 0
        else:
            score_6 = int(entry_6.get())*50
        text_v_result_6.set(score_6)
        time.sleep(0.1)

title_6 = tk.Label(window,text='启示',font=('arial',15)).place(x=600,y=300)
result_6 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_6,state='readonly',relief='sunken').place(x=655,y=303)

entry_6 = Entry(window, show = None,font = ('Arial',15))
entry_6.place(x=615,y=330)

thread_6 = threading.Thread(target=com_setresult_6)
thread_6.start()



#07
def com_setresult_7():
    global score_7
    while 1:
        if entry_7.get() == '':
            score_7 = 0
        else:
            score_7 = int(entry_7.get())
        text_v_result_7.set(score_7)
        time.sleep(0.1)

title_7 = tk.Label(window,text='修正分(上场分数或超出计算器部分分数)',font=('arial',15)).place(x=600,y=420)
result_7 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_7,state='readonly',relief='sunken')

entry_7 = Entry(window, show = None,font = ('Arial',15))
entry_7.place(x=615,y=450)

thread_7 = threading.Thread(target=com_setresult_7)
thread_7.start()



#08
def com_setresult_8():
    global score_8
    while 1:
        if entry_8.get() == '':
            score_8 = 0
        else:
            score_8 = int(entry_8.get())
        text_v_result_8.set(score_8)
        time.sleep(0.1)

title_8 = tk.Label(window,text='结算分',font=('arial',15)).place(x=600,y=360)
result_8 = Entry(window,bd=0,width=10,font=('arial',14),textvariable=text_v_result_8,state='readonly',relief='sunken')

entry_8 = Entry(window, show = None,font = ('Arial',15))
entry_8.place(x=615,y=390)

thread_8 = threading.Thread(target=com_setresult_8)
thread_8.start()




#00
def com_setresult_0():
    while 1:
        global score_0,score_1,score_2,score_31,score_32,score_4,score_5,score_6,score_7,score_8
        score_0 = str(score_1+score_2+score_31+score_4+score_5+score_6+score_7+score_32+score_8)
        text_v_result_0.set(score_0)
        time.sleep(0.1)

title_0 = tk.Label(window,text='总分',font=('arial',30)).place(x=5,y=560)
result_0 = Entry(window,bd=0,width=10,font=('arial',24),textvariable=text_v_result_0,state='readonly',relief='sunken')
result_0.place(x=15,y=630)

thread_0 = threading.Thread(target=com_setresult_0)
thread_0.start()


def shut():
    sys.exit()

but_shut = Button(window, text = '      关闭     ',font = ('Arial',40),command = shut)
but_shut.place(x=680,y=595)


def restart():
    p = sys.executable
    os.execl(p,p,*sys.argv)
    sys.exit()
    
but_clear = Button(window, text = '      重启     ',font = ('Arial',40),command = restart)
but_clear.place(x=360,y=595)

window.mainloop()