#maturitný príklad 43-Pyrotechnik
import tkinter as tk, random

win = tk.Tk()

time = 60
stop = False
colors = ["green", "red", "gray", "blue", "orange"]
sirka = 20
dlzka = 300
wires = []

canvas = tk.Canvas(win, width=600, height=600, bg="white")
canvas.pack()

random.shuffle(colors)
for i in range(len(colors)):
    wires.append(canvas.create_rectangle(200, 200+(i*sirka), 200+dlzka, 200+(i+1)*sirka, fill=colors[i], width=2))

winner = random.choice(wires)

hodiny = canvas.create_text(300, 100, text=time, font=("Arial", 50, "bold"), anchor="center")

def checker(event):
    global stop
    if stop:
        return
    objekty = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    if winner in objekty:
        print("Vyhral si")
        stop = True
        print(objekty)
        canvas.create_text(300, 300, text="Vyhral si!", font=("Arial", 50, "bold"), anchor="center")

def timer():
    global time, stop
    if stop:
        return
    time -= 1
    canvas.itemconfig(hodiny, text=time)
    if time > 0:
        win.after(1000, timer)
    else:
        stop = True
        canvas.create_text(300, 300, text="Prehral si!", font=("Arial", 50, "bold"), anchor="center")

canvas.bind("<Button-1>", checker)
win.after(1000, timer)

win.mainloop()


