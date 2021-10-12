import random
import tkinter as tk

root=tk.Tk()
root.geometry("400x200")
num = tk.StringVar()
num.set(u"\u2702")
dice=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
def roll():
    num.set(random.choice(dice))
root.title("Dice Simulator")
label=tk.Label(root,textvariable=num,fg="red",font=("Arial",100)).pack()
button=tk.Button(text="Roll Me..",fg="green",command=roll).pack()


root.mainloop()
