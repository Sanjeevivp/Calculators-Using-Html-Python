import tkinter as tk
import math

# ------------------ Function ------------------
def press(key):
    if key == '+/-':
        try:
            val = float(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(-val))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif key == '⌫':
        entry.delete(len(entry.get()) - 1)
    elif key == 'CE' or key == 'C':
        entry.delete(0, tk.END)
    elif key == '=':
        try:
            expression = entry.get().replace('×', '*').replace('÷', '/')
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif key == '1/x':
        try:
            result = str(1 / float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif key == 'x²':
        try:
            result = str(float(entry.get()) ** 2)
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif key == '√x':
        try:
            result = str(math.sqrt(float(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, key)

# ------------------ UI Setup ------------------
window = tk.Tk()
window.title("Windows Style Calculator")
window.geometry("400x500")
window.config(bg="#0f0f0f")
window.resizable(False, False)

# ------------------ Display ------------------
entry = tk.Entry(window, font=("Segoe UI", 24), bg="#1f1f1f", fg="white",
                 bd=0, insertbackground="white", justify='right')
entry.pack(fill="both", ipady=10, padx=20, pady=(20, 10))

# ------------------ Button Layout ------------------
buttons = [
    ['%', 'CE', 'C', '⌫'],
    ['1/x', 'x²', '√x', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['+/-', '0', '.', '=']
]

frame = tk.Frame(window, bg="#0f0f0f")
frame.pack(pady=5)

# ------------------ Button Design ------------------
def format_btn(b):
    # Assign custom colors for specific buttons
    if b == 'C':
        bg = '#d32f2f'            # Red
        active_bg = '#b71c1c'
    elif b == '⌫':
        bg = '#f0ad4e'            # Orange/Yellow
        active_bg = '#ec971f'
    else:
        bg = '#2f2f2f'            # Default dark grey
        active_bg = '#3f3f3f'

    return {
        'text': b,
        'font': ('Segoe UI', 18),
        'bg': bg,
        'fg': 'white',
        'width': 6,
        'height': 1,
        'bd': 0,
        'activebackground': active_bg,
        'command': lambda b=b: press(b)
    }

# ------------------ Button Display ------------------
for row in buttons:
    row_frame = tk.Frame(frame, bg="#0f0f0f")
    row_frame.pack(pady=6)
    for b in row:
        tk.Button(row_frame, **format_btn(b)).pack(side="left", padx=6)

# ------------------ Run ------------------
window.mainloop()
