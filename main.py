import pyautogui
import tkinter as tk
from tkinter.filedialog import *

# Create gui
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height= 300)
canvas.pack()

# screenshot function
def takeScreenShot():
    myscreenshot =pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+"_screenshot.png")

 # screenshot Button
mybutton = tk.Button(text="Take Screenshot", command=takeScreenShot, font=10)

# Create window
canvas.create_window(150, 150, window=mybutton)

tk.mainloop()