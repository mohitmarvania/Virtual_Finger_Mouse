"""
This is the GUI which will show the user to activate the
Virtual mouse and deactivate it.
"""

from tkinter import *
from VirutalMouseDetector import virtualMouse

#----------------------------------------------------------------------------------------------
LIGHT_GREY = "#F5F5F5"
LABEL_COLOR = "#25265E"
DEFAULT_FONT = ("Arial", 20)
DIGIT_FONT = ("Arial", 30, "bold")
SMALL_FONT = ("Arial", 16)
LARGE_FONT = ("Arial", 40, "bold")
#----------------------------------------------------------------------------------------------


def settingUpGUI():

    def activate():
        deactivate_btn.destroy()
        deactivate_btns = Button(window, text="Deactivate", command=deactivate, fg="black", bg="black", padx=25, pady=50)
        deactivate_btns.grid(row=2, column=3)

        activate_btn.destroy()
        activate_btns = Button(window, text="Activate", command=activate, fg="red", bg="red", padx=25, pady=50,
                               state=DISABLED)
        activate_btns.grid(row=2, column=2)
        print("Hello world")
        vm = virtualMouse()

    def deactivate():
        print("Deactivating.....")

    frame = Frame(window, bg="black")
    heading = Label(window, text="Activate/Deactivate")
    heading.grid(row=1, column=2, sticky=NSEW)
    activate_btn = Button(window, text="Activate", command=activate, fg="red", bg="red", padx=25, pady=50)
    activate_btn.grid(row=2, column=2)
    deactivate_btn = Button(window, text="Deactivate", command=deactivate, fg="black", bg="black", padx=25, pady=50,
                            state=DISABLED)
    deactivate_btn.grid(row=2, column=3)


window = Tk()
window.geometry("300x300")
window.resizable(0, 0)
window.title("Virtual Mouse")
settingUpGUI()
window.mainloop()
