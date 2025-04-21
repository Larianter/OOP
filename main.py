# File name: main.py
# Author: Noora Pellinen
# Description: Initalizes calculator and runs the application.

import UI,tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = UI.Calculator(root)
    root.mainloop()