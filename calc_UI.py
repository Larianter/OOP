import tkinter as tk
import ops

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

        for x, row in enumerate(button_layout):
            for y, val in enumerate(row):
                button = tk.Button(
                    button_frame, text=val, font=("Arial", 18), fg="black", command=lambda val=val: self.on_click(val),bg=self.bg_color, activebackground="rosybrown2"
                )
                button.grid(row=x, column=y, sticky="nsew", padx=1, pady=1)

        for x in range(5):
            button_frame.rowconfigure(x, weight=1)
        for y in range(5):
            button_frame.columnconfigure(y, weight=1)

    def update_display(self):
        self.display.configure(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)
        self.display.configure(state='disabled')

    def evaluate_expression(self, expr):
        try:
            expr = expr.strip()
            if "√" in expr:
                num = float(expr.replace("√", ""))
                op = ops.Square(num)
                return op.sqrt()

            if "x²" in expr:
                num = float(expr.replace("x²", ""))
                op = ops.Exponent(num, 2)
                return op.exp()

            if "x⁻¹" in expr:
                num = float(expr.replace("x⁻¹", ""))
                op = ops.Inverse(num)
                return op.inv()

            for operator, cls, method_name in [
                ('+', ops.Addition, 'add'),
                ('-', ops.Subtraction, 'sub'),
                ('*', ops.Multiplication, 'mul'),
                ('÷', ops.Division, 'div'),
                ('^', ops.Exponent, 'exp'),
            ]:
                if operator in expr:
                    a, b = expr.split(operator)
                    a = float(a.strip())
                    b = float(b.strip())
                    op = cls(a, b)
                    return getattr(op, method_name)()
                    
            # fallback if no operator matched
            return float(expr)

        except Exception as e:
            print("Evaluation error:", e)
            return "Error"

    def on_click(self, value):
        if value == 'CE':
            self.expression = ""
        elif value == 'Del':
            self.expression = self.expression[:-1]
        elif value == '=':
            result = self.evaluate_expression(self.expression)
            self.last_answer = str(result)
            self.expression = self.last_answer
        elif value == 'Ans':
            self.expression += self.last_answer
        else:
            self.expression += value
        self.update_display()