from tkinter import *

from ball import Ball

from paddle import Paddle





class Game:

##    def transition_button(widget):
        
##        print("clicked')

##        window = tkinter.Tk()
##        window.geometry("400x400")
##        window.title("Screen Transition")

              
##        self.canvas = Canvas(background="#cea", width=400, height=400)
##        self.place(x=0, y=0)
##        label1 = tkinter.Label(self.canvvas, text="game start")
##        label1.place(x=200, y=150, anchor=tkinter.CENTER)
##        button.place(x=200, y=250, anchor=tkinter.CENTER)
        

##        window.mainloop()

    def __init__(self):

        #image = tk.PhotoImage(file='kirakira.gif')
        #label01['image'] = image

       # widget.place_forget()
        
        self.tk = Tk()
        self.tk.title("Game")                       
        self.tk.resizable(False, False)             
        self.tk.wm_attributes("-topmost", True)     

        
        self.canvas = Canvas(self.tk, width=400, height=400, bd=False, highlightthickness=False)
        #self.photo_image = imageTk.PhotoImage(file="kirakira.gif")
        self.canvas.pack()      
        self.tk.update()        

        #canvas = tkinter.Canvas(window, bg="#deb887", height=200, width=200)
        #canvas.place(x=0, y=0)
        
        self.paddle = Paddle(self.canvas, "blue")
        self.ball = Ball(self.canvas, "red", self.paddle)

        
        self.canvas.bind_all("<KeyPress-Left>", self.paddle.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.paddle.turn_right)
        self.canvas.bind_all("<KeyPress-space>", self.ball.start)


    


    def main(self):
        
        self.update()       
        self.tk.mainloop()  

    def update(self):
        
        self.ball.draw()
    
        self.paddle.draw()


        self.canvas.after(1000 // 60, self.update)



game = Game()
game.main()




