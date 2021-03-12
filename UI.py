from tkinter import *
from tkinter import ttk
import algorithms

class VisualSortingAlgos:
    def __init__(self):
        self.algos = {"Selection Sort": algorithms.SelectionSort(), "Bubble Sort": algorithms.BubbleSort(), "Insertion Sort": algorithms.InsertionSort(), "Merge Sort": algorithms.MergeSort(), "Quick Sort": algorithms.QuickSort()}

        self.length = 100

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

        n = StringVar() 
        self.algoPicker = ttk.Combobox(self.window, width=26, font=('arial', 14), textvariable=n) 
        self.algoPicker['values'] = [algo for algo in self.algos]

        self.generateButton = Button(self.window, width=10, font=('arial', 14), text='generate', borderwidth=0, command=self.generateUnsortedList)
        self.sortButton = Button(self.window, width=10, font=('arial', 14), text='sort', borderwidth=0, command=self.sortList)   
        self.clearButton = Button(self.window, width=10, font=('arial', 14), text='clear', borderwidth=0, command=self.clearCanvas) 
        self.changeLengthButton = Button(self.window, width=20, font=('arial', 14), text='update length', borderwidth=0, command=self.updateLength)  
        self.lengthEntry = Entry(self.window, font=('arial', 13), width=25, borderwidth=0, justify=CENTER)

        self.colorScheme = IntVar()
        self.colorScheme.set(0)

        self.darkRB = Radiobutton(self.window, text="dark", font=('arial', 10, 'bold'), variable=self.colorScheme, bg=self.menuBarColor, fg=self.buttonColor, value=1, command=self.setColorScheme)
        self.lightRB = Radiobutton(self.window, text="light", font=('arial', 10, 'bold'), variable=self.colorScheme, bg=self.menuBarColor, fg=self.buttonColor, value=0, command=self.setColorScheme)

        self.setColorScheme()

        self.algoPicker.place(x=5, y=48)

        self.generateButton.place(x=5,y=5)
        self.sortButton.place(x=125,y=5)
        self.changeLengthButton.place(x=350,y=5)
        self.lengthEntry.place(x=350, y=48)
        self.clearButton.place(x=970,y=5)
        self.darkRB.place(x=1130, y=0)
        self.lightRB.place(x=1130, y=20)
        self.canvas.pack(side='bottom')

        self.userInputAndVisualize()

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
        self.generateButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.changeLengthButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.lengthEntry.configure(bg=self.mainScreenColor, fg=self.outlineColor, insertbackground=self.outlineColor)
        self.sortButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.clearButton.configure(fg=self.mainScreenColor, bg=self.buttonColor, activebackground=self.buttonColor, activeforeground=self.mainScreenColor)
        self.darkRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        self.lightRB.configure(bg=self.menuBarColor, fg=self.buttonColor, activebackground=self.menuBarColor, activeforeground=self.buttonColor)
        
    def updateLength(self):
        self.length = int(self.lengthEntry.get())       

    def generateUnsortedList(self):
        algo = self.algos[self.algoPicker.get()]
        algo.change_num_elements(self.length)
        algo.reset(self.canvas, self.mainScreenColor, self.linesColor, self.canvasHeight, self.canvasWidth, self.swap1Color, self.swap2Color)
        # self.update(algo)

    def sortList(self):
        algo = self.algos[self.algoPicker.get()]
        algo.algorithm(self.canvas, self.mainScreenColor, self.linesColor, self.canvasHeight, self.canvasWidth, self.swap1Color, self.swap2Color)
        # self.update(algo)

    def clearCanvas(self):
        self.canvas.delete("all")
        self.canvas.update()

    def userInputAndVisualize(self):
        loopActive = True
        while loopActive:
            self.canvas.update()

VisualSortingAlgos()