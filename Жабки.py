#Параметры
size = 200
margin = 60

#-------------
from tkinter import *
from tkinter.messagebox import *

#-Окно и поле-
root = Tk()
root.title('Девятьнашки')
canvas = Canvas(root,width=size*7+margin*2,height=size+margin*2,bg='#409945')
canvas.pack()

#Картинки с лягушками
img1=PhotoImage(file='frog-1.gif')
img2=PhotoImage(file='frog-2.gif')

#Функция нажатия на лягушку
def swap(event):
    nowx = (event.x-margin)//size
    nowy = (event.y-margin)//size
    
    #-Отсеиваем нажатия за пределы игрового поля
    if nowx<0 or nowx>6 or nowy!= 0:
        pass
    if frogs[nowx] == 1:
        if nowx > 0 and frogs[nowx-1] == 0:
            frogs[nowx],frogs[nowx-1] = frogs[nowx-1],frogs[nowx]
            field()
        if nowx > 1 and frogs[nowx-2] == 0:
            frogs[nowx],frogs[nowx-2] = frogs[nowx-2],frogs[nowx]
            field()
    if frogs[nowx] == -1:
        if nowx < 6 and frogs[nowx+1] == 0:
            frogs[nowx],frogs[nowx+1] = frogs[nowx+1],frogs[nowx]
            field()
        if nowx < 5 and frogs[nowx+2] == 0:
            frogs[nowx],frogs[nowx+2] = frogs[nowx+2],frogs[nowx]
            field()

#Функция генерации поля
start = [-1,-1,-1,0,1,1,1]
frogs = [-1,-1,-1,0,1,1,1]
toclean = []
def field():
 #Удаляем старых жабок
    for i in toclean:
        canvas.delete(i)
 #--------------------
    for i in range(len(frogs)):
        x = margin+i*size
        y = margin
        canvas.create_rectangle(x,y,x+size,y+size,outline='#6fc968')
        if frogs[i] == -1:
            frog = canvas.create_image(x+size/2,y+size/2,image=img1)
            toclean.append(frog)
        if frogs[i] == 1:
            frog = canvas.create_image(x+size/2,y+size/2,image=img2)
            toclean.append(frog)
    if frogs == [1,1,1,0,-1,-1,-1]:
        showinfo('УРА!','Жабки разошлись!')

#Функция новой игры
def new(event):
    for i in range(len(start)):
        frogs[i] = start[i]
    field()

#Кнопка для новой игры
butnew = Button(text=('Новая игра'),                 
               bg='#320311', fg='#409945',  # цвет фона и надписи
               activebackground='#409945',  # цвет нажатой кнопки
               activeforeground='#320311',  # цвет надписи когда кнопка нажата
               font=("Comic Sans MS", size//10))  # шрифт и размер надписи
butnew.pack(side = BOTTOM,expand=1,fill=BOTH)
butnew.bind('<Button-1>', new)


field()
canvas.bind('<Button-1>',swap)
root.mainloop()
