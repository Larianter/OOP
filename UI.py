import tkinter as tk
import ops
from parser import CalcTransformer, calcGrammar
from lark import Lark

class Calculator():
    def __init__(self, root):
        self.bg_color = "thistle2" #As I get to do the UI, I'll decide the colours >:D
        self.last_answer = "0"
        self.root = root
        self.root.configure(bg=self.bg_color) 
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.expression = ""

        self.parser = Lark(calcGrammar, parser="lalr", transformer=CalcTransformer(self.last_answer))

        # Display Entry
        self.display = tk.Entry(
            root, font=("Arial", 24), fg="black",
            borderwidth=2, relief="groove", justify='right',
        )
        top_frame = tk.Frame(self.root,bg=self.bg_color)
        top_frame.pack(fill='x', padx=10, pady=(5, 0))
        history_button = tk.Button(top_frame,text="History",command=self.show_history)
        history_button.pack(side="right")
        self.history_data = []
        self.display.bind("<Key>", lambda event: self.history(event))
        self.display.bind("<Return>", self.history)
        self.display.configure(state="disabled") # made sure the user can't edit the display
        self.display.pack(fill='both', ipadx=8, ipady=25, padx=10, pady=10)


        # Button Layout
        self.create_buttons()

    def history(self, event=None):
        xx = self.display.get().strip()
        list_partial_matches = []
        if xx.strip() != "":
            x = self.display.winfo_rootx()
            y = self.display.winfo_rooty()
            try:
                self.top_menu.destroy()
            except:
                print ("No active top")

            for item in self.history:
                if xx in item:
                    list_partial_matches.append(item)

            if list_partial_matches != []:
                self.top_menu = tk.Toplevel(self)
                self.top_menu.geometry("+{}+{}".format(x, y+20))
                self.top_menu.overrideredirect(1)
                for item in list_partial_matches:
                    btn = tk.Button(self.top_menu, text=item, highlightthickness=0, command= lambda i=item: self.select_word(i), anchor="w")
                    btn.pack(fill="x")
        else:
            if self.top_menu != None:
                self.top_menu.destroy()
                self.top_menu = None

    def record_history(self, event):
        print ("test2")
        x = self.display.get()
        if x not in self.history:
            self.history.append(x)

    def show_history(self):
        if hasattr(self, 'top_menu') and self.top_menu.winfo_exists():
            self.top_menu.destroy()
            return
        self.top_menu = tk.Toplevel(self.root)
        self.top_menu.title("History")
        self.top_menu.geometry("200x300")
        self.top_menu.configure(bg=self.bg_color)

        for item in reversed(self.history_data):
            btn = tk.Button(self.top_menu, text = item, anchor="w", bg="white", command= lambda i=item: self.select_word(i))
            btn.pack(fill="x")

    
    def select_word(self, word):
        self.display.delete(0, "end")
        self.display.insert(0, word)
        self.top_menu.destroy()

    def create_buttons(self):
        button_layout = [
            [ '(', ')','CE','Del','^'],
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

    def on_click(self, value):
        if value == 'CE':
            self.expression = ""
        elif value == 'Del':
            self.expression = self.expression[:-1]
        elif value == '=':
            try:
                self.parser = Lark(calcGrammar, parser="lalr", transformer=CalcTransformer(self.last_answer))
                result = self.parser.parse(self.expression)
                self.last_answer = str(result)
                self.history_data.append(f"{self.expression} = {self.last_answer}")
                self.expression = self.last_answer
            except Exception as e:
                print("Parse error:", e)
                self.expression = "Error"
        elif value == 'Ans':
            self.expression += self.last_answer
        else:
            self.expression += value
        self.update_display()