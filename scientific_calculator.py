import tkinter as tk
import math

# ------------------ Function ------------------
def press(key):
    try:
        if key == 'C':
            entry.delete(0, tk.END)
        elif key == '⌫':
            entry.delete(len(entry.get()) - 1)
        elif key == '=':
            expression = entry.get().replace('×', '*').replace('÷', '/').replace('^', '**')
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        elif key == 'π':
            entry.insert(tk.END, str(math.pi))
        elif key == 'e':
            entry.insert(tk.END, str(math.e))
        elif key == '√':
            entry.insert(tk.END, str(math.sqrt(float(entry.get()))))
        elif key == 'x²':
            entry.insert(tk.END, str(float(entry.get()) ** 2))
        elif key == 'x³':
            entry.insert(tk.END, str(float(entry.get()) ** 3))
        elif key == '1/x':
            entry.insert(tk.END, str(1 / float(entry.get())))
        elif key == '|x|':
            entry.insert(tk.END, str(abs(float(entry.get()))))
        elif key == 'exp':
            entry.insert(tk.END, str(math.exp(float(entry.get()))))
        elif key == 'ln':
            entry.insert(tk.END, str(math.log(float(entry.get()))))
        elif key == 'log':
            entry.insert(tk.END, str(math.log10(float(entry.get()))))
        elif key == 'n!':
            entry.insert(tk.END, str(math.factorial(int(entry.get()))))
        elif key == '+/-':
            entry.insert(tk.END, str(-float(entry.get())))
        elif key == 'sin':
            entry.insert(tk.END, str(math.sin(math.radians(float(entry.get())))))
        elif key == 'cos':
            entry.insert(tk.END, str(math.cos(math.radians(float(entry.get())))))
        elif key == 'tan':
            entry.insert(tk.END, str(math.tan(math.radians(float(entry.get())))))
        elif key == 'sec':
            entry.insert(tk.END, str(1 / math.cos(math.radians(float(entry.get())))))
        elif key == 'csc':
            entry.insert(tk.END, str(1 / math.sin(math.radians(float(entry.get())))))
        elif key == 'cot':
            entry.insert(tk.END, str(1 / math.tan(math.radians(float(entry.get())))))
        else:
            entry.insert(tk.END, key)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ------------------ UI Setup ------------------
window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("520x1050")
window.config(bg="#0f0f0f")
window.resizable(False, False)

# ------------------ Display ------------------
entry = tk.Entry(window, font=("Segoe UI", 24), bg="#1f1f1f", fg="white",
                 bd=0, insertbackground="white", justify='right')
entry.pack(fill="both", ipady=10, padx=20, pady=(20, 10))

# ------------------ Mode Selectors ------------------
mode_frame = tk.Frame(window, bg="#0f0f0f")
mode_frame.pack(pady=(0, 10))

mode_label = tk.Label(mode_frame, text="Mode:", fg="white", bg="#0f0f0f", font=('Segoe UI', 12))
mode_label.pack(side="left")

mode_var = tk.StringVar()
mode_var.set("Function")
mode_menu = tk.OptionMenu(mode_frame, mode_var, "Trigonometry", "Function")
mode_menu.config(bg="#2f2f2f", fg="white", bd=0, highlightthickness=0, font=('Segoe UI', 11))
mode_menu.pack(side="left", padx=10)

# ------------------ Buttons ------------------
buttons = [
    ['2^n', 'π', 'e', 'C', '⌫'],
    ['x²', '1/x', '|x|', 'exp', 'mod'],
    ['√', '(', ')', 'n!', '÷'],
    ['x³', '7', '8', '9', '×'],
    ['10^x', '4', '5', '6', '−'],
    ['log', '1', '2', '3', '+'],
    ['ln', '+/-', '0', '.', '='],
    ['sin', 'cos', 'tan', 'sec', 'csc', 'cot']
]

frame = tk.Frame(window, bg="#0f0f0f")
frame.pack(pady=5)

# ------------------ Button Design ------------------
def format_btn(b):
    if b == 'C':
        bg = '#d32f2f'
        active_bg = '#b71c1c'
    elif b == '⌫':
        bg = '#f0ad4e'
        active_bg = '#ec971f'
    elif b == '=':
        bg = '#28a745'
        active_bg = '#218838'
    else:
        bg = '#2f2f2f'
        active_bg = '#3f3f3f'

    return {
        'text': b,
        'font': ('Segoe UI', 16),
        'bg': bg,
        'fg': 'white',
        'width': 6,
        'height': 2,
        'bd': 0,
        'activebackground': active_bg,
        'command': lambda b=b: press(b)
    }

# ------------------ Button Display ------------------
for row in buttons:
    row_frame = tk.Frame(frame, bg="#0f0f0f")
    row_frame.pack(pady=4)
    for b in row:
        tk.Button(row_frame, **format_btn(b)).pack(side="left", padx=4)

# ------------------ Run ------------------
window.mainloop()
