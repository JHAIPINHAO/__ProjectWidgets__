import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MedianFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        # create ttk.radiobuttons in self
        # ttk.Style change ttk.Radiobutton shape
        self.w = master
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('clam')          
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT, padx=10, pady=10)
        self.radioStringVar = tk.StringVar()
        self.radiobutton1 = ttk.Radiobutton(radionFrame, text='Option 1',variable=self.radioStringVar,value="Option 1",command=self.radioEvent)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(radionFrame, text='Option 2',variable=self.radioStringVar,value="Option 2",command=self.radioEvent)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(radionFrame, text='Option 3', variable=self.radioStringVar,value="Option 3",command=self.radioEvent)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(radionFrame, text='Option 4', variable=self.radioStringVar,value="Option 4",command=self.radioEvent)
        self.radiobutton4.pack()
        self.radioStringVar.set('Option 1')

        # create ttk.checkbuttons in self
        checkFrames = ttk.LabelFrame(self, text='Check Buttons')
        checkFrames.pack(side=tk.RIGHT, padx=10, pady=10)

        self.checkStringVar1 = tk.StringVar()
        self.checkStringVar2 = tk.StringVar()
        self.checkStringVar3 = tk.StringVar()
        self.checkStringVar4 = tk.StringVar()

        self.checkbutton1 = ttk.Checkbutton(checkFrames, text='Option 1',variable=self.checkStringVar1,command=self.checkEvent,onvalue='op1check',offvalue='op1off')
        self.checkbutton1.pack()
        self.checkbutton2 = ttk.Checkbutton(checkFrames, text='Option 2',variable=self.checkStringVar2,command=self.checkEvent,onvalue='op2check',offvalue='op2off')
        self.checkbutton2.pack()
        self.checkbutton3 = ttk.Checkbutton(checkFrames, text='Option 3', variable=self.checkStringVar3,command=self.checkEvent,onvalue='op3check',offvalue='op3off')
        self.checkbutton3.pack()
        self.checkbutton4 = ttk.Checkbutton(checkFrames, text='Option 4', variable=self.checkStringVar4,command=self.checkEvent,onvalue='op4check',offvalue='op4off')
        self.checkbutton4.pack() 
        
    
    def radioEvent(self):
        self.w.radioButtonEventOfMedianFrame(self.radioStringVar.get())

    def checkEvent(self):
        print(self.checkStringVar1.get())
        print(self.checkStringVar2.get())
        print(self.checkStringVar3.get())
        print(self.checkStringVar4.get())
        #self.w.radioButtonEventOfMedianFrame(self.checkStringVar.get())