import pyautogui
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
import tkinter as tk
from screeninfo import get_monitors 
import os
from tkterminal import Terminal
import pynput
from pynput.mouse import Listener
import pyautogui
import turtle
import math 
import random




def update_progress_bar(progressbar, screen_width, screen_height, root):
    x, y = root.winfo_pointerx() - root.winfo_rootx(), root.winfo_pointery() - root.winfo_rooty()
    progress = 100 - (y / (screen_height / 100))
    progressbar['value'] = progress
    progressbar.after(1, update_progress_bar, progressbar, screen_width, screen_height, root)
    update_mouse_lines(root, x, y, screen_width, screen_height)

def update_mouse_lines(root, mouse_x, mouse_y, screen_width, screen_height):
    canvas = root.canvas
    #canvas.delete("mouse_line")  
    
    
    
    def on_key_press(event):
        if event.char:
            colors = ["white", "black", "red", "orange", "green", "yellow", "purple", "blue"]
            
            #canvas.create_line(0, mouse_y, screen_width, mouse_y, fill="white",)
            #canvas.create_line(mouse_x, 0, mouse_x, screen_height, fill="white")
            size = random.randint(0, 20)
            canvas.create_oval(mouse_x - size, mouse_y - size, mouse_x + size, mouse_y + size, fill=(random.choice(colors)))

    root.bind("<space>", on_key_press)

    
    

def main():
    root = tk.Tk()
    
    root.attributes('-alpha', .5)

    root.attributes('-topmost', True)
    

    monitor = get_monitors()[0]
    screen_width = monitor.width
    screen_height = monitor.height

    root.geometry(f"{screen_width}x{screen_height}+0+0")

    canvas = tk.Canvas(root, bg='blue', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    root.canvas = canvas

     
    progressbar = ttk.Progressbar(root, orient=tk.VERTICAL, length=160, style="green.Horizontal.TProgressbar") 
    progressbar.place(x=(screen_width / 2), y=(screen_height / 6))

    style = ttk.Style()
    style.theme_use('default')
    style.configure("green.Horizontal.TProgressbar", background='#FFFF00')
    
    #terminal = Terminal(pady=5, padx=5)
    #terminal.pack(expand=True, fill='both')

    update_progress_bar(progressbar, screen_width, screen_height, root) 

    root.mainloop()

main()