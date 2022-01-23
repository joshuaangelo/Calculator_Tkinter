from ast import Expression
from tkinter import *


root = Tk()
root.geometry('340x360')
root.title('Calculator')
root.resizable(FALSE, FALSE)


class Calc:
      def __init__(self, master):
            main_frame = Frame(master)
            main_frame.pack(pady=5, padx=10)

            btn_frame = Frame(master)
            btn_frame.pack(pady=2, padx=5)

            #Displays the input and output
            self.entry = Entry(main_frame, width=300, borderwidth=3) # to add font styles
            self.entry.pack()

            btn_height = 3
            btn_width = 8
            font = ('NORMAL', 11)
            pady = 4

            #Buttons, Left to right
            self.btn_7 = Button(btn_frame, text='7', height=btn_height, 
                        width=btn_width, font=font, command=lambda: self.click(7))
            self.btn_7.grid(row=0, column=0, pady=pady)

            self.btn_8 = Button(btn_frame, text='8', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(8))
            self.btn_8.grid(row=0, column=1, pady=pady)

            self.btn_9 = Button(btn_frame, text='9', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(9))
            self.btn_9.grid(row=0, column=2, pady=pady)

            self.btn_divide = Button(btn_frame, text='÷',height=btn_height, 
                                    width=btn_width, font=font, command=self.divide)
            self.btn_divide.grid(row=0, column=3, pady=pady)

            self.btn_4 = Button(btn_frame, text='4', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(4))
            self.btn_4.grid(row=1, column=0, pady=pady)

            self.btn_5 = Button(btn_frame, text='5', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(5))
            self.btn_5.grid(row=1, column=1, pady=pady)

            self.btn_6 = Button(btn_frame, text='6', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(6))
            self.btn_6.grid(row=1, column=2, pady=pady)

            self.btn_multiply = Button(btn_frame, text='x', height=btn_height, 
                                       width=btn_width, font=font, command=self.multiply)
            self.btn_multiply.grid(row=1, column=3, pady=pady)
      
            self.btn_1 = Button(btn_frame, text='1', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(1))
            self.btn_1.grid(row=2, column=0, pady=pady)

            self.btn_2 = Button(btn_frame, text='2', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(2))
            self.btn_2.grid(row=2, column=1, pady=pady)

            self.btn_3 = Button(btn_frame, text='3', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(3))
            self.btn_3.grid(row=2, column=2, pady=pady)

            self.btn_subtract = Button(btn_frame, text='-',
                                  height=btn_height, width=btn_width, font=font, command=self.subtract)
            self.btn_subtract.grid(row=2, column=3, pady=pady)
   
            self.btn_clear = Button(btn_frame, text='Clear',
                               height=btn_height, width=btn_width, font=font, command=self.clear)
            self.btn_clear.grid(row=3, column=0, pady=pady)

            self.btn_0 = Button(btn_frame, text='0', height=btn_height,
                                width=btn_width, font=font, command=lambda: self.click(0))
            self.btn_0.grid(row=3, column=1, pady=pady)

            self.btn_dot = Button(btn_frame, text='.',
                             height=btn_height, width=btn_width, font=font)
            self.btn_dot.grid(row=3, column=2, pady=pady)

            self.btn_add = Button(btn_frame, text='+',
                             height=btn_height, width=btn_width, font=font, command=self.adding)
            self.btn_add.grid(row=3, column=3, pady=pady)

            self.btn_equals = Button(btn_frame, text='=',
                             height=btn_height, width=40, font=font, command=self.equals)
            self.btn_equals.grid(row=4, columnspan=4, pady=pady)

      def clear(self):
            self.entry.delete(0, END)


      def click(self, event):
            if self.entry.get() == 'Can not divide by Zero': 
                  self.entry.delete(0, END)
            else:
                  self.current = self.entry.get()
                  self.entry.delete(0, END)
                  self.entry.insert(END, str(self.current) + str(event))

      
      def equals(self):
            second_number = self.entry.get()
            self.entry.delete(0, END)

            if operation == 'add':
                  self.entry.insert(0, f_num + int(second_number))
            elif operation == 'subtract':
                self.entry.insert(0, f_num - int(second_number))
            elif operation == 'divide':
                  try: #Try Zero division error
                      self.entry.insert(0, f_num / int(second_number))
                  except ZeroDivisionError:
                        self.entry.delete(0, END)
                        self.entry.insert(END, 'Can not divide by Zero')

            elif operation == 'multiply':
                      self.entry.insert(0, f_num * int(second_number))


      def adding(self): #Deletes current entry texts and saves it in a variable for later use
            first_number = self.entry.get()
            global f_num
            global operation
            operation = 'add'
            f_num = int(first_number)
            self.entry.delete(0, END)

      def subtract(self):
            first_number = self.entry.get()
            global f_num
            global operation
            operation = 'subtract'
            f_num = int(first_number)
            self.entry.delete(0, END)


      def divide(self):
            first_number = self.entry.get()
            global f_num
            global operation
            operation = 'divide'
            f_num = int(first_number)
            self.entry.delete(0, END)


      def multiply(self):
            first_number = self.entry.get()
            global f_num
            global operation
            operation = 'multiply'
            f_num = int(first_number)
            self.entry.delete(0, END)



c = Calc(root)
root.mainloop()