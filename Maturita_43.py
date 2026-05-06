import tkinter as tk, random

win = tk.Tk()

time = 60
colors = ["green", "red", "gray", "blue", "orange"]
sirka = 20
dlzka = 300
wires = []
hram = True  # Premenná, ktorá stráži, či hra ešte beží

canvas = tk.Canvas(win, width=600, height=600, bg="white")
canvas.pack()

random.shuffle(colors)
for i in range(len(colors)):
    w = canvas.create_rectangle(200, 200 + (i * sirka), 200 + dlzka, 200 + (i + 1) * sirka, fill=colors[i], width=2)
    wires.append(w)

winner = random.choice(wires)

# Uložíme si ID textu do premennej 'hodiny'
hodiny = canvas.create_text(300, 100, text=time, font=("Arial", 50, "bold"), anchor="center")


def checker(event):
    global hram
    if not hram: return  # Ak už je koniec, nič nerob

    objekty = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    if winner in objekty:
        hram = False
        canvas.create_text(300, 450, text="Vyhral si!", fill="green", font=("Arial", 50, "bold"))
    elif len(objekty) > 0:  # Ak klikol na iný drôt (nepovinné, ale logické pre pyrotechnika)
        hram = False
        canvas.create_text(300, 450, text="Prehral si!", fill="red", font=("Arial", 50, "bold"))


def timer():
    global time, hram
    if not hram: return  # Ak sme vyhrali, nepokračuj v odpočítavaní

    time = time - 1
    # DÔLEŽITÉ: Tu aktualizujeme text na plátne
    canvas.itemconfig(hodiny, text=time)

    if time > 0:
        win.after(1000, timer)
    else:
        hram = False
        canvas.create_text(300, 450, text="Prehral si!", fill="red", font=("Arial", 50, "bold"))


canvas.bind("<Button-1>", checker)
win.after(1000, timer)

win.mainloop()


