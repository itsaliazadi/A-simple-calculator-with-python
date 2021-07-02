import tkinter as tk

def calculate(math_operation, text_bar):
	
	result = eval(math_operation)
	text_bar.delete("1.0", tk.END)
	text_bar.insert(tk.END, result)


print('Done')