import tkinter



def transition_botton(widget):
    print("clicked")

window = tkinter.Tk()

window.geometry("400x400")

window.title("Screen Transition")


canvas1 = tkinter.Canvas(background="#cea", width=400, height=400)
canvas1.place(x=0, y=0)
label1 = tkinter.Label(canvas1, text="----- Ball Game -----")
label1.place(x=200,y=150, anchor=tkinter.CENTER)
button = tkinter.Button(canvas1, text="START",command=lambda:transition_button(window))
button.place(x=200, y=250, anchor=tkinter.CENTER)

def transition_button(widget):
    widget.destroy()
    window2 = tkinter.Tk()
    window2.geometry("400x400")
    window2.title("Screen 2")
    canvas2 = tkinter.Canvas(background="#eca", width=400, height=400)
    canvas2.place(x=0, y=0)
    label2 = tkinter.Label(canvas2)
    label2.place(x=200, y=200, anchor=tkinter.CENTER)

    
game.main()


root.mainloop()

