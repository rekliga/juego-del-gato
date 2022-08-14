import tkinter
from tkinter import messagebox


ventana = tkinter.Tk()
ventana.geometry('300x200')
ventana.title("EL JUEGO DEL GATO")
cont = 0
filas = []
columnas = []

activador = 0
 
def l1():
    global cont,activador
    activador = 1
    #print(cont)
    info = bt1.grid_info()
    print((info["row"], info["column"]))
    #print(cont)
    filas.append(info["row"])
    columnas.append(info["row"])
    if cont == 0:
        bt1.config(text='X')
        cont += 1
    else:
        bt1.config(text='O')
        cont = 0
    bt1.config(state=tkinter.DISABLED)
    #print(cont)
bt1 = tkinter.Button(ventana,text='',command=l1)
bt1.grid(row=1,column=1)
#print(cont)
def l2():
    global cont
    #bt2.config(text='X')
    info = bt2.grid_info()
    print((info["row"], info["column"]))
    filas.append(info["row"])
    columnas.append(info["row"])
    if cont == 0:
        bt2.config(text='X')
        cont += 1
    else:
        bt2.config(text='O')
        cont = 0
    bt2.config(state=tkinter.DISABLED)

bt2 = tkinter.Button(ventana,text='',command=l2)
bt2.grid(row=1,column=2)

def l3():
    global cont
    #bt2.config(text='X')
    info = bt3.grid_info()
    filas.append(info["row"])
    columnas.append(info["row"])
    print((info["row"], info["column"]))
    if cont == 0:
        bt3.config(text='X')
        cont += 1
    else:
        bt3.config(text='O')
        cont = 0
    bt3.config(state=tkinter.DISABLED)

bt3 = tkinter.Button(ventana,text='',command=l3)
bt3.grid(row=1,column=3)

def l4():
    global cont
    #bt2.config(text='X')
    info = bt4.grid_info()
    filas.append(info["row"])
    columnas.append(info["row"])
    print((info["row"], info["column"]))
    if cont == 0:
        bt4.config(text='X')
        cont += 1
    else:
        bt4.config(text='O')
        cont = 0
    bt4.config(state=tkinter.DISABLED)
    
bt4 = tkinter.Button(ventana,text='',command=l4)
bt4.grid(row=2,column=1)

def l5():
    global cont
    #bt2.config(text='X')
    info = bt5.grid_info()
    filas.append(info["row"])
    columnas.append(info["row"])
    print((info["row"], info["column"]))
    if cont == 0:
        bt5.config(text='X')
        cont += 1
    else:
        bt5.config(text='O')
        cont = 0
    bt5.config(state=tkinter.DISABLED)
    
bt5 = tkinter.Button(ventana,text='',command=l5)
bt5.grid(row=2,column=2)

def l6():
    global cont
    #bt2.config(text='X')
    info = bt6.grid_info()
    filas.append(info["row"])
    columnas.append(info["row"])
    print((info["row"], info["column"]))
    if cont == 0:
        bt6.config(text='X')
        cont += 1
    else:
        bt6.config(text='O')
        cont = 0
    bt6.config(state=tkinter.DISABLED)
    
bt6 = tkinter.Button(ventana,text='',command=l6)
bt6.grid(row=2,column=3)

def l7():
    global cont
    #bt2.config(text='X')
    info = bt7.grid_info()
    filas.append(info["row"])
    columnas.append(info["row"])
    print((info["row"], info["column"]))
    if cont == 0:
        bt7.config(text='X')
        cont += 1
    else:
        bt7.config(text='O')
        cont = 0
    bt7.config(state=tkinter.DISABLED)
    
bt7 = tkinter.Button(ventana,text='',command=l7)
bt7.grid(row=3,column=1)

def l8():
    global cont
    #bt2.config(text='X')
    info = bt8.grid_info()
    print((info["row"], info["column"]))
    filas.append(info["row"])
    columnas.append(info["row"])
    if cont == 0:
        bt8.config(text='X')
        cont += 1
    else:
        bt8.config(text='O')
        cont = 0
    bt8.config(state=tkinter.DISABLED)
    
bt8 = tkinter.Button(ventana,text='',command=l8)
bt8.grid(row=3,column=2)

def l9():
    global cont
    #bt2.config(text='X')
    info = bt9.grid_info()
    print((info["row"], info["column"]))
    filas.append(info["row"])
    columnas.append(info["row"])
    if cont == 0:
        bt9.config(text='X')
        cont += 1
    else:
        bt9.config(text='O')
        cont = 0
    bt9.config(state=tkinter.DISABLED)
    
bt9 = tkinter.Button(ventana,text='',command=l9)
bt9.grid(row=3,column=3)
def update(): 
    print(filas)
    if activador==1:
        buton = tkinter.Button(ventana,text='ilker')
        buton.grid(row=7,column=7)
    try:
        if filas[0]==1:
            print('ganaste')
        #ventana.config(text=str(random.random()))
            messagebox.showinfo('ganaste carnal')
            print(filas)
    except:
        pass
    ventana.after(1000, update)

print('las filas son',filas)
print('las columnas',columnas)


ventana.after(1000, update)
ventana.mainloop()