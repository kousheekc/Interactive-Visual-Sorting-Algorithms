from tkinter import *
from tkinter import ttk
import time

class Interface:
    def __init__(self, algos, array):
        self.algos = algos
        self.array = array

        self.outlineColor = '#1e1e1e'
        self.mainScreenColor = '#e6e6e6'
        self.menuBarColor = '#34495e'
        self.nodeColor = '#32e632'
        self.buttonColor = '#1abc9c'

        self.canvasHeight = 680
        self.canvasWidth = 1200

        self.window = Tk()
        self.window.title('Visual Sorting Algos')

        self.window.geometry(f"{self.canvasWidth}x{self.canvasHeight}")

        self.canvas = Canvas(self.window, height = self.canvasHeight-80, width = self.canvasWidth, borderwidth=0, highlightthickness=0)

        self.show_steps = IntVar()
        self.colorScheme = IntVar()
        self.colorScheme.set(0)
        n = StringVar() 
        self.algoPicker = ttk.Combobox(self.window, width=26, font=('arial', 14), textvariable=n) 
        self.algoPicker['values'] = [algo for algo in self.algos]

        self.sortButton = Button(self.window, width=20, font=('arial', 14), text='sort', borderwidth=0, command=self.sortList)   
        self.generateButton = Button(self.window, width=20, font=('arial', 14), text='generate', borderwidth=0, command=self.generateUnsortedList)  
        self.clearButton = Button(self.window, width=10, font=('arial', 14), text='clear', borderwidth=0, command=self.clearCanvas) 
        self.lengthEntry = Entry(self.window, font=('arial', 13), width=25, borderwidth=0, justify=CENTER)
        self.show_steps_checkbox = Checkbutton(self.window, font=('arial', 12), text="show steps", variable=self.show_steps)
        self.darkRB = Radiobutton(self.window, text="dark", font=('arial', 10, 'bold'), variable=self.colorScheme, bg=self.menuBarColor, fg=self.buttonColor, value=1, command=self.setColorScheme)
        self.lightRB = Radiobutton(self.window, text="light", font=('arial', 10, 'bold'), variable=self.colorScheme, bg=self.menuBarColor, fg=self.buttonColor, value=0, command=self.setColorScheme)

        self.setColorScheme()

        self.algoPicker.place(x=5, y=48)
        self.sortButton.place(x=5,y=5)
        self.generateButton.place(x=350,y=5)
        self.lengthEntry.place(x=350, y=48)
        self.show_steps_checkbox.place(x=640, y=45)
        self.clearButton.place(x=970,y=5)
        self.darkRB.place(x=1130, y=0)
        self.lightRB.place(x=1130, y=20)
        self.canvas.pack(side='bottom')

    def setColorScheme(self):
        if self.colorScheme.get() == 1:
            self.outlineColor = '#e6e6e6'
            self.mainScreenColor = '#1e1e1e'
            self.menuBarColor = '#252526'
            self.linesColor = '#1abc9c'
            self.buttonColor = '#23a7f2'
            self.swap1Color = '#32e632'
            self.swap2Color = '#ff4d4d'
        else:
            self.outlineColor = '#1e1e1e'
            self.mainScreenColor = '#e6e6e6'
            self.menuBarColor = '#34495e'
            self.linesColor = '#1abc9c'
            self.buttonColor = '#1abc9c'
            self.swap1Color = '#32e632'
            self.swap2Color = '#ff4d4d'

        self.window.configure(bg=self.menuBarColor)
        self.canvas.configure(bg=self.mainScreenColor)
        self.lengthEntry.configure(bg=self.mainScreenColor, fg=self.outlineColor, insertbackground=self.outlineColor)
        self.sortButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.generateButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.show_steps_checkbox.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        self.clearButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.darkRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        self.lightRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        
    def generateUnsortedList(self):
        length = int(self.lengthEntry.get())       
        self.array.reset(length)
        self.update_array()

    def sortList(self):
        algo = self.algos[self.algoPicker.get()]
        swaps = algo.algorithm(self.array)
        for swap in swaps:
            if (self.show_steps.get() == 1):
                time.sleep(0.1)
            self.update_array(swap[0], swap[1])


    def clearCanvas(self):
        self.canvas.delete("all")
        self.update()

    def update_array(self, swap1=None, swap2=None):
        self.canvas.configure(bg=self.mainScreenColor)
        self.canvas.delete("all")

        k = int(self.canvasWidth/len(self.array))

        for i in range(len(self.array)):
            colour = self.linesColor

            if swap1 == self.array[i]:
                colour = self.swap1Color
            elif swap2 == self.array[i]:
                colour = self.swap2Color

            self.canvas.create_rectangle(i*k, self.array[i], i*k+k, self.canvasHeight, fill=colour)
        
        self.canvas.pack()
        self.update()


    def update(self):
        self.canvas.update()