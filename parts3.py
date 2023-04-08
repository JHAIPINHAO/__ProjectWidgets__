import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class BottomFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.w = master
        listFrame = ttk.LabelFrame(self,text="List Box")
        listFrame.pack(side=tk.LEFT,padx=10,pady=10) 
        list = tk.Listbox(listFrame,height=6,width=10)
        list.pack(side=tk.LEFT)
        self.data = []
        for month in range(1,13):
            self.data.append(f'{month}月')

        for item in self.data:
            list.insert(tk.END,item)

        scrollBar = ttk.Scrollbar(listFrame,command=list.yview)
        scrollBar.pack(side=tk.RIGHT,fill=tk.Y)
        list.configure(yscrollcommand=scrollBar.set)
        list.bind('<<ListboxSelect>>', self.items_selected)

        comboBoxFrame = ttk.LabelFrame(self,text="Combo Box")
        comboBoxFrame.pack(side=tk.LEFT,fill=tk.Y,padx=10,pady=10)

        self.comboBoxValues  = ('請選擇月份',
                        'January',
						'February',
						'March',
						'April',
						'May',
						'June',
						'July',
						'August',
						'September',
						'October',
						'November',
						'December')
        
        
        comboBox = ttk.Combobox(comboBoxFrame,state= "readonly",width=8)
        comboBox.pack()
        comboBox['values'] = self.comboBoxValues        
        comboBox.current(0)
        comboBox.bind('<<ComboboxSelected>>', self.month_changed)
        
        
        
        

    def items_selected(self,event):
        listbox = event.widget
        #selectedIndex -> tuple
        (selectedIndex,) = listbox.curselection()        
        selectedValue = self.data[selectedIndex]
        self.w.listBoxEventOfBottomFrame(selectedValue)

    def month_changed(self,event):
        combobox = event.widget
        selectedIndex= combobox.current()
        selectedValue = self.comboBoxValues[selectedIndex]
        self.w.comboBoxEventOfBottomFrame(selectedValue)