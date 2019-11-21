from tkinter import *
import random
import datetime
# import pypyodbc
import time

# создаем главное окно
root = Tk()
root.title("Это великолепная программа с терминалом и цехом")
root.configure(background="gray74")
root.geometry('1024x860')

# connection = pypyodbc.connect('Driver={SQL Server};'
#                               'Server=AHTUCTPECC-PK;'
#                               'Database=LabACY;')

# -----------------Описание терминала---------------------------
term = Canvas(root, width=270, height=250, bg="gray47")
term.place(relx=0.01, rely=0.06, anchor=NW)

term_label = Label(root, text="Терминал", font="Verdana16")
term_label.place(relx=0.15, rely=0.06, anchor=S)
# term.create_text(20+120, 30, text="Терминал", font="Verdana 14", fill="grey7", anchor=S)

term_dat_1 = Label(root, text="Датчик1", font="Verdana14")
term_dat_1.place(relx=0.02, rely=0.358-0.288, anchor=NW)

term_dat_2 = Label(root, text="Датчик2", font="Verdana14")
term_dat_2.place(relx=0.02, rely=0.358+0.04-0.288, anchor=NW)

term_dat_3 = Label(root, text="Датчик3", font="Verdana14")
term_dat_3.place(relx=0.02, rely=0.358+0.08-0.288, anchor=NW)

term_dat_4 = Label(root, text="Датчик4", font="Verdana14")
term_dat_4.place(relx=0.02, rely=0.358+0.12-0.288, anchor=NW)

term_dat_5 = Label(root, text="Датчик5", font="Verdana14")
term_dat_5.place(relx=0.02, rely=0.358+0.16-0.288, anchor=NW)
#
# term_dat_6 = Label(root, text="Датчик5", font="Verdana14")
# term_dat_6.place(relx=0.032, rely=0.358+0.20, anchor=NW)
#
# term_dat_7 = Label(root, text="Датчик6", font="Verdana14")
# term_dat_7.place(relx=0.032, rely=0.358+0.24, anchor=NW)
#
# term_dat_8 = Label(root, text="Датчик8", font="Verdana14")
# term_dat_8.place(relx=0.032, rely=0.358+0.28, anchor=NW)
#
# term_dat_9 = Label(root, text="Датчик9", font="Verdana14")
# term_dat_9.place(relx=0.032, rely=0.358+0.32, anchor=NW)
#
# term_dat_10 = Label(root, text="Датчик10", font="Verdana14")
# term_dat_10.place(relx=0.025, rely=0.358+0.36, anchor=NW)

sost = Canvas(root, width=200, height=20)
sost.place(relx=0.37, rely=0.01, anchor=NW)

tim = Canvas(root, width=50, height=20)
tim.place(relx=0.01, rely=0.01, anchor=NW)

# ------------------------------------------------------------

zn_dat_1 = Canvas(root, width=40, height=21)
zn_dat_1.place(relx=0.09, rely=0.358-0.288, anchor=NW)

zn_dat_2 = Canvas(root, width=40, height=21)
zn_dat_2.place(relx=0.09, rely=0.358+0.04-0.288, anchor=NW)

zn_dat_3 = Canvas(root, width=40, height=21)
zn_dat_3.place(relx=0.09, rely=0.358+0.08-0.288, anchor=NW)

zn_dat_4 = Canvas(root, width=40, height=21)
zn_dat_4.place(relx=0.09, rely=0.358+0.12-0.288, anchor=NW)

zn_dat_5 = Canvas(root, width=40, height=21)
zn_dat_5.place(relx=0.09, rely=0.358+0.16-0.288, anchor=NW)
#
# zn_dat_6 = Canvas(root, width=40, height=21)
# zn_dat_6.place(relx=0.1, rely=0.358+0.20, anchor=NW)
#
# zn_dat_7 = Canvas(root, width=40, height=21)
# zn_dat_7.place(relx=0.1, rely=0.358+0.24, anchor=NW)
#
# zn_dat_8 = Canvas(root, width=40, height=21)
# zn_dat_8.place(relx=0.1, rely=0.358+0.28, anchor=NW)
#
# zn_dat_9 = Canvas(root, width=40, height=21)
# zn_dat_9.place(relx=0.1, rely=0.358+0.32, anchor=NW)
#
# zn_dat_10 = Canvas(root, width=40, height=21)
# zn_dat_10.place(relx=0.1, rely=0.358+0.36, anchor=NW)
# ----------- Холсты под графики-------------------------------
graph_1 = Canvas(root, width=280, height=50)
graph_1.place(relx=0.34, rely=0.39-0.34, anchor=NW)

graph_2 = Canvas(root, width=280, height=50)
graph_2.place(relx=0.34, rely=0.39+0.08-0.34, anchor=NW)

graph_3 = Canvas(root, width=280, height=50)
graph_3.place(relx=0.34, rely=0.39+0.16-0.34, anchor=NW)

graph_4 = Canvas(root, width=280, height=50)
graph_4.place(relx=0.34, rely=0.39+0.24-0.34, anchor=NW)

graph_5 = Canvas(root, width=280, height=50)
graph_5.place(relx=0.34, rely=0.39+0.32-0.34, anchor=NW)
# --------------------------------------------------------------

# --------------------Номера графиков --------------------------
grterm_dat_1 = Label(root, text="[1]", font="Verdana14")
grterm_dat_1.place(relx=0.315, rely=0.39-0.325, anchor=NE)

grterm_dat_2 = Label(root, text="[2]", font="Verdana14")
grterm_dat_2.place(relx=0.315, rely=0.39+0.08-0.325, anchor=NE)

grterm_dat_3 = Label(root, text="[3]", font="Verdana14")
grterm_dat_3.place(relx=0.315, rely=0.39+0.16-0.325, anchor=NE)

grterm_dat_4 = Label(root, text="[4]", font="Verdana14")
grterm_dat_4.place(relx=0.315, rely=0.39+0.24-0.325, anchor=NE)

grterm_dat_5 = Label(root, text="[5]", font="Verdana14")
grterm_dat_5.place(relx=0.315, rely=0.39+0.32-0.325, anchor=NE)
# ---------------------------------------------------------------

# --------------------Номера графиков --------------------------
grterm_dat_1 = Label(root, text="50\n\n10\n0", font="Verdana 7")
grterm_dat_1.place(relx=0.34, rely=0.39-0.309, anchor=E)

grterm_dat_2 = Label(root, text="50\n0\n\n-50", font="Verdana 7")
grterm_dat_2.place(relx=0.34, rely=0.39+0.08-0.308, anchor=E)

grterm_dat_3 = Label(root, text="17\n\n6\n1", font="Verdana 7")
grterm_dat_3.place(relx=0.34, rely=0.39+0.16-0.308, anchor=E)

grterm_dat_4 = Label(root, text="1\n\n\n0", font="Verdana 7")
grterm_dat_4.place(relx=0.34, rely=0.39+0.24-0.309, anchor=E)

grterm_dat_5 = Label(root, text="80\n70\n0\n-20", font="Verdana 7")
grterm_dat_5.place(relx=0.34, rely=0.39+0.32-0.309, anchor=E)

now = datetime.datetime.now()

time_bar_1_0 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_1_0.place(relx=0.36, rely=0.39-0.269, anchor=E)

time_bar_1_1 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_1_1.place(relx=0.41, rely=0.39-0.269, anchor=E)

time_bar_1_2 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_1_2.place(relx=0.465, rely=0.39-0.269, anchor=E)

time_bar_1_3 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_1_3.place(relx=0.52, rely=0.39-0.269, anchor=E)

time_bar_1_4 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_1_4.place(relx=0.573, rely=0.39-0.269, anchor=E)

time_bar_2_0 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_2_0.place(relx=0.36, rely=0.39-0.189, anchor=E)

time_bar_2_1 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_2_1.place(relx=0.41, rely=0.39-0.189, anchor=E)

time_bar_2_2 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_2_2.place(relx=0.465, rely=0.39-0.189, anchor=E)

time_bar_2_3 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_2_3.place(relx=0.52, rely=0.39-0.189, anchor=E)

time_bar_2_4 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_2_4.place(relx=0.573, rely=0.39-0.189, anchor=E)

time_bar_3_0 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_3_0.place(relx=0.36, rely=0.39-0.1114, anchor=E)

time_bar_3_1 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_3_1.place(relx=0.41, rely=0.39-0.1114, anchor=E)

time_bar_3_2 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_3_2.place(relx=0.465, rely=0.39-0.1114, anchor=E)

time_bar_3_3 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_3_3.place(relx=0.52, rely=00.39-0.1114, anchor=E)

time_bar_3_4 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_3_4.place(relx=0.573, rely=0.39-0.1114, anchor=E)

time_bar_4_0 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_4_0.place(relx=0.36, rely=0.36, anchor=E)

time_bar_4_1 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_4_1.place(relx=0.41, rely=0.36, anchor=E)

time_bar_4_2 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_4_2.place(relx=0.465, rely=0.36, anchor=E)

time_bar_4_3 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_4_3.place(relx=0.52, rely=0.36, anchor=E)

time_bar_4_4 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_4_4.place(relx=0.573, rely=0.36, anchor=E)

time_bar_5_0 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_5_0.place(relx=0.36, rely=0.44, anchor=E)

time_bar_5_1 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_5_1.place(relx=0.41, rely=0.44, anchor=E)

time_bar_5_2 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_5_2.place(relx=0.465, rely=0.44, anchor=E)

time_bar_5_3 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_5_3.place(relx=0.52, rely=0.44, anchor=E)

time_bar_5_4 = Label(root, text=now.strftime("%M:%S"), font="Verdana 6")
time_bar_5_4.place(relx=0.573, rely=0.44, anchor=E)


# ---------------------------------------------------------------


# ----------------Описание Буфера------------------------------------

# ----------------Первая строка--------------------------------------
# buffer = Canvas(root, width=340, height=350, bg="gray45")
# buffer.place(relx=0.59, rely=0.059, anchor=NW)

# buffer_1_1 = Canvas(root, width=40, height=25)
# buffer_1_1.place(relx=0.50, rely=0.059, anchor=NW)
#
# buffer_1_2 = Canvas(root, width=40, height=25)
# buffer_1_2.place(relx=0.50+0.048, rely=0.059, anchor=NW)
#
# buffer_1_3 = Canvas(root, width=40, height=25)
# buffer_1_3.place(relx=0.50+0.096, rely=0.059, anchor=NW)

buffer_1_4 = Canvas(root, width=40, height=25)
buffer_1_4.place(relx=0.50+0.144, rely=0.059, anchor=NW)

buffer_1_5 = Canvas(root, width=40, height=25)
buffer_1_5.place(relx=0.50+0.192, rely=0.059, anchor=NW)

buffer_1_6 = Canvas(root, width=40, height=25)
buffer_1_6.place(relx=0.50+0.240, rely=0.059, anchor=NW)

buffer_1_7 = Canvas(root, width=40, height=25)
buffer_1_7.place(relx=0.50+0.288, rely=0.059, anchor=NW)

buffer_1_8 = Canvas(root, width=40, height=25)
buffer_1_8.place(relx=0.50+0.336, rely=0.059, anchor=NW)

# buffer_1_9 = Canvas(root, width=40, height=25)
# buffer_1_9.place(relx=0.50+0.384, rely=0.059, anchor=NW)
#
# buffer_1_10 = Canvas(root, width=40, height=25)
# buffer_1_10.place(relx=0.50+0.432, rely=0.059, anchor=NW)
# ---------------------------------------------------------------------
# -------------------Вторая строка-------------------------------------
buffer_2_4 = Canvas(root, width=40, height=25)
buffer_2_4.place(relx=0.50+0.144, rely=0.059+0.038, anchor=NW)

buffer_2_5 = Canvas(root, width=40, height=25)
buffer_2_5.place(relx=0.50+0.192, rely=0.059+0.038, anchor=NW)

buffer_2_6 = Canvas(root, width=40, height=25)
buffer_2_6.place(relx=0.50+0.240, rely=0.059+0.038, anchor=NW)

buffer_2_7 = Canvas(root, width=40, height=25)
buffer_2_7.place(relx=0.50+0.288, rely=0.059+0.038, anchor=NW)

buffer_2_8 = Canvas(root, width=40, height=25)
buffer_2_8.place(relx=0.50+0.336, rely=0.059+0.038, anchor=NW)
# ----------------------------------------------------------------------

# -----------------------3------------------------------------------
buffer_3_4 = Canvas(root, width=40, height=25)
buffer_3_4.place(relx=0.50+0.144, rely=0.059+0.076, anchor=NW)

buffer_3_5 = Canvas(root, width=40, height=25)
buffer_3_5.place(relx=0.50+0.192, rely=0.059+0.076, anchor=NW)

buffer_3_6 = Canvas(root, width=40, height=25)
buffer_3_6.place(relx=0.50+0.240, rely=0.059+0.076, anchor=NW)

buffer_3_7 = Canvas(root, width=40, height=25)
buffer_3_7.place(relx=0.50+0.288, rely=0.059+0.076, anchor=NW)

buffer_3_8 = Canvas(root, width=40, height=25)
buffer_3_8.place(relx=0.50+0.336, rely=0.059+0.076, anchor=NW)
# --------------------------------------------------------------------

# -----------------------4------------------------------------------
buffer_4_4 = Canvas(root, width=40, height=25)
buffer_4_4.place(relx=0.50+0.144, rely=0.059+0.114, anchor=NW)

buffer_4_5 = Canvas(root, width=40, height=25)
buffer_4_5.place(relx=0.50+0.192, rely=0.059+0.114, anchor=NW)

buffer_4_6 = Canvas(root, width=40, height=25)
buffer_4_6.place(relx=0.50+0.240, rely=0.059+0.114, anchor=NW)

buffer_4_7 = Canvas(root, width=40, height=25)
buffer_4_7.place(relx=0.50+0.288, rely=0.059+0.114, anchor=NW)

buffer_4_8 = Canvas(root, width=40, height=25)
buffer_4_8.place(relx=0.50+0.336, rely=0.059+0.114, anchor=NW)
# --------------------------------------------------------------------

# -----------------------5------------------------------------------
buffer_5_4 = Canvas(root, width=40, height=25)
buffer_5_4.place(relx=0.50+0.144, rely=0.059+0.152, anchor=NW)

buffer_5_5 = Canvas(root, width=40, height=25)
buffer_5_5.place(relx=0.50+0.192, rely=0.059+0.152, anchor=NW)

buffer_5_6 = Canvas(root, width=40, height=25)
buffer_5_6.place(relx=0.50+0.240, rely=0.059+0.152, anchor=NW)

buffer_5_7 = Canvas(root, width=40, height=25)
buffer_5_7.place(relx=0.50+0.288, rely=0.059+0.152, anchor=NW)

buffer_5_8 = Canvas(root, width=40, height=25)
buffer_5_8.place(relx=0.50+0.336, rely=0.059+0.152, anchor=NW)
# -------------------------------------------------------------------

# -----------------------6------------------------------------------
buffer_6_4 = Canvas(root, width=40, height=25)
buffer_6_4.place(relx=0.50+0.144, rely=0.059+0.190, anchor=NW)

buffer_6_5 = Canvas(root, width=40, height=25)
buffer_6_5.place(relx=0.50+0.192, rely=0.059+0.190, anchor=NW)

buffer_6_6 = Canvas(root, width=40, height=25)
buffer_6_6.place(relx=0.50+0.240, rely=0.059+0.190, anchor=NW)

buffer_6_7 = Canvas(root, width=40, height=25)
buffer_6_7.place(relx=0.50+0.288, rely=0.059+0.190, anchor=NW)

buffer_6_8 = Canvas(root, width=40, height=25)
buffer_6_8.place(relx=0.50+0.336, rely=0.059+0.190, anchor=NW)
# -------------------------------------------------------------------

# -----------------------7------------------------------------------
buffer_7_4 = Canvas(root, width=40, height=25)
buffer_7_4.place(relx=0.50+0.144, rely=0.059+0.228, anchor=NW)

buffer_7_5 = Canvas(root, width=40, height=25)
buffer_7_5.place(relx=0.50+0.192, rely=0.059+0.228, anchor=NW)

buffer_7_6 = Canvas(root, width=40, height=25)
buffer_7_6.place(relx=0.50+0.240, rely=0.059+0.228, anchor=NW)

buffer_7_7 = Canvas(root, width=40, height=25)
buffer_7_7.place(relx=0.50+0.288, rely=0.059+0.228, anchor=NW)

buffer_7_8 = Canvas(root, width=40, height=25)
buffer_7_8.place(relx=0.50+0.336, rely=0.059+0.228, anchor=NW)
# -------------------------------------------------------------------

# -----------------------8------------------------------------------
buffer_8_4 = Canvas(root, width=40, height=25)
buffer_8_4.place(relx=0.50+0.144, rely=0.059+0.266, anchor=NW)

buffer_8_5 = Canvas(root, width=40, height=25)
buffer_8_5.place(relx=0.50+0.192, rely=0.059+0.266, anchor=NW)

buffer_8_6 = Canvas(root, width=40, height=25)
buffer_8_6.place(relx=0.50+0.240, rely=0.059+0.266, anchor=NW)

buffer_8_7 = Canvas(root, width=40, height=25)
buffer_8_7.place(relx=0.50+0.288, rely=0.059+0.266, anchor=NW)

buffer_8_8 = Canvas(root, width=40, height=25)
buffer_8_8.place(relx=0.50+0.336, rely=0.059+0.266, anchor=NW)
# -------------------------------------------------------------------

# -----------------------9------------------------------------------
buffer_9_4 = Canvas(root, width=40, height=25)
buffer_9_4.place(relx=0.50+0.144, rely=0.059+0.304, anchor=NW)

buffer_9_5 = Canvas(root, width=40, height=25)
buffer_9_5.place(relx=0.50+0.192, rely=0.059+0.304, anchor=NW)

buffer_9_6 = Canvas(root, width=40, height=25)
buffer_9_6.place(relx=0.50+0.240, rely=0.059+0.304, anchor=NW)

buffer_9_7 = Canvas(root, width=40, height=25)
buffer_9_7.place(relx=0.50+0.288, rely=0.059+0.304, anchor=NW)

buffer_9_8 = Canvas(root, width=40, height=25)
buffer_9_8.place(relx=0.50+0.336, rely=0.059+0.304, anchor=NW)
# -------------------------------------------------------------------

# -----------------------10------------------------------------------
buffer_10_4 = Canvas(root, width=40, height=25)
buffer_10_4.place(relx=0.50+0.144, rely=0.059+0.342, anchor=NW)

buffer_10_5 = Canvas(root, width=40, height=25)
buffer_10_5.place(relx=0.50+0.192, rely=0.059+0.342, anchor=NW)

buffer_10_6 = Canvas(root, width=40, height=25)
buffer_10_6.place(relx=0.50+0.240, rely=0.059+0.342, anchor=NW)

buffer_10_7 = Canvas(root, width=40, height=25)
buffer_10_7.place(relx=0.50+0.288, rely=0.059+0.342, anchor=NW)

buffer_10_8 = Canvas(root, width=40, height=25)
buffer_10_8.place(relx=0.50+0.336, rely=0.059+0.342, anchor=NW)

buffer_label = Label(root, text="Буфер", font="Verdana16")
buffer_label.place(relx=0.76, rely=0.05, anchor=S)
# buffer.create_text(170, 30, text="Буфер", font="Verdana 14", fill="grey7", anchor=S)
# --------------------------------------------------------------------------

# ------------------Описание Цеха--------------------------------------------
ceh_label = Label(root, text="Цех", font="Verdana16")
ceh_label.place(relx=0.73, rely=0.588, anchor=S)

fra = Frame(root, width=600, height=70)
fra.place(x=420, y=510)

ceh = Text(fra, width=82, height=24, font="Verdana 8", wrap=WORD)
ceh.pack(side=LEFT)
# ceh.place(relx=0.47, rely=0.588, anchor=NW)

scroll = Scrollbar(fra, command=ceh.yview)
scroll.pack(side=RIGHT, fill=BOTH)

ceh.config(yscrollcommand=scroll.set)



# fra = Frame(root, width=425, height=50)
# fra.place(x=600, y=500)
# tx = Text(fra, width=63, height=17, wrap=WORD)
# scr = Scrollbar(fra, command=tx.yview)
# tx.configure(yscrollcommand=scr.set)
# scr.pack(fill=BOTH, side=RIGHT)
# tx.pack()
# ceh.create_text(170, 30, text="Цех", font="Verdana 14", fill="grey7", anchor=S)
# -----------------------------------------------------------------------------------

#
# zn_dat_1 = Canvas(root, width=40, height=21)
# zn_dat_1.place(relx=0.1, rely=0.358, anchor=NW)
#
# zn_dat_2 = Canvas(root, width=40, height=21)
# zn_dat_2.place(relx=0.1, rely=0.358+0.04, anchor=NW)
#

# ---------------------Кнопки---------------------------------------------------------
btn1 = Button(text="Генерировать")
btn1.place(relx=0.227, rely=0.358-0.288, anchor="ne")
# ------------------------------------------------------------------------------------
btn2 = Button(text="Оборвать связь")
btn2.place(relx=0.27, rely=0.358+0.04-0.288, anchor="ne")
# -------------------------------------------------------------------------------------
btn3 = Button(text="Восстановить связь")
btn3.place(relx=0.27, rely=0.358+0.08-0.288, anchor="ne")
# -------------------------------------------------------------------------------------
btn4 = Button(text="Стоп")
btn4.place(relx=0.27, rely=0.358-0.288, anchor="ne")
# btn4 = Button(text="Остановить")
# btn4.place(relx=0.33, rely=0.358+0.12, anchor="ne")
# ------------------------------------------------------------------------------------
# canv = Canvas(root, width=1024, height=860, bg="lightblue")
#
# canv.create_rectangle(20, 300, 300, 700, fill="saddle brown", outline="black")
# canv.create_text(20+140, 300, text="Терминал", font="Verdana 14", fill="grey7", anchor=S)
#
# canv.create_rectangle(600, 50, 940, 400, fill="gray45", outline="black")
# canv.create_text(600+170, 50, text="Буфер", font="Verdana 14", fill="grey7", anchor=S)
#
# canv.create_rectangle(600, 550, 940, 800, fill="chartreuse4", outline="black")
# canv.create_text(600+170, 550, text="Цех", font="Verdana 14", fill="grey7", anchor=S)
# root.mainloop()








signal = 1



# Создание буфера
buf0 = [0, 0, 0, 0, 0, 0]
buf1 = [0, 0, 0, 0, 0, 0]
buf2 = [0, 0, 0, 0, 0, 0]
buf3 = [0, 0, 0, 0, 0, 0]
buf4 = [0, 0, 0, 0, 0, 0]
buf5 = [0, 0, 0, 0, 0, 0]
buf6 = [0, 0, 0, 0, 0, 0]
buf7 = [0, 0, 0, 0, 0, 0]
buf8 = [0, 0, 0, 0, 0, 0]
buf9 = [0, 0, 0, 0, 0, 0]

buf = [buf0, buf1, buf2, buf3, buf4, buf5, buf6, buf7, buf8, buf9]
# Вроде буфер готов

numb = 0

graph0 = [0, 0, 0, 0, 0]
graph1 = [0, 0, 0, 0, 0]
graph2 = [0, 0, 0, 0, 0]
graph3 = [0, 0, 0, 0, 0]
graph4 = [0, 0, 0, 0, 0]
graph = [graph0, graph1, graph2, graph3, graph4]

# ЭКСПЕРИМЕНТЫ ----------------------------------------------------------------------------------------
# list1 = [random.randint(0, 50), random.randint(-50, 50), random.uniform(1, 17), random.randint(0, 1)]
# for numb in range(5):
#     buf[numb] = list1
#     print(str(buf[numb]))
#
#
#
# now = datetime.datetime.now()
# print(now.strftime("%d-%m-%Y %H:%M:"))
#
# -------------------------------------------------------------------------------------------------------

i = 0

# def clear_buff():
#     j = 0
#     global buffer_1_4, buffer_1_5, buffer_1_6, buffer_1_7, buffer_1_8
#     global buffer_2_4, buffer_2_5, buffer_2_6, buffer_2_7, buffer_3_8
#     global buffer_3_4, buffer_3_5, buffer_3_6, buffer_3_7, buffer_3_8
#     global buffer_4_4, buffer_4_5, buffer_4_6, buffer_4_7, buffer_4_8
#     global buffer_5_4, buffer_5_5, buffer_5_6, buffer_5_7, buffer_5_8
#     global buffer_6_4, buffer_6_5, buffer_6_6, buffer_6_7, buffer_6_8
#     global buffer_7_4, buffer_7_5, buffer_7_6, buffer_7_7, buffer_7_8
#     global buffer_8_4, buffer_8_5, buffer_8_6, buffer_8_7, buffer_8_8
#     global buffer_9_4, buffer_9_5, buffer_9_6, buffer_9_7, buffer_9_8
#     global buffer_10_4, buffer_10_5, buffer_10_6, buffer_10_7, buffer_10_8
#     global i
#     for j in range(i):
#


def delete_buff():
    global buffer_1_4, buffer_1_5, buffer_1_6, buffer_1_7, buffer_1_8
    global buffer_2_4, buffer_2_5, buffer_2_6, buffer_2_7, buffer_3_8
    global buffer_3_4, buffer_3_5, buffer_3_6, buffer_3_7, buffer_3_8
    global buffer_4_4, buffer_4_5, buffer_4_6, buffer_4_7, buffer_4_8
    global buffer_5_4, buffer_5_5, buffer_5_6, buffer_5_7, buffer_5_8
    global buffer_6_4, buffer_6_5, buffer_6_6, buffer_6_7, buffer_6_8
    global buffer_7_4, buffer_7_5, buffer_7_6, buffer_7_7, buffer_7_8
    global buffer_8_4, buffer_8_5, buffer_8_6, buffer_8_7, buffer_8_8
    global buffer_9_4, buffer_9_5, buffer_9_6, buffer_9_7, buffer_9_8
    global buffer_10_4, buffer_10_5, buffer_10_6, buffer_10_7, buffer_10_8
    global buf

    buf[0] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[1] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[2] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[3] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[4] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[5] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[6] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[7] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[8] = [NONE, NONE, NONE, NONE, NONE, NONE]
    buf[9] = [NONE, NONE, NONE, NONE, NONE, NONE]

    buffer_1_4.delete(ALL)
    buffer_1_5.delete(ALL)
    buffer_1_6.delete(ALL)
    buffer_1_7.delete(ALL)
    buffer_1_8.delete(ALL)

    buffer_2_4.delete(ALL)
    buffer_2_5.delete(ALL)
    buffer_2_6.delete(ALL)
    buffer_2_7.delete(ALL)
    buffer_2_8.delete(ALL)

    buffer_3_4.delete(ALL)
    buffer_3_5.delete(ALL)
    buffer_3_6.delete(ALL)
    buffer_3_7.delete(ALL)
    buffer_3_8.delete(ALL)

    buffer_4_4.delete(ALL)
    buffer_4_5.delete(ALL)
    buffer_4_6.delete(ALL)
    buffer_4_7.delete(ALL)
    buffer_4_8.delete(ALL)

    buffer_5_4.delete(ALL)
    buffer_5_5.delete(ALL)
    buffer_5_6.delete(ALL)
    buffer_5_7.delete(ALL)
    buffer_5_8.delete(ALL)

    buffer_6_4.delete(ALL)
    buffer_6_5.delete(ALL)
    buffer_6_6.delete(ALL)
    buffer_6_7.delete(ALL)
    buffer_6_8.delete(ALL)

    buffer_7_4.delete(ALL)
    buffer_7_5.delete(ALL)
    buffer_7_6.delete(ALL)
    buffer_7_7.delete(ALL)
    buffer_7_8.delete(ALL)

    buffer_8_4.delete(ALL)
    buffer_8_5.delete(ALL)
    buffer_8_6.delete(ALL)
    buffer_8_7.delete(ALL)
    buffer_8_8.delete(ALL)

    buffer_9_4.delete(ALL)
    buffer_9_5.delete(ALL)
    buffer_9_6.delete(ALL)
    buffer_9_7.delete(ALL)
    buffer_9_8.delete(ALL)

    buffer_10_4.delete(ALL)
    buffer_10_5.delete(ALL)
    buffer_10_6.delete(ALL)
    buffer_10_7.delete(ALL)
    buffer_10_8.delete(ALL)


opros = 1600

f = open("text.txt", 'w')
f.close()
j = 0


def scale(canvas):
    for c in range(4):
        canvas.create_line(0, 10+c*10, 3, 10+c*10, width=2)
    for c in range(27):
        canvas.create_line(10+c*10, 50, 10+c*10, 48, width=2)
    for c in range(4):
        canvas.create_line(0, 10+c*10, 280, 10+c*10, fill="gray82", width=1)
    for c in range(27):
        canvas.create_line(10+c*10, 0, 10+c*10, 50, fill="gray82", width=1)
    for c in range(5):
        canvas.create_line(0+c*56, 0, 0+c*56, 50, fill="gray55", width=1)


def delete_graph():
    graph_1.delete(ALL)
    graph_2.delete(ALL)
    graph_3.delete(ALL)
    graph_4.delete(ALL)
    graph_5.delete(ALL)



scale(graph_1)
graph_1.create_line(0, 50, 280, 50, width=1)
graph_1.create_line(1, 0, 1, 50, width=3)
graph_1.create_line(0, 40, 280, 40, width=1.5, fill="yellow")
graph_1.create_line(0, 45, 280, 45, width=1.5, fill="red")
scale(graph_2)
graph_2.create_line(0, 25, 280, 25, width=1)
graph_2.create_line(0, 50, 280, 50, width=1)
graph_2.create_line(1, 0, 1, 50, width=3)
graph_2.create_line(0, 10, 280, 10, width=1.5, fill="yellow")
graph_2.create_line(0, 5, 280, 5, width=1.5, fill="red")
graph_2.create_line(0, 40, 280, 40, width=1.5, fill="yellow")
graph_2.create_line(0, 45, 280, 45, width=1.5, fill="red")
scale(graph_3)
graph_3.create_line(0, 50, 280, 50, width=1)
graph_3.create_line(1, 0, 1, 50, width=3)
graph_3.create_line(0, 30, 280, 30, width=1.5, fill="yellow")
graph_3.create_line(0, 45, 280, 45, width=1.5, fill="red")
scale(graph_4)
graph_4.create_line(0, 50, 280, 50, width=1)
graph_4.create_line(1, 0, 1, 50, width=3)
graph_4.create_line(0, 15, 280, 15, width=1.5, fill="red")
scale(graph_5)
graph_5.create_line(0, 40, 280, 40, width=1)
graph_5.create_line(0, 50, 280, 50, width=1)
graph_5.create_line(1, 0, 1, 50, width=3)
graph_5.create_line(0, 15, 280, 15, width=1.5, fill="yellow")
graph_5.create_line(0, 5, 280, 5, width=1.5, fill="red")
# stanok-kachalka
z=0
photo = [PhotoImage(file='stanok-kachalka.gif', format = 'gif -index %i' %(i)) for i in range(17)]
label_gachi = Label(root, image = photo[z])
label_gachi.place(relx=0.01, rely=0.6)



svyas = [PhotoImage(file='copy-gif-3.gif', format = 'gif -index %i' %(i)) for i in range(20)]
nosvyas = PhotoImage(file='11b33e3daad1.png')
label_smeert = Label(root, image = svyas[0])
label_smeert.place(relx=0.5, rely=0.5, anchor="center")




schet = 0
timetable = [0, 0, 0, 0, 0]

def terminal():
    global signal, close, opros, photo, label_gachi, solve, kostil_list
    global i, z
    global buffer_1_4, buffer_1_5, buffer_1_6, buffer_1_7, buffer_1_8
    global buffer_2_4, buffer_2_5, buffer_2_6, buffer_2_7, buffer_3_8
    global buffer_3_4, buffer_3_5, buffer_3_6, buffer_3_7, buffer_3_8
    global buffer_4_4, buffer_4_5, buffer_4_6, buffer_4_7, buffer_4_8
    global buffer_5_4, buffer_5_5, buffer_5_6, buffer_5_7, buffer_5_8
    global buffer_6_4, buffer_6_5, buffer_6_6, buffer_6_7, buffer_6_8
    global buffer_7_4, buffer_7_5, buffer_7_6, buffer_7_7, buffer_7_8
    global buffer_8_4, buffer_8_5, buffer_8_6, buffer_8_7, buffer_8_8
    global buffer_9_4, buffer_9_5, buffer_9_6, buffer_9_7, buffer_9_8
    global buffer_10_4, buffer_10_5, buffer_10_6, buffer_10_7, buffer_10_8
    global zn_dat_1, zn_dat_2, zn_dat_3, zn_dat_4, zn_dat_5
    global list1, buf, now, graph, j, sost, timetable, schet
    close = 0
    # Генератор чиселок
    list1 = [random.randint(0, 50), random.randint(-50, 50), round(random.uniform(1, 17), 3),
             random.randint(0, 1), round(random.uniform(-20, 80), 2)]

    tim.delete(ALL)
    tim.create_text(25, 10, text=str(opros/1000) + " c", font="Verdana 8", justify="center")

    if (schet < 5):
        timetable[schet] = now.strftime("%M:%S")
        schet = schet + 1
    else:
        timetable[0] = timetable[1][:]
        timetable[1] = timetable[2][:]
        timetable[2] = timetable[3][:]
        timetable[3] = timetable[4][:]
        timetable[4] = now.strftime("%M:%S")

    # time_bar_1_0.delete(ALL)
    # time_bar_2_0.delete(ALL)
    # time_bar_3_0.delete(ALL)
    # time_bar_4_0.delete(ALL)
    # time_bar_5_0.delete(ALL)
    #
    # time_bar_1_1.delete(ALL)
    # time_bar_2_1.delete(ALL)
    # time_bar_3_1.delete(ALL)
    # time_bar_4_1.delete(ALL)
    # time_bar_5_1.delete(ALL)
    #
    # time_bar_1_2.delete(ALL)
    # time_bar_2_2.delete(ALL)
    # time_bar_3_2.delete(ALL)
    # time_bar_4_2.delete(ALL)
    # time_bar_5_2.delete(ALL)
    #
    # time_bar_1_3.delete(ALL)
    # time_bar_2_3.delete(ALL)
    # time_bar_3_3.delete(ALL)
    # time_bar_4_3.delete(ALL)
    # time_bar_5_3.delete(ALL)
    #
    # time_bar_1_4.delete(ALL)
    # time_bar_2_4.delete(ALL)
    # time_bar_3_4.delete(ALL)
    # time_bar_4_4.delete(ALL)
    # time_bar_5_4.delete(ALL)

    time_bar_1_0.configure(text=timetable[0])
    time_bar_2_0.configure(text=timetable[0])
    time_bar_3_0.configure(text=timetable[0])
    time_bar_4_0.configure(text=timetable[0])
    time_bar_5_0.configure(text=timetable[0])

    time_bar_1_1.configure(text=timetable[1])
    time_bar_2_1.configure(text=timetable[1])
    time_bar_3_1.configure(text=timetable[1])
    time_bar_4_1.configure(text=timetable[1])
    time_bar_5_1.configure(text=timetable[1])

    time_bar_1_2.configure(text=timetable[2])
    time_bar_2_2.configure(text=timetable[2])
    time_bar_3_2.configure(text=timetable[2])
    time_bar_4_2.configure(text=timetable[2])
    time_bar_5_2.configure(text=timetable[2])

    time_bar_1_3.configure(text=timetable[3])
    time_bar_2_3.configure(text=timetable[3])
    time_bar_3_3.configure(text=timetable[3])
    time_bar_4_3.configure(text=timetable[3])
    time_bar_5_3.configure(text=timetable[3])

    time_bar_1_4.configure(text=timetable[4])
    time_bar_2_4.configure(text=timetable[4])
    time_bar_3_4.configure(text=timetable[4])
    time_bar_4_4.configure(text=timetable[4])
    time_bar_5_4.configure(text=timetable[4])


    root.after(0, lambda: label_gachi.configure(image=photo[0]))
    root.after(1*int(opros/17), lambda: label_gachi.configure(image=photo[1]))
    root.after(2*int(opros/17), lambda: label_gachi.configure(image=photo[2]))
    root.after(3*int(opros/17), lambda: label_gachi.configure(image=photo[3]))
    root.after(4*int(opros/17), lambda: label_gachi.configure(image=photo[4]))
    root.after(5*int(opros/17), lambda: label_gachi.configure(image=photo[5]))
    root.after(6*int(opros/17), lambda: label_gachi.configure(image=photo[6]))
    root.after(7*int(opros/17), lambda: label_gachi.configure(image=photo[7]))
    root.after(8*int(opros/17), lambda: label_gachi.configure(image=photo[8]))
    root.after(9*int(opros/17), lambda: label_gachi.configure(image=photo[9]))
    root.after(10*int(opros/17), lambda: label_gachi.configure(image=photo[10]))
    root.after(11*int(opros/17), lambda: label_gachi.configure(image=photo[11]))
    root.after(12*int(opros/17), lambda: label_gachi.configure(image=photo[12]))
    root.after(13*int(opros/17), lambda: label_gachi.configure(image=photo[13]))
    root.after(14*int(opros/17), lambda: label_gachi.configure(image=photo[14]))
    root.after(15*int(opros/17), lambda: label_gachi.configure(image=photo[15]))
    root.after(16*int(opros/17), lambda: label_gachi.configure(image=photo[16]))
    # root.after(17*int(opros/17), lambda: label_gachi.configure(image=photo[17]))
    # root.after(209, lambda: label_gachi.configure(image=photo[18]))
    # root.after(220, lambda: label_gachi.configure(image=photo[19]))
    # root.after(231, lambda: label_gachi.configure(image=photo[20]))
    # root.after(242, lambda: label_gachi.configure(image=photo[21]))
    # root.after(253, lambda: label_gachi.configure(image=photo[22]))
    # root.after(264, lambda: label_gachi.configure(image=photo[23]))
    # root.after(275, lambda: label_gachi.configure(image=photo[24]))
    # root.after(286, lambda: label_gachi.configure(image=photo[25]))
    # root.after(297, lambda: label_gachi.configure(image=photo[26]))
    # root.after(308, lambda: label_gachi.configure(image=photo[27]))
    # root.after(319, lambda: label_gachi.configure(image=photo[28]))
    # root.after(330, lambda: label_gachi.configure(image=photo[29]))
    # root.after(341, lambda: label_gachi.configure(image=photo[30]))
    # root.after(352, lambda: label_gachi.configure(image=photo[31]))
    # root.after(363, lambda: label_gachi.configure(image=photo[32]))
    # root.after(374, lambda: label_gachi.configure(image=photo[33]))
    # root.after(385, lambda: label_gachi.configure(image=photo[34]))
    # root.after(396, lambda: label_gachi.configure(image=photo[35]))
    # root.after(407, lambda: label_gachi.configure(image=photo[36]))
    # root.after(418, lambda: label_gachi.configure(image=photo[37]))
    # root.after(429, lambda: label_gachi.configure(image=photo[38]))
    # root.after(440, lambda: label_gachi.configure(image=photo[39]))
    # root.after(451, lambda: label_gachi.configure(image=photo[40]))
    # root.after(462, lambda: label_gachi.configure(image=photo[41]))
    # root.after(473, lambda: label_gachi.configure(image=photo[42]))
    # root.after(484, lambda: label_gachi.configure(image=photo[43]))
    # root.after(495, lambda: label_gachi.configure(image=photo[44]))
    # root.after(506, lambda: label_gachi.configure(image=photo[45]))
    # root.after(517, lambda: label_gachi.configure(image=photo[46]))
    # root.after(528, lambda: label_gachi.configure(image=photo[47]))
    # root.after(539, lambda: label_gachi.configure(image=photo[48]))
    # root.after(550, lambda: label_gachi.configure(image=photo[49]))
    # root.after(561, lambda: label_gachi.configure(image=photo[50]))
    # root.after(572, lambda: label_gachi.configure(image=photo[51]))
    # root.after(583, lambda: label_gachi.configure(image=photo[52]))
    # root.after(594, lambda: label_gachi.configure(image=photo[53]))
    # root.after(605, lambda: label_gachi.configure(image=photo[54]))
    # root.after(616, lambda: label_gachi.configure(image=photo[55]))
    # root.after(627, lambda: label_gachi.configure(image=photo[56]))
    # root.after(638, lambda: label_gachi.configure(image=photo[57]))
    # root.after(649, lambda: label_gachi.configure(image=photo[58]))
    # root.after(660, lambda: label_gachi.configure(image=photo[59]))
    # root.after(671, lambda: label_gachi.configure(image=photo[60]))
    # root.after(682, lambda: label_gachi.configure(image=photo[61]))
    # root.after(693, lambda: label_gachi.configure(image=photo[62]))
    # root.after(704, lambda: label_gachi.configure(image=photo[63]))
    # root.after(715, lambda: label_gachi.configure(image=photo[64]))
    # root.after(726, lambda: label_gachi.configure(image=photo[65]))
    # root.after(737, lambda: label_gachi.configure(image=photo[66]))
    # root.after(748, lambda: label_gachi.configure(image=photo[67]))
    # root.after(759, lambda: label_gachi.configure(image=photo[68]))


    # if z < 15:
    #     photochka = photo[z]
    #     z += 1
    #     label_gachi.configure(image=photochka)
    # else:
    #     z=0
    #     photochka = photo[z]
    #     z += 1
    #     label_gachi.configure(image=photochka)


    if j < 5:
        graph[j] = list1
        print(list1)
        print(graph)
        delete_graph()
        scale(graph_1)
        graph_1.create_line(0, 50, 280, 50, width=1)
        graph_1.create_line(1, 0, 1, 50, width=3)
        graph_1.create_line(0, 40, 280, 40, width=1.5, fill="yellow")
        graph_1.create_line(0, 45, 280, 45, width=1.5, fill="red")
        scale(graph_2)
        graph_2.create_line(0, 25, 280, 25, width=1)
        graph_2.create_line(0, 50, 280, 50, width=1)
        graph_2.create_line(1, 0, 1, 50, width=3)
        graph_2.create_line(0, 10, 280, 10, width=1.5, fill="yellow")
        graph_2.create_line(0, 5, 280, 5, width=1.5, fill="red")
        graph_2.create_line(0, 40, 280, 40, width=1.5, fill="yellow")
        graph_2.create_line(0, 45, 280, 45, width=1.5, fill="red")
        scale(graph_3)
        graph_3.create_line(0, 50, 280, 50, width=1)
        graph_3.create_line(1, 0, 1, 50, width=3)
        graph_3.create_line(0, 30, 280, 30, width=1.5, fill="yellow")
        graph_3.create_line(0, 45, 280, 45, width=1.5, fill="red")
        scale(graph_4)
        graph_4.create_line(0, 50, 280, 50, width=1)
        graph_4.create_line(1, 0, 1, 50, width=3)
        graph_4.create_line(0, 15, 280, 15, width=1.5, fill="red")
        scale(graph_5)
        graph_5.create_line(0, 40, 280, 40, width=1)
        graph_5.create_line(0, 50, 280, 50, width=1)
        graph_5.create_line(1, 0, 1, 50, width=3)
        graph_5.create_line(0, 15, 280, 15, width=1.5, fill="yellow")
        graph_5.create_line(0, 5, 280, 5, width=1.5, fill="red")

        if j == 0:
            graph_1.create_line(0, (50-graph[0][0])*0.9, 8, (50-graph[0][0])*0.9, width=2)
            graph_2.create_line(0, (50-(graph[0][1]*0.45+25)), 8, (50-(graph[0][1]*0.45+25)), width=2)
            graph_3.create_line(0, 50-(graph[0][2]*2), 8, 50-(graph[0][2]*2), width=2)
            graph_4.create_line(0, 50-(graph[0][3]*25+10), 8, 50-(graph[0][3]*25+10), width=2)
            graph_5.create_line(0, 50-(graph[0][4]*0.45+10), 8, 50-(graph[0][4]*0.45+10), width=2)

        if j == 1:
            graph_1.create_line(0, (50 - graph[0][0]) * 0.9, 56, (50 - graph[1][0]) * 0.9, width=2)
            graph_2.create_line(0, (50 - (graph[0][1] * 0.45 + 25)), 56, (50 - (graph[1][1] * 0.45 + 25)), width=2)
            graph_3.create_line(0, 50 - (graph[0][2] * 2), 56, 50 - (graph[0][2] * 2), width=2)
            graph_4.create_line(0, 50 - (graph[0][3] * 25 + 10), 56, 50 - (graph[1][3] * 25 + 10), width=2)
            graph_5.create_line(0, 50 - (graph[0][4] * 0.45 + 10), 56, 50 - (graph[1][4] * 0.45 + 10), width=2)
        if j == 2:
            graph_1.create_line(0, (50 - graph[0][0]) * 0.9,         56, (50 - graph[1][0]) * 0.9, width=2)
            graph_2.create_line(0, (50 - (graph[0][1] * 0.45 + 25)), 56, (50 - (graph[1][1] * 0.45 + 25)), width=2)
            graph_3.create_line(0, 50 - (graph[0][2] * 2),           56, 50 - (graph[1][2] * 2), width=2)
            graph_4.create_line(0, 50 - (graph[0][3] * 25 + 10),     56, 50 - (graph[1][3] * 25 + 10), width=2)
            graph_5.create_line(0, 50 - (graph[0][4] * 0.45 + 10),   56, 50 - (graph[1][4] * 0.45 + 10), width=2)

            graph_1.create_line(56, (50 - graph[1][0]) * 0.9,           56+56, (50 - graph[2][0]) * 0.9, width=2)
            graph_2.create_line(56, (50 - (graph[1][1] * 0.45 + 25)),    56+56, (50 - (graph[2][1] * 0.45 + 25)), width=2)
            graph_3.create_line(56, 50 - (graph[1][2] * 2),              56+56, 50 - (graph[2][2] * 2), width=2)
            graph_4.create_line(56, 50 - (graph[1][3] * 25 + 10),        56+56, 50 - (graph[2][3] * 25 + 10), width=2)
            graph_5.create_line(56, 50 - (graph[1][4] * 0.45 + 10),      56+56, 50 - (graph[2][4] * 0.45 + 10), width=2)
        if j == 3:
            graph_1.create_line(0, (50 - graph[0][0]) * 0.9, 56, (50 - graph[1][0]) * 0.9, width=2)
            graph_2.create_line(0, (50 - (graph[0][1] * 0.45 + 25)), 56, (50 - (graph[1][1] * 0.45 + 25)), width=2)
            graph_3.create_line(0, 50 - (graph[0][2] * 2), 56, 50 - (graph[1][2] * 2), width=2)
            graph_4.create_line(0, 50 - (graph[0][3] * 25 + 10), 56, 50 - (graph[1][3] * 25 + 10), width=2)
            graph_5.create_line(0, 50 - (graph[0][4] * 0.45 + 10), 56, 50 - (graph[1][4] * 0.45 + 10), width=2)

            graph_1.create_line(56, (50 - graph[1][0]) * 0.9, 56 + 56, (50 - graph[2][0]) * 0.9, width=2)
            graph_2.create_line(56, (50 - (graph[1][1] * 0.45 + 25)), 56 + 56, (50 - (graph[2][1] * 0.45 + 25)), width=2)
            graph_3.create_line(56, 50 - ((graph[1][2]) * 2), 56 + 56, 50 - ((graph[2][2]) * 2), width=2)
            graph_4.create_line(56, 50 - (graph[1][3] * 25 + 10), 56 + 56, 50 - (graph[2][3] * 25 + 10), width=2)
            graph_5.create_line(56, 50 - (graph[1][4] * 0.45 + 10), 56 + 56, 50 - (graph[2][4] * 0.45 + 10), width=2)

            graph_1.create_line(56+56, (50 - graph[2][0]) * 0.9,            56 + 56+56, (50 - graph[3][0]) * 0.9, width=2)
            graph_2.create_line(56+56, (50 - (graph[2][1] * 0.45 + 25)),    56 + 56+56, (50 - (graph[3][1] * 0.45 + 25)), width=2)
            graph_3.create_line(56+56, 50 - ((graph[2][2]) * 2),              56 + 56+56, 50 - ((graph[3][2]) * 2), width=2)
            graph_4.create_line(56+56, 50 - (graph[2][3] * 25 + 10),        56 + 56+56, 50 - (graph[3][3] * 25 + 10), width=2)
            graph_5.create_line(56+56, 50 - (graph[2][4] * 0.45 + 10),      56 + 56+56, 50 - (graph[3][4] * 0.45 + 10), width=2)
        if j == 4:
            graph_1.create_line(0, (50 - graph[0][0]) * 0.9,                56, (50 - graph[1][0]) * 0.9, width=2)
            graph_2.create_line(0, (50 - (graph[0][1] * 0.45 + 25)),        56, (50 - (graph[1][1] * 0.45 + 25)), width=2)
            graph_3.create_line(0, 50 - (graph[0][2] * 2),                  56, 50 - (graph[1][2] * 2), width=2)
            graph_4.create_line(0, 50 - (graph[0][3] * 25 + 10),            56, 50 - (graph[1][3] * 25 + 10), width=2)
            graph_5.create_line(0, 50 - (graph[0][4] * 0.45 + 10),          56, 50 - (graph[1][4] * 0.45 + 10), width=2)

            graph_1.create_line(56, (50 - graph[1][0]) * 0.9,               56 + 56, (50 - graph[2][0]) * 0.9, width=2)
            graph_2.create_line(56, (50 - (graph[1][1] * 0.45 + 25)),       56 + 56, (50 - (graph[2][1] * 0.45 + 25)), width=2)
            graph_3.create_line(56, 50 - ((graph[1][2]) * 2),                 56 + 56, 50 - ((graph[2][2]) * 2), width=2)
            graph_4.create_line(56, 50 - (graph[1][3] * 25 + 10),           56 + 56, 50 - (graph[2][3] * 25 + 10), width=2)
            graph_5.create_line(56, 50 - (graph[1][4] * 0.45 + 10),         56 + 56, 50 - (graph[2][4] * 0.45 + 10), width=2)

            graph_1.create_line(56 + 56, (50 - graph[2][0]) * 0.9,              56 + 56 + 56, (50 - graph[3][0]) * 0.9, width=2)
            graph_2.create_line(56 + 56, (50 - (graph[2][1] * 0.45 + 25)),      56 + 56 + 56, (50 - (graph[3][1] * 0.45 + 25)), width=2)
            graph_3.create_line(56 + 56, 50 - ((graph[2][2]) * 2),                56 + 56 + 56, 50 - (graph[3][2] * 2), width=2)
            graph_4.create_line(56 + 56, 50 - (graph[2][3] * 25 + 10),          56 + 56 + 56, 50 - (graph[3][3] * 25 + 10), width=2)
            graph_5.create_line(56 + 56, 50 - (graph[2][4] * 0.45 + 10),        56 + 56 + 56, 50 - (graph[3][4] * 0.45 + 10), width=2)

            graph_1.create_line(56 + 56+56, (50 - graph[3][0]) * 0.9,           56 + 56 + 56+56, (50 - graph[4][0]) * 0.9, width=2)
            graph_2.create_line(56 + 56+56, (50 - (graph[3][1] * 0.45 + 25)),   56 + 56 + 56+56, (50 - (graph[4][1] * 0.45 + 25)), width=2)
            graph_3.create_line(56 + 56+56, 50 - (graph[3][2] * 2),             56 + 56 + 56+56, 50 - (graph[4][2] * 2), width=2)
            graph_4.create_line(56 + 56+56, 50 - (graph[3][3] * 25 + 10),       56 + 56 + 56+56, 50 - (graph[4][3] * 25 + 10), width=2)
            graph_5.create_line(56 + 56+56, 50 - (graph[3][4] * 0.45 + 10),     56 + 56 + 56+56, 50 - (graph[4][4] * 0.45 + 10), width=2)
        j = j + 1
    else:
        graph[0] = graph[1]
        graph[1] = graph[2]
        graph[2] = graph[3]
        graph[3] = graph[4]
        graph[4] = list1

        delete_graph()
        scale(graph_1)
        graph_1.create_line(0, 50, 280, 50, width=1)
        graph_1.create_line(1, 0, 1, 50, width=3)
        graph_1.create_line(0, 40, 280, 40, width=1.5, fill="yellow")
        graph_1.create_line(0, 45, 280, 45, width=1.5, fill="red")
        scale(graph_2)
        graph_2.create_line(0, 25, 280, 25, width=1)
        graph_2.create_line(0, 50, 280, 50, width=1)
        graph_2.create_line(1, 0, 1, 50, width=3)
        graph_2.create_line(0, 10, 280, 10, width=1.5, fill="yellow")
        graph_2.create_line(0, 5, 280, 5, width=1.5, fill="red")
        graph_2.create_line(0, 40, 280, 40, width=1.5, fill="yellow")
        graph_2.create_line(0, 45, 280, 45, width=1.5, fill="red")
        scale(graph_3)
        graph_3.create_line(0, 50, 280, 50, width=1)
        graph_3.create_line(1, 0, 1, 50, width=3)
        graph_3.create_line(0, 30, 280, 30, width=1.5, fill="yellow")
        graph_3.create_line(0, 45, 280, 45, width=1.5, fill="red")
        scale(graph_4)
        graph_4.create_line(0, 50, 280, 50, width=1)
        graph_4.create_line(1, 0, 1, 50, width=3)
        graph_4.create_line(0, 15, 280, 15, width=1.5, fill="red")
        scale(graph_5)
        graph_5.create_line(0, 40, 280, 40, width=1)
        graph_5.create_line(0, 50, 280, 50, width=1)
        graph_5.create_line(1, 0, 1, 50, width=3)
        graph_5.create_line(0, 15, 280, 15, width=1.5, fill="yellow")
        graph_5.create_line(0, 5, 280, 5, width=1.5, fill="red")

        graph_1.create_line(0, (50 - graph[0][0]) * 0.9, 56, (50 - graph[1][0]) * 0.9, width=2)
        graph_2.create_line(0, (50 - (graph[0][1] * 0.45 + 25)), 56, (50 - (graph[1][1] * 0.45 + 25)), width=2)
        graph_3.create_line(0, 50 - ((graph[0][2]) * 2), 56, 50 - ((graph[1][2]) * 2), width=2)
        graph_4.create_line(0, 50 - (graph[0][3] * 25 + 10), 56, 50 - (graph[1][3] * 25 + 10), width=2)
        graph_5.create_line(0, 50 - (graph[0][4] * 0.45 + 10), 56, 50 - (graph[1][4] * 0.45 + 10), width=2)

        graph_1.create_line(56, (50 - graph[1][0]) * 0.9, 56 + 56, (50 - graph[2][0]) * 0.9, width=2)
        graph_2.create_line(56, (50 - (graph[1][1] * 0.45 + 25)), 56 + 56, (50 - (graph[2][1] * 0.45 + 25)), width=2)
        graph_3.create_line(56, 50 - ((graph[1][2]) * 2), 56 + 56, 50 - ((graph[2][2]) * 2), width=2)
        graph_4.create_line(56, 50 - (graph[1][3] * 25 + 10), 56 + 56, 50 - (graph[2][3] * 25 + 10), width=2)
        graph_5.create_line(56, 50 - (graph[1][4] * 0.45 + 10), 56 + 56, 50 - (graph[2][4] * 0.45 + 10), width=2)

        graph_1.create_line(56 + 56, (50 - graph[2][0]) * 0.9, 56 + 56 + 56, (50 - graph[3][0]) * 0.9, width=2)
        graph_2.create_line(56 + 56, (50 - (graph[2][1] * 0.45 + 25)), 56 + 56 + 56, (50 - (graph[3][1] * 0.45 + 25)),
                            width=2)
        graph_3.create_line(56 + 56, 50 - ((graph[2][2]) * 2), 56 + 56 + 56, 50 - ((graph[3][2]) * 2), width=2)
        graph_4.create_line(56 + 56, 50 - (graph[2][3] * 25 + 10), 56 + 56 + 56, 50 - (graph[3][3] * 25 + 10), width=2)
        graph_5.create_line(56 + 56, 50 - (graph[2][4] * 0.45 + 10), 56 + 56 + 56, 50 - (graph[3][4] * 0.45 + 10),
                            width=2)

        graph_1.create_line(56 + 56 + 56, (50 - graph[3][0]) * 0.9, 56 + 56 + 56 + 56, (50 - graph[4][0]) * 0.9,
                            width=2)
        graph_2.create_line(56 + 56 + 56, (50 - (graph[3][1] * 0.45 + 25)), 56 + 56 + 56 + 56,
                            (50 - (graph[4][1] * 0.45 + 25)), width=2)
        graph_3.create_line(56 + 56 + 56, 50 - ((graph[3][2]) * 2), 56 + 56 + 56 + 56, 50 - ((graph[4][2]) * 2), width=2)
        graph_4.create_line(56 + 56 + 56, 50 - (graph[3][3] * 25 + 10), 56 + 56 + 56 + 56, 50 - (graph[4][3] * 25 + 10),
                            width=2)
        graph_5.create_line(56 + 56 + 56, 50 - (graph[3][4] * 0.45 + 10), 56 + 56 + 56 + 56,
                            50 - (graph[4][4] * 0.45 + 10), width=2)
    # print(graph)
    # print(list1)
    now = NONE
    now = datetime.datetime.now()
    chance = random.random()
    # Конец генератора
    f = open('text.txt', 'a')
    zn_dat_1.delete(ALL)
    zn_dat_2.delete(ALL)
    zn_dat_3.delete(ALL)
    zn_dat_4.delete(ALL)
    zn_dat_5.delete(ALL)
    zn_dat_1.configure(bg="ghost white")
    zn_dat_2.configure(bg="ghost white")
    zn_dat_3.configure(bg="ghost white")
    zn_dat_4.configure(bg="ghost white")
    zn_dat_5.configure(bg="ghost white")

    zn_dat_1.create_text(20, 12.5, text=list1[0], font="Verdana 8", justify="center")
    if list1[0] < 10:
        zn_dat_1.configure(bg="yellow")
    if list1[0] < 5:
        zn_dat_1.configure(bg="red")

    zn_dat_2.create_text(20, 12.5, text=list1[1], font="Verdana 8", justify="center")
    if ((list1[1] < -40) or (list1[1] > 40)):
        zn_dat_2.configure(bg="yellow")
    if ((list1[1] < -45) or (list1[1] > 45)):
        zn_dat_2.configure(bg="red")

    zn_dat_3.create_text(20, 12.5, text=list1[2], font="Verdana 8", justify="center")
    if list1[2] < 6:
        zn_dat_3.configure(bg="yellow")
    if list1[2] < 3:
        zn_dat_3.configure(bg="red")

    zn_dat_4.create_text(20, 12.5, text=list1[3], font="Verdana 8", justify="center")
    if list1[3] == 1:
        zn_dat_4.configure(bg="red")

    zn_dat_5.create_text(20, 12.5, text=list1[4], font="Verdana 8", justify="center")
    if list1[4] > 70:
        zn_dat_5.configure(bg="yellow")
    if list1[4] > 79:
        zn_dat_5.configure(bg="red")
    # print(now)
    if chance < 0.8 and signal == 1:
        root.after(0, lambda: label_smeert.configure(image=svyas[0]))
        root.after(1 * int(opros / 20), lambda: label_smeert.configure(image=svyas[1]))
        root.after(2 * int(opros / 20), lambda: label_smeert.configure(image=svyas[2]))
        root.after(3 * int(opros / 20), lambda: label_smeert.configure(image=svyas[3]))
        root.after(4 * int(opros / 20), lambda: label_smeert.configure(image=svyas[4]))
        root.after(5 * int(opros / 20), lambda: label_smeert.configure(image=svyas[5]))
        root.after(6 * int(opros / 20), lambda: label_smeert.configure(image=svyas[6]))
        root.after(7 * int(opros / 20), lambda: label_smeert.configure(image=svyas[7]))
        root.after(8 * int(opros / 20), lambda: label_smeert.configure(image=svyas[8]))
        root.after(9 * int(opros / 20), lambda: label_smeert.configure(image=svyas[9]))
        root.after(10 * int(opros / 20), lambda: label_smeert.configure(image=svyas[10]))
        root.after(11 * int(opros / 20), lambda: label_smeert.configure(image=svyas[11]))
        root.after(12 * int(opros / 20), lambda: label_smeert.configure(image=svyas[12]))
        root.after(13 * int(opros / 20), lambda: label_smeert.configure(image=svyas[13]))
        root.after(14 * int(opros / 20), lambda: label_smeert.configure(image=svyas[14]))
        root.after(15 * int(opros / 20), lambda: label_smeert.configure(image=svyas[15]))
        root.after(16 * int(opros / 20), lambda: label_smeert.configure(image=svyas[16]))
        root.after(17 * int(opros / 20), lambda: label_smeert.configure(image=svyas[17]))
        root.after(18 * int(opros / 20), lambda: label_smeert.configure(image=svyas[18]))
        root.after(19 * int(opros / 20), lambda: label_smeert.configure(image=svyas[19]))

        if i > 0:

            sost.delete(ALL)
            sost.configure(bg="yellow")
            sost.create_text(100, 10, text="Восстанавливаем связь", font="Verdana 8", justify="center")

            root.after(1 * int(opros/4), lambda: sost.delete(ALL))
            root.after(1 * int(opros/4), lambda: sost.configure(bg="yellow"))
            root.after(1 * int(opros/4), lambda: sost.create_text(100, 10, text="Обновляем время опроса", font="Verdana 8", justify="center"))

            root.after(2 * int(opros/4), lambda: sost.delete(ALL))
            root.after(2 * int(opros/4), lambda: sost.configure(bg="green"))
            root.after(2 * int(opros/4), lambda: sost.create_text(100, 10, text="Переносим данные из буфера", font="Verdana 8", justify="center"))

            root.after(3 * int(opros/4), lambda: sost.delete(ALL))
            root.after(3 * int(opros/4), lambda: sost.configure(bg="green"))
            root.after(3 * int(opros/4), lambda: sost.create_text(100, 10, text="Нормальная работа", font="Verdana 8", justify="center"))


            for numb in range(i):
                f.write(str(buf[numb]) + "\n")
                # Костыли для уставных значений
                kostil_list = buf[numb][:]
                if kostil_list[0] < 5:
                    box = open('textbox.txt', 'w')
                    kostil_list[0] = NONE
                    kostil_list[0] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Первый датчик достиг АВАРИЙНОГО значения" + "\n"
                    box.write(str(kostil_list[0]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()

                elif kostil_list[0] < 10:
                    box = open('textbox.txt', 'w')
                    kostil_list[0] = NONE
                    kostil_list[0] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Первый датчик достиг предаварийного значения" + "\n"
                    box.write(str(kostil_list[0]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()

                if kostil_list[1] > 45 or kostil_list[1] < -45:
                    box = open('textbox.txt', 'w')
                    kostil_list[1] = NONE
                    kostil_list[1] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Второй датчик достиг АВАРИЙНОГО значения" + "\n"
                    box.write(str(kostil_list[1]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()
                elif kostil_list[1] > 40 or kostil_list[1] < -40:
                    box = open('textbox.txt', 'w')
                    kostil_list[1] = NONE
                    kostil_list[1] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Второй датчик достиг предаварийного значения" + "\n"
                    box.write(str(kostil_list[1]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()

                if kostil_list[2] < 3:
                    box = open('textbox.txt', 'w')
                    kostil_list[2] = NONE
                    kostil_list[2] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Третий датчик достиг АВАРИЙНОГО значения" + "\n"
                    box.write(str(kostil_list[2]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()
                elif kostil_list[2] < 6:
                    box = open('textbox.txt', 'w')
                    kostil_list[2] = NONE
                    kostil_list[2] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Третий датчик достиг предаварийного значения" + "\n"
                    box.write(str(kostil_list[2]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()

                if kostil_list[3] == 1:
                    box = open('textbox.txt', 'w')
                    kostil_list[3] = NONE
                    kostil_list[3] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Четвертый датчик достиг АВАРИЙНОГО значения" + "\n"
                    box.write(str(kostil_list[3]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()

                if kostil_list[4] > 79:
                    box = open('textbox.txt', 'w')
                    kostil_list[4] = NONE
                    kostil_list[4] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Пятый датчик достиг АВАРИЙНОГО значения" + "\n"
                    box.write(str(kostil_list[4]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()
                elif kostil_list[4] > 70:
                    box = open('textbox.txt', 'w')
                    kostil_list[4] = NONE
                    kostil_list[4] = str(
                        now.strftime("%d-%m-%Y %H:%M:%S")) + " Пятый датчик достиг предаварийного значения" + "\n"
                    box.write(str(kostil_list[4]) + "\n")
                    box.close()
                    box = open('textbox.txt', 'r')
                    hude_text = box.read()
                    ceh.insert(1.0, hude_text)
                    box.close()
                kostil_list = NONE
            f.write(str(list1) + "\n")
            kostil_list = list1[:]
            if kostil_list[0] < 5:
                box = open('textbox.txt', 'w')
                kostil_list[0] = NONE
                kostil_list[0] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Первый датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[0]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            elif kostil_list[0] < 10:
                box = open('textbox.txt', 'w')
                kostil_list[0] = NONE
                kostil_list[0] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Первый датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[0]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[1] > 45 or kostil_list[1] < -45:
                box = open('textbox.txt', 'w')
                kostil_list[1] = NONE
                kostil_list[1] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Второй датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[1]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            elif kostil_list[1] > 40 or kostil_list[1] < -40:
                box = open('textbox.txt', 'w')
                kostil_list[1] = NONE
                kostil_list[1] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Второй датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[1]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[2] < 3:
                box = open('textbox.txt', 'w')
                kostil_list[2] = NONE
                kostil_list[2] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Третий датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[2]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            elif kostil_list[2] < 6:
                box = open('textbox.txt', 'w')
                kostil_list[2] = NONE
                kostil_list[2] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Третий датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[2]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[3] == 1:
                box = open('textbox.txt', 'w')
                kostil_list[3] = NONE
                kostil_list[3] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Четвертый датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[3]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[4] > 79:
                box = open('textbox.txt', 'w')
                kostil_list[4] = NONE
                kostil_list[4] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Пятый датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[4]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            elif kostil_list[4] > 70:
                box = open('textbox.txt', 'w')
                kostil_list[4] = NONE
                kostil_list[4] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Пятый датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[4]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            kostil_list = NONE
            delete_buff()
            i = 0
        else:

            sost.delete(ALL)
            sost.configure(bg="green")
            sost.create_text(100, 10, text="Нормальная работа", font="Verdana 8", justify="center")

            f.write(str(list1) + "\n")
            kostil_list = list1[:]
            if kostil_list[0] < 5:
                box = open('textbox.txt', 'w')
                kostil_list[0] = NONE
                kostil_list[0] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Первый датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[0]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            elif kostil_list[0] < 10:
                box = open('textbox.txt', 'w')
                kostil_list[0] = NONE
                kostil_list[0] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Первый датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[0]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[1] > 45 or kostil_list[1] < -45:
                box = open('textbox.txt', 'w')
                kostil_list[1] = NONE
                kostil_list[1] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Второй датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[1]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            elif kostil_list[1] > 40 or kostil_list[1] < -40:
                box = open('textbox.txt', 'w')
                kostil_list[1] = NONE
                kostil_list[1] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Второй датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[1]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[2] < 3:
                box = open('textbox.txt', 'w')
                kostil_list[2] = NONE
                kostil_list[2] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Третий датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[2]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            elif kostil_list[2] < 6:
                box = open('textbox.txt', 'w')
                kostil_list[2] = NONE
                kostil_list[2] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Третий датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[2]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[3] == 1:
                box = open('textbox.txt', 'w')
                kostil_list[3] = NONE
                kostil_list[3] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Четвертый датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[3]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()

            if kostil_list[4] > 79:
                box = open('textbox.txt', 'w')
                kostil_list[4] = NONE
                kostil_list[4] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Пятый датчик достиг АВАРИЙНОГО значения" + "\n"
                box.write(str(kostil_list[4]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            elif kostil_list[4] > 70:
                box = open('textbox.txt', 'w')
                kostil_list[4] = NONE
                kostil_list[4] = str(
                    now.strftime("%d-%m-%Y %H:%M:%S")) + " Пятый датчик достиг предаварийного значения" + "\n"
                box.write(str(kostil_list[4]) + "\n")
                box.close()
                box = open('textbox.txt', 'r')
                hude_text = box.read()
                ceh.insert(1.0, hude_text)
                box.close()
            kostil_list = NONE
    else:
        root.after(0, lambda: label_smeert.configure(image=svyas[0]))
        root.after(1 * int(opros / 20), lambda: label_smeert.configure(image=svyas[1]))
        root.after(2 * int(opros / 20), lambda: label_smeert.configure(image=svyas[2]))
        root.after(3 * int(opros / 20), lambda: label_smeert.configure(image=svyas[3]))
        root.after(4 * int(opros / 20), lambda: label_smeert.configure(image=svyas[4]))
        # root.after(5 * int(opros / 20), lambda: label_smeert.configure(image=svyas[5]))
        # root.after(6 * int(opros / 20), lambda: label_smeert.configure(image=svyas[6]))
        # root.after(7 * int(opros / 20), lambda: label_smeert.configure(image=svyas[7]))
        # root.after(8 * int(opros / 20), lambda: label_smeert.configure(image=svyas[8]))
        # root.after(9 * int(opros / 20), lambda: label_smeert.configure(image=svyas[9]))
        # root.after(10 * int(opros / 20), lambda: label_smeert.configure(image=svyas[10]))
        root.after(5 * int(opros / 20), lambda: label_smeert.configure(image=nosvyas))
        if i < 10:

            sost.delete(ALL)
            sost.configure(bg="red")
            sost.create_text(100, 10, text="СБОЙ РАБОТЫ", font="Verdana 8", justify="center")

            root.after(3 * int(opros / 4), lambda: sost.delete(ALL))
            root.after(3 * int(opros / 4), lambda: sost.configure(bg="yellow"))
            root.after(3 * int(opros / 4), lambda: sost.create_text(100, 10, text="Заносим данные в буфер", font="Verdana 8",
                                                justify="center"))

            buf[i][0:4] = list1
            # buf[i][1] = list[1]
            # buf[i][2] = list[2]
            # buf[i][3] = list[3]
            # buf[i][4] = list[4]
            buf[i][5] = "Сбой"
            buf[i][6] = str(now.strftime("%d-%m-%Y %H:%M:%S"))
            # print(str(now.strftime("%d-%m-%Y %H:%M:%S")))
            # print(buf[i][6])
            if i == 0:
                buffer_1_4.create_text(20, 12.5, text=list1[0])
                buffer_1_5.create_text(20, 12.5, text=list1[1])
                buffer_1_6.create_text(20, 12.5, text=list1[2])
                buffer_1_7.create_text(20, 12.5, text=list1[3])
                buffer_1_8.create_text(20, 12.5, text=list1[4])
            if i == 1:
                buffer_2_4.create_text(20, 12.5, text=list1[0])
                buffer_2_5.create_text(20, 12.5, text=list1[1])
                buffer_2_6.create_text(20, 12.5, text=list1[2])
                buffer_2_7.create_text(20, 12.5, text=list1[3])
                buffer_2_8.create_text(20, 12.5, text=list1[4])
            if i == 2:
                buffer_3_4.create_text(20, 12.5, text=list1[0])
                buffer_3_5.create_text(20, 12.5, text=list1[1])
                buffer_3_6.create_text(20, 12.5, text=list1[2])
                buffer_3_7.create_text(20, 12.5, text=list1[3])
                buffer_3_8.create_text(20, 12.5, text=list1[4])
            if i == 3:
                buffer_4_4.create_text(20, 12.5, text=list1[0])
                buffer_4_5.create_text(20, 12.5, text=list1[1])
                buffer_4_6.create_text(20, 12.5, text=list1[2])
                buffer_4_7.create_text(20, 12.5, text=list1[3])
                buffer_4_8.create_text(20, 12.5, text=list1[4])
            if i == 4:
                buffer_5_4.create_text(20, 12.5, text=list1[0])
                buffer_5_5.create_text(20, 12.5, text=list1[1])
                buffer_5_6.create_text(20, 12.5, text=list1[2])
                buffer_5_7.create_text(20, 12.5, text=list1[3])
                buffer_5_8.create_text(20, 12.5, text=list1[4])
            if i == 5:
                buffer_6_4.create_text(20, 12.5, text=list1[0])
                buffer_6_5.create_text(20, 12.5, text=list1[1])
                buffer_6_6.create_text(20, 12.5, text=list1[2])
                buffer_6_7.create_text(20, 12.5, text=list1[3])
                buffer_6_8.create_text(20, 12.5, text=list1[4])
            if i == 6:
                buffer_7_4.create_text(20, 12.5, text=list1[0])
                buffer_7_5.create_text(20, 12.5, text=list1[1])
                buffer_7_6.create_text(20, 12.5, text=list1[2])
                buffer_7_7.create_text(20, 12.5, text=list1[3])
                buffer_7_8.create_text(20, 12.5, text=list1[4])
            if i == 7:
                buffer_8_4.create_text(20, 12.5, text=list1[0])
                buffer_8_5.create_text(20, 12.5, text=list1[1])
                buffer_8_6.create_text(20, 12.5, text=list1[2])
                buffer_8_7.create_text(20, 12.5, text=list1[3])
                buffer_8_8.create_text(20, 12.5, text=list1[4])
            if i == 8:
                buffer_9_4.create_text(20, 12.5, text=list1[0])
                buffer_9_5.create_text(20, 12.5, text=list1[1])
                buffer_9_6.create_text(20, 12.5, text=list1[2])
                buffer_9_7.create_text(20, 12.5, text=list1[3])
                buffer_9_8.create_text(20, 12.5, text=list1[4])
            if i == 9:
                buffer_10_4.create_text(20, 12.5, text=list1[0])
                buffer_10_5.create_text(20, 12.5, text=list1[1])
                buffer_10_6.create_text(20, 12.5, text=list1[2])
                buffer_10_7.create_text(20, 12.5, text=list1[3])
                buffer_10_8.create_text(20, 12.5, text=list1[4])
            i = i + 1
        else:

            sost.delete(ALL)
            sost.configure(bg="red")
            sost.create_text(100, 10, text="БУФЕР ПЕРЕПОЛНЕН", font="Verdana 8", justify="center")

            root.after(1 * int(opros / 3), lambda: sost.delete(ALL))
            root.after(1 * int(opros / 3), lambda: sost.configure(bg="red"))
            root.after(1 * int(opros / 3),
                       lambda: sost.create_text(100, 10, text="Прореживаем буфер", font="Verdana 8",
                                                justify="center"))

            root.after(2 * int(opros / 3), lambda: sost.delete(ALL))
            root.after(2 * int(opros / 3), lambda: sost.configure(bg="green"))
            root.after(2 * int(opros / 3),
                       lambda: sost.create_text(100, 10, text="Увеличиваем время опроса", font="Verdana 8",
                                                justify="center"))


            now = NONE
            opros = opros*2
            root.after(0*int(opros/19), lambda: buffer_2_4.configure(bg="blue2"))
            root.after(0*int(opros/19), lambda: buffer_2_5.configure(bg="blue2"))
            root.after(0*int(opros/19), lambda: buffer_2_6.configure(bg="blue2"))
            root.after(0*int(opros/19), lambda: buffer_2_7.configure(bg="blue2"))
            root.after(0*int(opros/19), lambda: buffer_2_8.configure(bg="blue2"))

            root.after(1*int(opros/19), lambda: buffer_2_4.delete(ALL))
            root.after(1*int(opros/19), lambda: buffer_2_5.delete(ALL))
            root.after(1*int(opros/19), lambda: buffer_2_6.delete(ALL))
            root.after(1*int(opros/19), lambda: buffer_2_7.delete(ALL))
            root.after(1*int(opros/19), lambda: buffer_2_8.delete(ALL))

            root.after(2*int(opros/19), lambda: buffer_2_4.create_text(20, 12.5, text=buf[2][0]))
            root.after(2*int(opros/19), lambda: buffer_3_4.delete(ALL))
            root.after(2*int(opros/19), lambda: buffer_2_5.create_text(20, 12.5, text=buf[2][1]))
            root.after(2*int(opros/19), lambda: buffer_3_5.delete(ALL))
            root.after(2*int(opros/19), lambda: buffer_2_6.create_text(20, 12.5, text=buf[2][2]))
            root.after(2*int(opros/19), lambda: buffer_3_6.delete(ALL))
            root.after(2*int(opros/19), lambda: buffer_2_7.create_text(20, 12.5, text=buf[2][3]))
            root.after(2*int(opros/19), lambda: buffer_3_7.delete(ALL))
            root.after(2*int(opros/19), lambda: buffer_2_8.create_text(20, 12.5, text=buf[2][4]))
            root.after(2*int(opros/19), lambda: buffer_3_8.delete(ALL))

            root.after(3*int(opros/19), lambda: buffer_2_4.configure(bg="ghost white"))
            root.after(3*int(opros/19), lambda: buffer_2_5.configure(bg="ghost white"))
            root.after(3*int(opros/19), lambda: buffer_2_6.configure(bg="ghost white"))
            root.after(3*int(opros/19), lambda: buffer_2_7.configure(bg="ghost white"))
            root.after(3*int(opros/19), lambda: buffer_2_8.configure(bg="ghost white"))

            # -----------------------------------------------------
            root.after(4*int(opros/19), lambda: buffer_4_4.configure(bg="blue2"))
            root.after(4*int(opros/19), lambda: buffer_4_5.configure(bg="blue2"))
            root.after(4*int(opros/19), lambda: buffer_4_6.configure(bg="blue2"))
            root.after(4*int(opros/19), lambda: buffer_4_7.configure(bg="blue2"))
            root.after(4*int(opros/19), lambda: buffer_4_8.configure(bg="blue2"))

            root.after(5*int(opros/19), lambda: buffer_4_4.delete(ALL))
            root.after(5*int(opros/19), lambda: buffer_4_5.delete(ALL))
            root.after(5*int(opros/19), lambda: buffer_4_6.delete(ALL))
            root.after(5*int(opros/19), lambda: buffer_4_7.delete(ALL))
            root.after(5*int(opros/19), lambda: buffer_4_8.delete(ALL))

            root.after(6*int(opros/19), lambda: buffer_3_4.create_text(20, 12.5, text=buf[4][0]))
            root.after(6*int(opros/19), lambda: buffer_5_4.delete(ALL))
            root.after(6*int(opros/19), lambda: buffer_3_5.create_text(20, 12.5, text=buf[4][1]))
            root.after(6*int(opros/19), lambda: buffer_5_5.delete(ALL))
            root.after(6*int(opros/19), lambda: buffer_3_6.create_text(20, 12.5, text=buf[4][2]))
            root.after(6*int(opros/19), lambda: buffer_5_6.delete(ALL))
            root.after(6*int(opros/19), lambda: buffer_3_7.create_text(20, 12.5, text=buf[4][3]))
            root.after(6*int(opros/19), lambda: buffer_5_7.delete(ALL))
            root.after(6*int(opros/19), lambda: buffer_3_8.create_text(20, 12.5, text=buf[4][4]))
            root.after(6*int(opros/19), lambda: buffer_5_8.delete(ALL))

            root.after(7*int(opros/19), lambda: buffer_4_4.configure(bg="ghost white"))
            root.after(7*int(opros/19), lambda: buffer_4_5.configure(bg="ghost white"))
            root.after(7*int(opros/19), lambda: buffer_4_6.configure(bg="ghost white"))
            root.after(7*int(opros/19), lambda: buffer_4_7.configure(bg="ghost white"))
            root.after(7*int(opros/19), lambda: buffer_4_8.configure(bg="ghost white"))

            # -------------------------------------------------------------------------

            root.after(8*int(opros/19), lambda: buffer_6_4.configure(bg="blue2"))
            root.after(8*int(opros/19), lambda: buffer_6_5.configure(bg="blue2"))
            root.after(8*int(opros/19), lambda: buffer_6_6.configure(bg="blue2"))
            root.after(8*int(opros/19), lambda: buffer_6_7.configure(bg="blue2"))
            root.after(8*int(opros/19), lambda: buffer_6_8.configure(bg="blue2"))

            root.after(9*int(opros/19), lambda: buffer_6_4.delete(ALL))
            root.after(9*int(opros/19), lambda: buffer_6_5.delete(ALL))
            root.after(9*int(opros/19), lambda: buffer_6_6.delete(ALL))
            root.after(9*int(opros/19), lambda: buffer_6_7.delete(ALL))
            root.after(9*int(opros/19), lambda: buffer_6_8.delete(ALL))

            root.after(10*int(opros/19), lambda: buffer_4_4.create_text(20, 12.5, text=buf[6][0]))
            root.after(10*int(opros/19), lambda: buffer_7_4.delete(ALL))
            root.after(10*int(opros/19), lambda: buffer_4_5.create_text(20, 12.5, text=buf[6][1]))
            root.after(10*int(opros/19), lambda: buffer_7_5.delete(ALL))
            root.after(10*int(opros/19), lambda: buffer_4_6.create_text(20, 12.5, text=buf[6][2]))
            root.after(10*int(opros/19), lambda: buffer_7_6.delete(ALL))
            root.after(10*int(opros/19), lambda: buffer_4_7.create_text(20, 12.5, text=buf[6][3]))
            root.after(10*int(opros/19), lambda: buffer_7_7.delete(ALL))
            root.after(10*int(opros/19), lambda: buffer_4_8.create_text(20, 12.5, text=buf[6][4]))
            root.after(10*int(opros/19), lambda: buffer_7_8.delete(ALL))

            root.after(11*int(opros/19), lambda: buffer_6_4.configure(bg="ghost white"))
            root.after(11*int(opros/19), lambda: buffer_6_5.configure(bg="ghost white"))
            root.after(11*int(opros/19), lambda: buffer_6_6.configure(bg="ghost white"))
            root.after(11*int(opros/19), lambda: buffer_6_7.configure(bg="ghost white"))
            root.after(11*int(opros/19), lambda: buffer_6_8.configure(bg="ghost white"))
            # -----------------------------------------------------
            root.after(12*int(opros/19), lambda: buffer_8_4.configure(bg="blue2"))
            root.after(12*int(opros/19), lambda: buffer_8_5.configure(bg="blue2"))
            root.after(12*int(opros/19), lambda: buffer_8_6.configure(bg="blue2"))
            root.after(12*int(opros/19), lambda: buffer_8_7.configure(bg="blue2"))
            root.after(12*int(opros/19), lambda: buffer_8_8.configure(bg="blue2"))

            root.after(13*int(opros/19), lambda: buffer_8_4.delete(ALL))
            root.after(13*int(opros/19), lambda: buffer_8_5.delete(ALL))
            root.after(13*int(opros/19), lambda: buffer_8_6.delete(ALL))
            root.after(13*int(opros/19), lambda: buffer_8_7.delete(ALL))
            root.after(13*int(opros/19), lambda: buffer_8_8.delete(ALL))

            root.after(14*int(opros/19), lambda: buffer_5_4.create_text(20, 12.5, text=buf[8][0]))
            root.after(14*int(opros/19), lambda: buffer_9_4.delete(ALL))
            root.after(14*int(opros/19), lambda: buffer_5_5.create_text(20, 12.5, text=buf[8][1]))
            root.after(14*int(opros/19), lambda: buffer_9_5.delete(ALL))
            root.after(14*int(opros/19), lambda: buffer_5_6.create_text(20, 12.5, text=buf[8][2]))
            root.after(14*int(opros/19), lambda: buffer_9_6.delete(ALL))
            root.after(14*int(opros/19), lambda: buffer_5_7.create_text(20, 12.5, text=buf[8][3]))
            root.after(14*int(opros/19), lambda: buffer_9_7.delete(ALL))
            root.after(14*int(opros/19), lambda: buffer_5_8.create_text(20, 12.5, text=buf[8][4]))
            root.after(14*int(opros/19), lambda: buffer_9_8.delete(ALL))

            root.after(15*int(opros/19), lambda: buffer_8_4.configure(bg="ghost white"))
            root.after(15*int(opros/19), lambda: buffer_8_5.configure(bg="ghost white"))
            root.after(15*int(opros/19), lambda: buffer_8_6.configure(bg="ghost white"))
            root.after(15*int(opros/19), lambda: buffer_8_7.configure(bg="ghost white"))
            root.after(15*int(opros/19), lambda: buffer_8_8.configure(bg="ghost white"))

            # -------------------------------------------------------------------------
            root.after(16*int(opros/19), lambda: buffer_10_4.configure(bg="blue2"))
            root.after(16*int(opros/19), lambda: buffer_10_5.configure(bg="blue2"))
            root.after(16*int(opros/19), lambda: buffer_10_6.configure(bg="blue2"))
            root.after(16*int(opros/19), lambda: buffer_10_7.configure(bg="blue2"))
            root.after(16*int(opros/19), lambda: buffer_10_8.configure(bg="blue2"))

            root.after(17*int(opros/19), lambda: buffer_10_4.delete(ALL))
            root.after(17*int(opros/19), lambda: buffer_10_5.delete(ALL))
            root.after(17*int(opros/19), lambda: buffer_10_6.delete(ALL))
            root.after(17*int(opros/19), lambda: buffer_10_7.delete(ALL))
            root.after(17*int(opros/19), lambda: buffer_10_8.delete(ALL))

            root.after(18*int(opros/19), lambda: buffer_10_4.configure(bg="ghost white"))
            root.after(18*int(opros/19), lambda: buffer_10_5.configure(bg="ghost white"))
            root.after(18*int(opros/19), lambda: buffer_10_6.configure(bg="ghost white"))
            root.after(18*int(opros/19), lambda: buffer_10_7.configure(bg="ghost white"))
            root.after(18*int(opros/19), lambda: buffer_10_8.configure(bg="ghost white"))

            buf[1] = buf[2]
            buf[2] = buf[4]
            buf[3] = buf[6]
            buf[4] = buf[8]
            i = 5
    # print(buf)
    f.close()
    # if close == 1:
    #     return
    # box = open('textbox.txt','r')
    # hude_text = box.read()
    # ceh.insert(1.0, hude_text)
    # box.close()
    solve = root.after(opros, lambda: terminal())


# def exit_generation():
#     global close
#     close = 1


def nochance():
    global signal
    signal = 0


def normalin():
    global signal, opros
    signal = 1
    opros = 1600


def stop():
    global solve
    root.after_cancel(solve)

# Назначение клавиш--------------------
btn1.bind('<Button-1>', lambda event: terminal())
btn2.bind('<Button-1>', lambda event: nochance())
btn3.bind('<Button-1>', lambda event: normalin())
btn4.bind('<Button-1>', lambda event: stop())
# btn4.bind('<Button-1>', lambda event: exit_generation())
# ---------------------------------------
# отобразим программу в бесконечном цикле, всегда в конце программы
root.mainloop()
