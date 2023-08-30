from tkinter import *

# created look of the calculator
root = Tk()
root.title("Calculator")
root.minsize(200,400)
# calculator answer box
entry = Entry(root, width="35")
entry.grid(row="0", column="0", columnspan="10", padx="10", pady="10")


# calculator all buttons
button_1 = Button(root, text="1", padx="20", pady="20")
button_2 = Button(root, text="2", padx="20", pady="20")
button_3 = Button(root, text="3", padx="20", pady="20")
button_4 = Button(root, text="4", padx="20", pady="20")

button_5 = Button(root, text="5", padx="20", pady="20")
button_6 = Button(root, text="6", padx="20", pady="20")
button_7 = Button(root, text="7", padx="20", pady="20")
button_8 = Button(root, text="8", padx="20", pady="20")

button_9 = Button(root, text="9", padx="20", pady="20")
button_0 = Button(root, text="0", padx="20", pady="20")
button_del = Button(root, text="C", padx="20", pady="20")
button_plus = Button(root, text="+", padx="20", pady="20")

button_minus = Button(root, text="-", padx="20", pady="20")
button_multiplication = Button(root, text="*", padx="20", pady="20")
button_division = Button(root, text="/", padx="20", pady="20")
button_answer = Button(root, text="=", padx="20", pady="20")

button_point = Button(root, text=".", padx="20", pady="20")

# calculator button design box
button_1.grid(row="1", column="0")
button_2.grid(row="1", column="1")
button_3.grid(row="1", column="2")
button_4.grid(row="1", column="3")

button_5.grid(row="2", column="0")
button_6.grid(row="2", column="1")
button_7.grid(row="2", column="2")
button_8.grid(row="2", column="3")

button_9.grid(row="3", column="0")
button_0.grid(row="3", column="1")
button_del.grid(row="3", column="2")
button_plus.grid(row="3", column="3")

button_minus.grid(row="4", column="0")
button_multiplication.grid(row="4", column="1")
button_division.grid(row="4", column="2")
button_answer.grid(row="4", column="3")

button_point.grid(row="5", column="0")

root.mainloop()