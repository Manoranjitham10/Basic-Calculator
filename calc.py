import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Calculator")
        self.root.geometry("400x500")
        self.expression = ""
        
        self.result_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        result_frame = tk.Frame(self.root, bg="lightblue")
        result_frame.pack(expand=True, fill="both")
        
        result_entry = tk.Entry(result_frame, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg="white", fg="black")
        result_entry.grid(row=0, column=0, columnspan=5)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")
        
        buttons = [
            ('7', 'lightgrey'), ('8', 'lightgrey'), ('9', 'lightgrey'), ('/', 'orange'), ('C', 'red'),
            ('4', 'lightgrey'), ('5', 'lightgrey'), ('6', 'lightgrey'), ('*', 'orange'), ('<<', 'red'),
            ('1', 'lightgrey'), ('2', 'lightgrey'), ('3', 'lightgrey'), ('-', 'orange'), ('', 'white'),
            ('0', 'lightgrey'), ('.', 'lightgrey'), ('=', 'green'), ('+', 'orange'), ('', 'white')
        ]
        
        row = 1
        col = 0
        
        for (button, color) in buttons:
            if button != '':
                button_widget = tk.Button(button_frame, text=button, font=("Arial", 18), bd=1, relief="raised", width=5, height=2, bg=color, fg="black", command=lambda b=button: self.button_click(b))
                button_widget.grid(row=row, column=col, sticky="nsew")
            
            col += 1
            if col == 5:
                col = 0
                row += 1
        
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)
    
    def button_click(self, button):
        if button == 'C':
            self.expression = ""
        elif button == '<<':
            self.expression = self.expression[:-1]
        elif button == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += button
        
        self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
