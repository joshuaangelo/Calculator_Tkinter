from tkinter import *


root = Tk()
root.geometry('340x400')
root.title('Calculator')
root.resizable(FALSE, FALSE)


class Calc:
      def __init__(self, master):
            main_frame = Frame(master)
            main_frame.pack(pady=10, padx=10)

            btn_frame = Frame()
            btn_frame.pack(pady=5, padx=5)

            #Displays the input and output
            list_box = Listbox(main_frame, width=300, border=1, height=4)
            list_box.pack()

            btn_height = 4
            btn_width = 9
            font = ('normal', 11)

            #Buttons, Left to right
            btn_7 = Button(btn_frame, text='7', height=btn_height, 
                        width=btn_width, font=font)
            btn_7.grid(row=0, column=0)

            btn_8 = Button(btn_frame, text='8', height=btn_height,
                           width=btn_width, font=font)
            btn_8.grid(row=0, column=1)

            btn_9 = Button(btn_frame, text='9', height=btn_height,
                           width=btn_width, font=font)
            btn_9.grid(row=0, column=2)

            btn_divide = Button(btn_frame, text='÷',
                                height=btn_height, width=btn_width, font=font)
            btn_divide.grid(row=0, column=3)

            btn_4 = Button(btn_frame, text='4', height=btn_height,
                           width=btn_width, font=font)
            btn_4.grid(row=1, column=0)

            btn_5 = Button(btn_frame, text='5', height=btn_height,
                           width=btn_width, font=font)
            btn_5.grid(row=1, column=1)

            btn_6 = Button(btn_frame, text='6', height=btn_height,
                           width=btn_width, font=font)
            btn_6.grid(row=1, column=2)

            btn_multiply = Button(btn_frame, text='x',
                                  height=btn_height, width=btn_width, font=font)
            btn_multiply.grid(row=1, column=3)
            ##########
            btn_1 = Button(btn_frame, text='1', height=btn_height,
                           width=btn_width, font=font)
            btn_1.grid(row=2, column=0)

            btn_2 = Button(btn_frame, text='2', height=btn_height,
                           width=btn_width, font=font)
            btn_2.grid(row=2, column=1)

            btn_3 = Button(btn_frame, text='3', height=btn_height,
                           width=btn_width, font=font)
            btn_3.grid(row=2, column=2)

            btn_subtract = Button(btn_frame, text='-',
                                  height=btn_height, width=btn_width, font=font)
            btn_subtract.grid(row=2, column=3)
            ######
            btn_clear = Button(btn_frame, text='C',
                               height=btn_height, width=btn_width, font=font)
            btn_clear.grid(row=3, column=0)

            btn_0 = Button(btn_frame, text='0', height=btn_height,
                           width=btn_width, font=font)
            btn_0.grid(row=3, column=1)

            btn_dot = Button(btn_frame, text='.',
                             height=btn_height, width=btn_width, font=font)
            btn_dot.grid(row=3, column=2)

            btn_add = Button(btn_frame, text='+',
                             height=btn_height, width=btn_width, font=font)
            btn_add.grid(row=3, column=3)



c = Calc(root)
root.mainloop()