from tkinter import *
import tkinter as tk
import threading
import time
import os
import sys
from playsound import playsound


window = Tk()
window.title("仙术杯计算器(by椰蓉猫)")
window.geometry("1320x700")
window.resizable(width = False, height = False)

def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        int(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False



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

text_v_result_0_2 = StringVar()
text_v_result_0_5 = StringVar()
text_v_result_0_31 = StringVar()
text_v_result_0_32 = StringVar()
text_v_result_0_1 = StringVar()


##01
def com_setresult_1():
    global score_1_1,score_1_2,score_1_3,score_1
    score_1 = int(score_1_1)*50 + int(score_1_2)*20 + int(score_1_3)*10
    text_v_result_1.set(score_1)
    text_v_result_0_1.set(int(score_1_1)*'6星(50) ' + int(score_1_2)*'5星(20) ' + int(score_1_3)*'4星(10) ')

title_1 = tk.Label(window,text='临时招募',font=('黑体',15)).place(x=5,y=5)
result_1 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_1,state='readonly',relief='sunken').place(x=90,y=8)

score_1_1 = 0
def com_result_1_1(v):
    global score_1_1
    score_1_1 = v
    com_setresult_1()

title_1_1 = tk.Label(window,text='6星(50)',font=('黑体',11)).place(x=15,y=35)
scale_1_1 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_1_1)
scale_1_1.place(x=70,y=37)

score_1_2 = 0
def com_result_1_2(v):
    global score_1_2
    score_1_2 = v
    com_setresult_1()

title_1_2 = tk.Label(window,text='5星(20)',font=('黑体',11)).place(x=15,y=85)
scale_1_2 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_1_2)
scale_1_2.place(x=70,y=87)

score_1_3 = 0
def com_result_1_3(v):
    global score_1_3
    score_1_3 = v
    com_setresult_1()

title_1_3 = tk.Label(window,text='4星(10)',font=('黑体',11)).place(x=15,y=135)
scale_1_3 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_1_3)
scale_1_3.place(x=70,y=137)



##02
def com_setresult_2():
    global score_2
    while 1:
        score_2 = checkvar_2_1.get()*450+checkvar_2_2.get()*300+checkvar_2_3.get()*120+checkvar_2_4.get()*150+checkvar_2_5.get()*230
        text_v_result_2.set(score_2)
        text_v_result_0_2.set(checkvar_2_1.get()*'骑士(450)'+checkvar_2_2.get()*'水月(300)'+checkvar_2_3.get()*'锈锤(120)'+checkvar_2_4.get()*'寒灾(150)'+checkvar_2_5.get()*'墓碑(230)')
        time.sleep(0.1)

title_2 = tk.Label(window,text='结局',font=('黑体',15)).place(x=5,y=185)
result_2 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_2,state='readonly',relief='sunken').place(x=55,y=188)

checkvar_2_1 = IntVar()
checkvar_2_2 = IntVar()
checkvar_2_3 = IntVar()
checkvar_2_4 = IntVar()
checkvar_2_5 = IntVar()

checkbut_2_1 = Checkbutton(window,text='骑士(450)',font=('黑体',14),variable=checkvar_2_1,onvalue=1,offvalue=0)
checkbut_2_1.place(x=15,y=220)
checkbut_2_2 = Checkbutton(window,text='水月(300)',font=('黑体',14),variable=checkvar_2_2,onvalue=1,offvalue=0)
checkbut_2_2.place(x=15,y=255)
checkbut_2_3 = Checkbutton(window,text='锈锤(120)',font=('黑体',14),variable=checkvar_2_3,onvalue=1,offvalue=0)
checkbut_2_3.place(x=15,y=290)
checkbut_2_4 = Checkbutton(window,text='寒灾(150)',font=('黑体',14),variable=checkvar_2_4,onvalue=1,offvalue=0)
checkbut_2_4.place(x=15,y=325)
checkbut_2_5 = Checkbutton(window,text='墓碑(230)',font=('黑体',14),variable=checkvar_2_5,onvalue=1,offvalue=0)
checkbut_2_5.place(x=15,y=360)

thread_2 = threading.Thread(target=com_setresult_2)
thread_2.setDaemon(True)
thread_2.start()



#031
def com_setresult_3():
    global score_3_1,score_3_2,score_3_3,score_3_4,score_3_5,score_3_6,score_3_7,score_3_8,score_3_9,score_3_10,score_3_11,score_3_12,score_3_13,score_31
    score_31 = int(score_3_1)*40 + int(score_3_2)*40 + int(score_3_3)*100 + int(score_3_4)*60 + int(score_3_5)*40 + int(score_3_6)*50 + int(score_3_7)*120 + int(score_3_8)*90 + int(score_3_9)*90 + int(score_3_10)*90 + int(score_3_11)*50 + int(score_3_12)*150 + int(score_3_13)*80
    text_v_result_31.set(score_31)
    text_v_result_0_31.set(int(score_3_1)*'巢穴(40) ' + int(score_3_2)*'瞻前顾后(40) ' + int(score_3_3)*'领地意识(100) ' + int(score_3_4)*'狩猎场(60) ' + int(score_3_5)*'铳与秩序(40) ' + int(score_3_6)*'无漏溟痕乐园(50) ' + int(score_3_7)*'失控(120) ' + int(score_3_8)*'育生池(90) ' + int(score_3_9)*'好梦在何方(90) ' + int(score_3_10)*'余烬方阵(90) ' + int(score_3_11)*'机械之灾(50) ' + int(score_3_12)*'水火相容(150) ' + int(score_3_13)*'深度认知(80) ')

title_3 = tk.Label(window,text='紧急',font=('黑体',15)).place(x=300,y=5)
result_3 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_31,state='readonly',relief='sunken').place(x=350,y=8)

score_3_1 = 0
def com_result_3_1(v):
    global score_3_1
    score_3_1 = v
    com_setresult_3()

title_3_1 = tk.Label(window,text='巢穴(40)',font=('黑体',11)).place(x=310,y=35)
scale_3_1 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_1)
scale_3_1.place(x=440,y=37)

score_3_2 = 0
def com_result_3_2(v):
    global score_3_2
    score_3_2 = v
    com_setresult_3()

title_3_2 = tk.Label(window,text='瞻前顾后(40)',font=('黑体',11)).place(x=310,y=75)
scale_3_2 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_2)
scale_3_2.place(x=440,y=77)

score_3_3 = 0
def com_result_3_3(v):
    global score_3_3
    score_3_3 = v
    com_setresult_3()

title_3_3 = tk.Label(window,text='领地意识(100)',font=('黑体',11)).place(x=310,y=115)
scale_3_3 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_3)
scale_3_3.place(x=440,y=117)

score_3_4 = 0
def com_result_3_4(v):
    global score_3_4
    score_3_4 = v
    com_setresult_3()

title_3_4 = tk.Label(window,text='狩猎场(60)',font=('黑体',11)).place(x=310,y=155)
scale_3_4 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_4)
scale_3_4.place(x=440,y=157)

score_3_5 = 0
def com_result_3_5(v):
    global score_3_5
    score_3_5 = v
    com_setresult_3()

title_3_5 = tk.Label(window,text='铳与秩序(40)',font=('黑体',11)).place(x=310,y=195)
scale_3_5 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_5)
scale_3_5.place(x=440,y=197)

score_3_6 = 0
def com_result_3_6(v):
    global score_3_6
    score_3_6 = v
    com_setresult_3()

title_3_6 = tk.Label(window,text='无漏溟痕乐园(50)',font=('黑体',11)).place(x=310,y=235)
scale_3_6 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_6)
scale_3_6.place(x=440,y=237)

score_3_7 = 0
def com_result_3_7(v):
    global score_3_7
    score_3_7 = v
    com_setresult_3()

title_3_7 = tk.Label(window,text='失控(120)',font=('黑体',11)).place(x=310,y=275)
scale_3_7 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_7)
scale_3_7.place(x=440,y=277)

score_3_8 = 0
def com_result_3_8(v):
    global score_3_8
    score_3_8 = v
    com_setresult_3()

title_3_8 = tk.Label(window,text='育生池(90)',font=('黑体',11)).place(x=310,y=315)
scale_3_8 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_8)
scale_3_8.place(x=440,y=317)

score_3_9 = 0
def com_result_3_9(v):
    global score_3_9
    score_3_9 = v
    com_setresult_3()

title_3_9 = tk.Label(window,text='好梦在何方(90)',font=('黑体',11)).place(x=310,y=355)
scale_3_9 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_9)
scale_3_9.place(x=440,y=357)

score_3_10 = 0
def com_result_3_10(v):
    global score_3_10
    score_3_10 = v
    com_setresult_3()

title_3_10 = tk.Label(window,text='余烬方阵(90)',font=('黑体',11)).place(x=310,y=395)
scale_3_10 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_10)
scale_3_10.place(x=440,y=397)

score_3_11 = 0
def com_result_3_11(v):
    global score_3_11
    score_3_11 = v
    com_setresult_3()

title_3_11 = tk.Label(window,text='机械之灾(50)',font=('黑体',11)).place(x=310,y=435)
scale_3_11 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_11)
scale_3_11.place(x=440,y=437)

score_3_12 = 0
def com_result_3_12(v):
    global score_3_12
    score_3_12 = v
    com_setresult_3()

title_3_12 = tk.Label(window,text='水火相容(150)',font=('黑体',11)).place(x=310,y=475)
scale_3_12 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_12)
scale_3_12.place(x=440,y=477)

score_3_13 = 0
def com_result_3_13(v):
    global score_3_13
    score_3_13 = v
    com_setresult_3()

title_3_13 = tk.Label(window,text='深度认知(80)',font=('黑体',11)).place(x=310,y=515)
scale_3_13 = Scale(window, from_=0, to=2, orient=tk.HORIZONTAL, length=80, showvalue=0,tickinterval=1, resolution=1, command=com_result_3_13)
scale_3_13.place(x=440,y=517)



#032
def com_setresult_32():
    global score_32
    while 1:
        score_32 = checkvar_32_1.get()*30+checkvar_32_2.get()*50+checkvar_32_3.get()*100+checkvar_32_4.get()*50+checkvar_32_5.get()*100+checkvar_32_6.get()*80+checkvar_32_7.get()*50
        text_v_result_32.set(score_32)
        text_v_result_0_32.set(checkvar_32_1.get()*'监工现场击杀鸭子(30) '+checkvar_32_2.get()*'真相通关(50) '+checkvar_32_3.get()*'真相无漏(100) '+checkvar_32_4.get()*'跳舞通关(50) '+checkvar_32_5.get()*'跳舞无漏全收(100) '+checkvar_32_6.get()*'鸭本运作通关(80) '+checkvar_32_7.get()*'狂信如火无漏(50) ')
        time.sleep(0.1)

title_32 = tk.Label(window,text='事件',font=('黑体',15)).place(x=600,y=5)
result_32 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_32,state='readonly',relief='sunken').place(x=650,y=8)

checkvar_32_1 = IntVar()
checkvar_32_2 = IntVar()
checkvar_32_3 = IntVar()
checkvar_32_4 = IntVar()
checkvar_32_5 = IntVar()
checkvar_32_6 = IntVar()
checkvar_32_7 = IntVar()

checkbut_32_1 = Checkbutton(window,text='监工现场击杀鸭子(30)',font=('黑体',14),variable=checkvar_32_1,onvalue=1,offvalue=0).place(x=610,y=40)
checkbut_32_2 = Checkbutton(window,text='真相通关(50)',font=('黑体',14),variable=checkvar_32_2,onvalue=1,offvalue=0).place(x=610,y=75)
checkbut_32_3 = Checkbutton(window,text='真相无漏(100)',font=('黑体',14),variable=checkvar_32_3,onvalue=1,offvalue=0).place(x=610,y=110)
checkbut_32_4 = Checkbutton(window,text='跳舞通关(50)',font=('黑体',14),variable=checkvar_32_4,onvalue=1,offvalue=0).place(x=610,y=145)
checkbut_32_5 = Checkbutton(window,text='跳舞无漏全收(100)',font=('黑体',14),variable=checkvar_32_5,onvalue=1,offvalue=0).place(x=610,y=180)
checkbut_32_6 = Checkbutton(window,text='鸭本运作通关(80)',font=('黑体',14),variable=checkvar_32_6,onvalue=1,offvalue=0).place(x=610,y=215)
checkbut_32_7 = Checkbutton(window,text='狂信如火无漏(50)',font=('黑体',14),variable=checkvar_32_7,onvalue=1,offvalue=0).place(x=610,y=250)

thread_32 = threading.Thread(target=com_setresult_32)
thread_32.setDaemon(True)
thread_32.start()



#04
def com_setresult_4():
    global score_4
    while 1:
        if entry_4.get() == '':
            score_4 = 0
        elif is_number(entry_4.get()):
            score_4 = int(entry_4.get())*10
        text_v_result_4.set(score_4)
        time.sleep(0.1)

title_4 = tk.Label(window,text='藏品',font=('黑体',15)).place(x=600,y=360)
result_4 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_4,state='readonly',relief='sunken').place(x=655,y=363)

entry_4 = Entry(window, show = None,font = ('黑体',15))
entry_4.place(x=615,y=390)

thread_4 = threading.Thread(target=com_setresult_4)
thread_4.setDaemon(True)
thread_4.start()



#05
def com_setresult_5():
    global score_5_1,score_5_2,score_5_3,score_5
    score_5 = (int(score_5_1) + int(score_5_2) + int(score_5_3))*20
    text_v_result_0_5.set('鸭子(20) '*int(score_5_1)+'狗头(20) '*int(score_5_2)+'熊(20) '*int(score_5_3))
    text_v_result_5.set(score_5)
    time.sleep(0.1)

title_5 = tk.Label(window,text='隐藏怪',font=('黑体',15)).place(x=5,y=410)
result_5 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_5,state='readonly',relief='sunken').place(x=75,y=413)

score_5_1 = 0
def com_result_5_1(v):
    global score_5_1
    score_5_1 = v
    com_setresult_5()

title_5_1 = tk.Label(window,text='鸭子(20)',font=('黑体',11)).place(x=5,y=440)
scale_5_1 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_5_1)
scale_5_1.place(x=70,y=443)

score_5_2 = 0
def com_result_5_2(v):
    global score_5_2
    score_5_2 = v
    com_setresult_5()

title_5_2 = tk.Label(window,text='狗头(20)',font=('黑体',11)).place(x=5,y=490)
scale_5_2 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_5_2)
scale_5_2.place(x=70,y=493)

score_5_3 = 0
def com_result_5_3(v):
    global score_5_3
    score_5_3 = v
    com_setresult_5()

title_5_3 = tk.Label(window,text='熊(20)',font=('黑体',11)).place(x=5,y=540)
scale_5_3 = Scale(window, from_=0, to=8, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_5_3)
scale_5_3.place(x=70,y=543)

thread_5 = threading.Thread(target=com_setresult_5)
thread_5.setDaemon(True)
thread_5.start()

#06
def com_setresult_6():
    global score_6
    text_v_result_6.set(score_6)
        

title_6 = tk.Label(window,text='启示',font=('黑体',15)).place(x=600,y=310)
result_6 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_6,state='readonly',relief='sunken').place(x=655,y=313)

def com_result_6(v):
    global score_6
    score_6 = int(v)*50
    com_setresult_6()

scale_6 = Scale(window, from_=0, to=7, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=1, resolution=1, command=com_result_6)
scale_6.place(x=700,y=313)


#07
def com_setresult_7():
    global score_7
    while 1:
        if entry_7.get() == '':
            score_7 = 0
        elif is_number(entry_7.get()):
            score_7 = int(entry_7.get())
        text_v_result_7.set(score_7)
        time.sleep(0.1)

title_7 = tk.Label(window,text='修正分',font=('黑体',15)).place(x=600,y=480)
result_7 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_7,state='readonly',relief='sunken')

entry_7 = Entry(window, show = None,font = ('黑体',15))
entry_7.place(x=615,y=510)

thread_7 = threading.Thread(target=com_setresult_7)
thread_7.setDaemon(True)
thread_7.start()



#08
def com_setresult_8():
    global score_8
    while 1:
        if entry_8.get() == '':
            score_8 = 0
        elif is_number(entry_8.get()):
            score_8 = int(entry_8.get())
        text_v_result_8.set(score_8)
        time.sleep(0.1)

title_8 = tk.Label(window,text='结算分',font=('黑体',15)).place(x=600,y=420)
result_8 = Entry(window,bd=0,width=10,font=('黑体',14),textvariable=text_v_result_8,state='readonly',relief='sunken')

entry_8 = Entry(window, show = None,font = ('黑体',15))
entry_8.place(x=615,y=450)

thread_8 = threading.Thread(target=com_setresult_8)
thread_8.setDaemon(True)
thread_8.start()




#00
def com_setresult_0():
    while 1:
        global score_0,score_1,score_2,score_31,score_32,score_4,score_5,score_6,score_7,score_8
        if score_1+score_2+score_31+score_4+score_5+score_6+score_7+score_32+score_8 >= 3020:
            score_0 = str(score_1+score_2+score_31+score_4+score_5+score_6+score_7+score_32+score_8) + '!'
        else:
            score_0 = str(score_1+score_2+score_31+score_4+score_5+score_6+score_7+score_32+score_8)
        text_v_result_0.set(score_0)
        time.sleep(0.1)

title_0 = tk.Label(window,text='总分',font=('黑体',30)).place(x=960,y=5)
result_0 = Entry(window,bd=0,width=10,font=('黑体',24),textvariable=text_v_result_0,state='readonly',relief='sunken')
result_0.place(x=1060,y=12)



##结局
result_0_2 = Message(window,bd=0,width=280,font=('黑体',16),textvariable=text_v_result_0_2,fg='blue').place(x=952,y=63)
##临招
result_0_1 = Message(window,bd=0,width=280,font=('黑体',17),textvariable=text_v_result_0_1,fg='orange').place(x=952,y=113)
##隐藏怪
result_0_5 = Message(window,bd=0,width=280,font=('黑体',17),textvariable=text_v_result_0_5,fg='purple').place(x=952,y=223)
##紧急
result_0_31 = Message(window,bd=0,width=280,font=('黑体',17),textvariable=text_v_result_0_31,fg='red').place(x=952,y=313)
##事件
result_0_32 = Message(window,bd=0,width=280,font=('黑体',17),textvariable=text_v_result_0_32,fg='green').place(x=952,y=553)





thread_0 = threading.Thread(target=com_setresult_0)
thread_0.setDaemon(True)
thread_0.start()







def clear():
    scale_1_1.set(0)
    scale_1_2.set(0)
    scale_1_3.set(0)
    checkvar_2_1.set(0)
    checkvar_2_2.set(0)
    checkvar_2_3.set(0)
    checkvar_2_4.set(0)
    checkvar_2_5.set(0)
    scale_3_1.set(0)
    scale_3_2.set(0)
    scale_3_3.set(0)
    scale_3_4.set(0)
    scale_3_5.set(0)
    scale_3_6.set(0)
    scale_3_7.set(0)
    scale_3_8.set(0)
    scale_3_9.set(0)
    scale_3_10.set(0)
    scale_3_11.set(0)
    scale_3_12.set(0)
    scale_3_13.set(0)
    checkvar_32_1.set(0)
    checkvar_32_2.set(0)
    checkvar_32_3.set(0)
    checkvar_32_4.set(0)
    checkvar_32_5.set(0)
    checkvar_32_6.set(0)
    checkvar_32_7.set(0)
    entry_4.delete(0,END)
    scale_5_1.set(0)
    scale_5_2.set(0)
    scale_5_3.set(0)
    scale_6.set(0)
    entry_7.delete(0,END)
    entry_8.delete(0,END)
    playsound('guiling.mp3')

    

    

but_clear = Button(window, text = '              归零!              ',font = ('黑体',40),command = clear,fg='red')
but_clear.place(x=0,y=607)

window.mainloop()