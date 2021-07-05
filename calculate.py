import tkinter as tk

# This function simply deletes all the text in the text_bar and inserts the result.
def calculate(math_operation, text_bar):
	
	result = eval(math_operation)
	text_bar.delete("1.0", tk.END)
	text_bar.insert(tk.END, result)



