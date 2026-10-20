import tkinter as tk
import ctypes
import os
import sys

crosshair = tk.Tk()

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    crosshair_png = os.path.join(sys._MEIPASS, "CurrentCrosshair.png")
    ico = os.path.join(sys._MEIPASS, "kappa.ico")
else:
    crosshair_png = "CurrentCrosshair.png"
    ico = "kappa.ico"


crosshair_image = tk.PhotoImage(file=crosshair_png) # The CurrentCrosshair that is selected
tk.Label(crosshair, image=crosshair_image, bg='#43ff43ff1').place(relx=0.5, rely=0.5, anchor='center') # Places a transparent widget with CurrentCrosshair.png in the center of the screen

crosshair.iconbitmap(ico) # ICO file
crosshair.title("Arrowhead: Enhancing Your Aim.")  # Title Bar
crosshair.wm_attributes("-topmost", True) # Forces the window to be topmost
crosshair.wm_attributes("-fullscreen", True) # Forces the window to be fullscreen
crosshair.wm_attributes("-transparentcolor", "#43ff43ff1") # Selected transparent color
crosshair.configure(bg="#43ff43ff1") # Makes the background of the main window transparent

crosshair.update_idletasks() # Makes sure the window exists before trying to tamper with the properties (so it doesn't get overridden)
hwnd = ctypes.windll.user32.GetParent(crosshair.winfo_id()) # Grabs the HWND of the outer window
GWL_STYLE = -20 # Allows the changing of Extended List window properties
WS_EX_LAYERED = 0x00080000 # Allows see-through windows
WS_EX_TRANSPARENT = 0x00000020 # Allows click-through to background applications
style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE) # Reads the current windows settings from line 11 to Line 12
ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT) # Writes the current windows settings back with WS_EX_LAYERED and WS_EX_TRANSPARENT allowing the window to be click-through

crosshair.lift()
crosshair.mainloop()