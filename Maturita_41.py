import tkinter as tk
win = tk.Tk()
canvas = tk.Canvas(win, width=500, height=600, bg='white')
canvas.pack()
vysledok = ''
canvas.create_text(250, 375, text='Vyber jedla', font=('Arial', 40), anchor='center', fill='hotpink')

obj1 = canvas.create_rectangle(50, 450, 150, 550, fill='red', outline='black')
obj2 = canvas.create_rectangle(150, 450, 250, 550, fill='green', outline='black')
obj3 = canvas.create_rectangle(250, 450, 350, 550, fill='blue', outline='black')
obj4 = canvas.create_rectangle(350, 450, 450, 550, fill='orange', outline='black')

popis = tk.Label(win, text='Zadaj kod studenta :', font=('Arial', 10))
popis.pack()
vstup = tk.Entry(win, width=20)
vstup.insert(0, "")
vstup.pack()

def nacitat_kod():
    hodnota = vstup.get()
    if hodnota == '' or not hodnota.isalpha():
        return ''
    return hodnota

def stlacenie(event):
    global vysledok
    aktualny_kod = nacitat_kod()
    if aktualny_kod == '':
        return
    najblizsi = canvas.find_closest(event.x, event.y)[0]
    if najblizsi == obj1:
        vysledok = aktualny_kod + ' c'
    elif najblizsi == obj2:
        vysledok = aktualny_kod + ' z'
    elif najblizsi == obj3:
        vysledok = aktualny_kod + ' m'
    elif najblizsi == obj4:
        vysledok = aktualny_kod + ' o'
    subor.write(vysledok + '\n')
subor = open('vyber_jedla.txt', 'w')
canvas.bind('<Button-1>', stlacenie)
canvas.mainloop()
subor.close()
win.mainloop()