import tkinter as tk
import ctypes
import os
import sys

crosshair = tk.Tk()
selector = tk.Toplevel()

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    crosshair1_png = os.path.join(sys._MEIPASS, "Crosshair1.png")
    crosshair2_png = os.path.join(sys._MEIPASS, "Crosshair2.png")
    Empty_png = os.path.join(sys._MEIPASS, "Empty.png")
    ico = os.path.join(sys._MEIPASS, "kappa.ico")
else:
    crosshair1_png = "Crosshair1.png"
    crosshair2_png = "Crosshair2.png"
    Empty_png = "Empty.png"
    ico = "kappa.ico"

def crosshairswitch2():
    crosshairswitch2 = tk.PhotoImage(file=crosshair2_png)
    crosshair_image.config(file=crosshair2_png)

def crosshairswitch1():
    crosshairswitch1 = tk.PhotoImage(file=crosshair1_png)
    crosshair_image.config(file=crosshair1_png)

def crosshairhide():
    crosshairhide = tk.PhotoImage(file=Empty_png)
    crosshair_image.config(file=Empty_png)

crosshair_image = tk.PhotoImage(file=crosshair1_png) # The CurrentCrosshair that is selected
tk.Label(crosshair, image=crosshair_image, bg='#43ff43ff1').place(relx=0.5, rely=0.5, anchor='center') # Places a transparent widget with Crosshair1.png in the center of the screen

crosshair.iconbitmap(ico) # ICO file
crosshair.title("Arrowhead: Enhancing Your Aim.")  # Title Bar
crosshair.wm_attributes("-topmost", True) # Forces the window to be topmost
crosshair.wm_attributes("-fullscreen", True) # Forces the window to be fullscreen
crosshair.wm_attributes("-transparentcolor", "#43ff43ff1") # Selected transparent color
crosshair.configure(bg="#43ff43ff1") # Makes the background of the main window transparent

selector.iconbitmap(ico)
selector.title("Arrowhead: Crosshair Selector.")
selector.configure(bg="gray")
selector.geometry("500x500")
selector.resizable(False, False)

crosshairbutton2 = tk.Button(selector,text="Crosshair2",command=crosshairswitch2).place(relx=0.6, rely=0.5, anchor='center')
crosshairbutton1 = tk.Button(selector,text="Crosshair1",command=crosshairswitch1).place(relx=0.4, rely=0.5, anchor='center')
crosshairhidebutton = tk.Button(selector,text="Hide Crosshair",command=crosshairhide).place(relx=0.5, rely=0.7, anchor='center')

crosshair.update_idletasks() # Makes sure the window exists before trying to tamper with the properties (so it doesn't get overridden)
hwnd = ctypes.windll.user32.GetParent(crosshair.winfo_id()) # Grabs the HWND of the outer window
GWL_STYLE = -20 # Allows the changing of Extended List window properties
WS_EX_LAYERED = 0x00080000 # Allows see-through windows
WS_EX_TRANSPARENT = 0x00000020 # Allows click-through to background applications
style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE) # Reads the current windows settings from line 11 to Line 12
ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT) # Writes the current windows settings back with WS_EX_LAYERED and WS_EX_TRANSPARENT allowing the window to be click-through

crosshair.lift()
crosshair.mainloop()