import tkinter as tk
from calculate import calculate

SCREEN = tk.Tk()
SCREEN.geometry("300x500")


text_bar = tk.Text(SCREEN, height=5, width=20)
text_bar.place(y=20, x=80)
math_operation = ''
text_bar.insert(tk.END, math_operation)
			

def get_the_math_operation(text):

	global math_operation
	math_operation += text
	text_bar.insert(tk.END, text)


def clear_command():

	index_number = round(1+(len(text_bar.get("1.0", tk.END)))*0.1 - 0.2, 1)
	text_bar.delete(str(index_number))


def create_number_buttons():

	number_0 = tk.Button(text=str(0), height=3, width=10, bg='red', command=lambda:get_the_math_operation('0'))
	number_0.place(y=440)

	number_1 = tk.Button(text=str(1), height=3, width=10, bg='red', command=lambda:get_the_math_operation('1'))
	number_1.place(y=400)

	number_2 = tk.Button(text=str(2), height=3, width=10, bg='red', command=lambda:get_the_math_operation('2'))
	number_2.place(y=400, x=100)

	number_3 = tk.Button(text=str(3), height=3, width=10, bg='red', command=lambda:get_the_math_operation('3'))
	number_3.place(y=400, x=200)

	number_4 = tk.Button(text=str(4), height=3, width=10, bg='red', command=lambda:get_the_math_operation('4'))
	number_4.place(y=360)

	number_5 = tk.Button(text=str(5), height=3, width=10, bg='red', command=lambda:get_the_math_operation('5'))
	number_5.place(y=360, x=100)

	number_6 = tk.Button(text=str(6), height=3, width=10, bg='red', command=lambda:get_the_math_operation('6'))
	number_6.place(y=360, x=200)

	number_7 = tk.Button(text=str(7), height=3, width=10, bg='red', command=lambda:get_the_math_operation('7'))
	number_7.place(y=320)

	number_8 = tk.Button(text=str(8), height=3, width=10, bg='red', command=lambda:get_the_math_operation('8'))
	number_8.place(y=320, x=100)

	number_9 = tk.Button(text=str(9), height=3, width=10, bg='red', command=lambda:get_the_math_operation('9'))
	number_9.place(y=320, x=200)

	

if __name__ == '__main__':

	create_number_buttons()
	create_operation_sign_buttons()



def create_operation_sign_buttons():

	dot = tk.Button(text=str('.'), height=3, width=10, bg='red', command=lambda:get_the_math_operation('.'))
	dot.place(y=440, x=100)

	equal = tk.Button(text=str('='), height=3, width=10, bg='blue', command=lambda:calculate(text_bar.get('1.0',tk.END), text_bar))
	equal.place(y=440, x=200)

	add = tk.Button(text='+', height=3, width=10, bg='gray', command=lambda:get_the_math_operation('+'))
	add.place(y=275)

	subtract = tk.Button(text='-', height=3, width=10, bg='gray', command=lambda:get_the_math_operation('-'))
	subtract.place(y=275, x=100)

	multiply = tk.Button(text='x', height=3, width=10, bg='gray', command=lambda:get_the_math_operation('*'))
	multiply.place(y=275, x=200)

	divide = tk.Button(text='/', height=3, width=10, bg='gray', command=lambda:get_the_math_operation('/'))
	divide.place(y=235)

	second_power = tk.Button(text='**', height=3, width=10, bg='gray', command=lambda:get_the_math_operation('**'))
	second_power.place(y=235, x=100)

	clear = tk.Button(text='clear', height=3, width=10, bg='gray', command=lambda:clear_command())
	clear.place(y=235, x=200)

	SCREEN.mainloop()


