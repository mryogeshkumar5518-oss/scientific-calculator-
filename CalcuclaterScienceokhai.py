from tkinter import *
import math
import tkinter.messagebox

# ==========================================================================================================================
root = Tk()
root.title("Scientific Calculator")
root.resizable(width=False, height=False)
root.geometry("400x490+400+40")

MainFrame = Frame(root, pady=2, relief=RIDGE)
MainFrame.grid()

calFrame = Frame(MainFrame, bd=20, padx=5, pady=2, relief=RIDGE)
calFrame.grid()

# =========================================================================================================================
class Calc:
    def __init__(self):
        self.total = 0
        self.current = "0"
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def display(self, value):
        txtResult.delete(0, END)
        txtResult.insert(0, value)

    def EnterNumber(self, num):
        self.result = False
        firstnum = txtResult.get()
        secondnum = str(num)

        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.' and '.' in firstnum:
                return
            self.current = firstnum + secondnum
        self.display(self.current)
#===============================================================================================================
    def sumTotal(self):
        self.result = True
        self.current = float(txtResult.get())

        if self.check_sum:
            self.validFunction()
        else:
            self.total = float(txtResult.get())
        self.display(self.total)

#================================================================================================================





#===============================================================================================================
    def validFunction(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "sub":
            self.total -= self.current
        elif self.op == "mult":
            self.total *= self.current
        elif self.op == "divide":
            self.total /= self.current
        elif self.op == "mod":
            self.total %= self.current

        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.validFunction()
        else:
            self.total = self.current
        self.op = op
        self.input_value = True
        self.check_sum = True

    def clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display("0")
        self.input_value = True

    def all_clear_Entry(self):
        self.clear_Entry()
        self.total = 0

    def mathsPM(self):
        self.current = -(float(txtResult.get()))
        self.display(self.current)

    def Log(self):
        self.current = math.log(float(txtResult.get()))
        self.display(self.current)

    def exp(self):
        self.current = math.exp(float(txtResult.get()))
        self.display(self.current)

    def tau(self):
        self.current = math.tau(float(txtResult.get()))
        self.display(self.current)

    def pi(self):
        self.current = math.pi(float(txtResult.get()))
        self.display(self.current)

    def sqrt(self):
        self.current = math.sqrt(float(txtResult.get()))
        self.display(self.current)

    def e(self):
        self.current = math.e(float(txtResult.get()))                
        self.display(self.current)

    def degrees(self):
        self.current = math.degrees(float(txtResult.get()))
        self.display(self.current)

    def acos(self):
        self.current = math.acos(float(txtResult.get()))
        self.display(self.current)

    def asin(self):
        self.current = math.asin(float(txtResult.get()))
        self.display(self.current)

    def atan(self):
        self.current = math.atan(float(txtResult.get()))
        self.display(self.current)

    def Log2(self):
        self.current = math.log2(float(txtResult.get()))
        self.display(self.current)

    def Lgamma(self):
        self.current = math.lgamma(float(txtResult.get()))
        self.display(self.current)

    def Log10(self):
        self.current = math.log10(float(txtResult.get()))
        self.display(self.current)

    def cos(self):
        self.current = math.cos(math.radians(float(txtResult.get())))
        self.display(self.current)

    def cosh(self):
        self.current = math.cosh(math.radians(float(txtResult.get())))
        self.display(self.current)

    def tan(self):
        self.current = math.tan(math.radians(float(txtResult.get())))
        self.display(self.current)

    def tanh(self):
        self.current = math.tanh(math.radians(float(txtResult.get())))
        self.display(self.current)

    def sin(self):
        self.current = math.sin(math.radians(float(txtResult.get())))
        self.display(self.current)

    def sinh(self):
        self.current = math.sinh(math.radians(float(txtResult.get())))
        self.display(self.current)
#=========================================================================================================================
    def mod(self):
        self.operation("mod")

    def backspace(self):
        num = txtResult.get()
        if len(num) > 1:
            new_num = num[:-1]
        else:
            new_num = "0"
        self.current = new_num
        self.display(new_num)

# =========================================================================================================================
added_value = Calc()

txtResult = Entry(calFrame, font=('arial', 16, 'bold'), bg="cadetblue", bd=30,
            width=28, justify=RIGHT)
txtResult.grid(row=0, column=0, columnspan=10, pady=1)
txtResult.insert(0, "0")

# =========================================================================================================================
numberpad = "789456123"
i = 0
btn = []

for j in range(2, 5):
    for q in range(3):
        btn.append(
            Button(
                calFrame,
                width=6,
                height=2,
                font=("arial", 16, "bold"),
                bd=4,
                activebackground="green",
                activeforeground="white",
                text=numberpad[i],
                command=lambda x=numberpad[i]: added_value.EnterNumber(x),
            )
        )
        btn[i].grid(row=j, column=q, pady=1)
        i += 1

# =========================================================================================================================
Button(calFrame, text="÷", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=lambda: added_value.operation("divide")).grid(row=5, column=3)

Button(calFrame, text="0", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=lambda: added_value.EnterNumber("0")).grid(row=5, column=0)

Button(calFrame, text="×", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=lambda: added_value.operation("mult")).grid(row=4, column=3)

Button(calFrame, text="-", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=lambda: added_value.operation("sub")).grid(row=3, column=3)

Button(calFrame, text=".", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=lambda: added_value.EnterNumber(".")).grid(row=5, column=1)

Button(calFrame, text="+", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=lambda: added_value.operation("add")).grid(row=2, column=3)

Button(calFrame, text="CE", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=added_value.clear_Entry).grid(row=1, column=1)

Button(calFrame, text="C", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=added_value.all_clear_Entry).grid(row=1, column=2)

Button(calFrame, text="=", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=added_value.sumTotal).grid(row=5, column=2)

Button(calFrame, text="←", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=added_value.backspace).grid(row=1, column=0)

Button(calFrame, text="±", width=6, height=2, font=('arial', 16, 'bold'),
       bd=4,activebackground='green',activeforeground='white', command=added_value.mathsPM).grid(row=1, column=3)

# ========================================Scientific Buttons=========================================================================

Button(calFrame, text="sin", width=6, height=2,font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.sin).grid(row=1, column=4)

Button(calFrame, text="cos", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.cos).grid(row=1, column=5)

Button(calFrame, text="tan", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.tan).grid(row=1, column=6)

Button(calFrame, text="π", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.pi).grid(row=1, column=7)

Button(calFrame, text="sin⁻¹", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.asin).grid(row=2, column=4)

Button(calFrame, text="cos⁻¹", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.acos).grid(row=2, column=5)

Button(calFrame, text="tan⁻¹", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.atan).grid(row=2, column=6)

Button(calFrame, text="2π", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.tau).grid(row=2, column=7)

Button(calFrame, text="e", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.e).grid(row=3, column=4)

Button(calFrame, text="√", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.sqrt).grid(row=3, column=5)

Button(calFrame, text="%", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.mod).grid(row=3, column=6)

Button(calFrame, text="Log", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.Log).grid(row=3, column=7)

Button(calFrame, text="EXP", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.exp).grid(row=4, column=4)

Button(calFrame, text="DEG", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.degrees).grid(row=4, column=5)

Button(calFrame, text="Lgamma", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.Lgamma).grid(row=4, column=6)

Button(calFrame, text="Log2", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.Log2).grid(row=4, column=7)

Button(calFrame, text="sinh", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.sinh).grid(row=5, column=4)

Button(calFrame, text="cosh", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.cosh).grid(row=5, column=5)

Button(calFrame, text="tanh", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.tanh).grid(row=5, column=6)

Button(calFrame, text="Log10", width=6, height=2, font=('arial', 16, 'bold'), bd=4,activebackground='green',activeforeground='white',
       command=added_value.Log10).grid(row=5, column=7)
#==========================================================================================================================

scientific_buttons = calFrame.grid_slaves()
scientific_buttons = [btn for btn in scientific_buttons if int(btn.grid_info()['column']) >= 4]
#==============================================================================================================================

#================================================================================================================================

#=========================================================================================================================
scientific_buttons = []
for widget in calFrame.winfo_children():
    info = widget.grid_info()
    if 'column' in info and int(info['column']) >= 4:
        scientific_buttons.append(widget)






# =========================================================================================================================
def iExit():
    if tkinter.messagebox.askyesno("Scientific Calculator", "Confirm exit?"):
        root.destroy()

def scientific():
    root.geometry("790x490+460+40")
    for btn in scientific_buttons:
        btn.grid()
        txtResult.config(width=56)

def standard():
    root.geometry("400x490+460+40")
    for btn in scientific_buttons:
        btn.grid_remove()
        txtResult.config(width=26)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=standard)
filemenu.add_command(label="Scientific", command=scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

root.config(menu=menubar)
root.mainloop()
