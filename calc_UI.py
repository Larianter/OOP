import tkinter as tk

class Calculator():
    def __init__(self, root):
        self.bg_color = "thistle2" #As I get to do the UI, I'll decide the colours >:D
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
        self.display.configure(state="disabled") # made sure the user can't edit the display
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
        #Don't touch the holy buttons, for working with the layout makes me sad :(

        button_frame = tk.Frame(self.root,bg=self.bg_color)
        button_frame.pack(expand=True, fill='both')

        for i, row in enumerate(button_layout):
            for j, val in enumerate(row):
                button = tk.Button(
                    button_frame, text=val, font=("Arial", 18), fg="black", command=lambda val=val: self.on_click(val),bg=self.bg_color, activebackground="rosybrown2"
                )
                button.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)

        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for j in range(5):
            button_frame.columnconfigure(j, weight=1)

    def update_display(self):
        self.display.configure(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)
        self.display.configure(state='disabled')

    def on_click(self, value):
        if value == 'CE':
            self.expression = ""
        elif value == 'Del':
            self.expression = self.expression[:-1]
        elif value == '=':
            try:
                # Replace symbols with Python operators
                expression = self.expression.replace('÷', '/').replace('x²', '**2').replace('√', '**0.5') \
                                            .replace('^', '**').replace('x⁻¹', '**-1')
                result = str(eval(expression))
                self.last_answer = result
                self.expression = result
            except Exception:
                self.expression = "Error"
        elif value == 'Ans':
            self.expression += self.last_answer
        else:
            self.expression += value.strip()

        self.update_display()