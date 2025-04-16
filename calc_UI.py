import tkinter as tk
import math
class Calculator():
    def __init__(self, root):
        self.bg_color = "#ffc0cb"
        self.last_answer = ""
        self.root = root
        self.root.configure(bg=self.bg_color)
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""

        # Display Entry
        self.display = tk.Entry(
            root, font=("Arial", 24), fg="black",
            borderwidth=2, relief="groove", justify='right',
        )
        self.display.pack(fill='both', ipadx=8, ipady=25, padx=10, pady=10)


        # Button Layout
        self.create_buttons()

    def create_buttons(self):
        button_layout = [
            [ ' (  ', ' )  ','CE','Del','^'],
            ['7','8','9', '÷','x²'],
            ['4','5','6', '*','x⁻¹'],
            ['1','2','3', '-','√'],
            ['0', '.', '=', '+','Ans']
        ]

        button_frame = tk.Frame(self.root,bg=self.bg_color)
        button_frame.pack(expand=True, fill='both')

        for i, row in enumerate(button_layout):
            for j, val in enumerate(row):
                button = tk.Button(
                    button_frame, text=val, font=("Arial", 18), fg="black", command=lambda val=val: self.on_click(val),bg=self.bg_color, activebackground="#f4a7b9"
                )
                button.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for j in range(5):
            button_frame.columnconfigure(j, weight=1)

    def on_click(self, key):
        if key == "=":
            try:
                expression = self.expression.replace('^', '**').replace('÷', '/').replace('√', 'math.sqrt')
                result = str(eval(expression))
                self.last_answer = result
                self.expression = result
            except:
                result = "Error"
                self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)

        elif key == "CE":
            self.expression = ""
            self.display.delete(0, tk.END)

        elif key == "Del":
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

        elif key == "x²":
            try:
                result = str(eval(self.expression + "**2"))
                self.expression = result
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""

        elif key == "x⁻¹":
            try:
                result = str(1 / eval(self.expression))
                self.expression = result
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""

        elif key == "Ans":
            self.expression += self.last_answer
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

        else:
            self.expression += str(key)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
