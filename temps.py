#lab 10
#kyle mcmahon
#this is a program that uses a gui to show a user their celcius temps converted into
#farenheit 

import tkinter

#creating the class and module definitions
class celtoferGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create the two widgets for the top frame.
        self.cel_label = tkinter.Label(self.top_frame, \
                                    text='Enter the temperature (in C):')
        self.cel_entry = tkinter.Entry(self.top_frame, \
                                        width=10)
        self.fer_label = tkinter.Label(self.top_frame, \
                                text='The temperature in fahrenheit:')

        # Assign the top frame's widgets to a grid position
        self.cel_label.grid(row=1,column=1)
        self.cel_entry.grid(row=1,column=2)
        self.fer_label.grid(row=3,column=1)
        
        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, \
                                          text='Calculate', \
                                          command=self.calcCTF)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The calcCTF method is a callback function for
    # the Calculate button

    def calcCTF(self):
        # Get the value entered by the  user in the
        # celcius entry field
        cel = float(self.cel_entry.get())

        # Calculate from celcius to farenheit
        ctf = 9 / 5 * cel + 32

        # Display the result in an info dialog box.
        self.result_label = tkinter.Label(self.top_frame, \
                                text=str( ctf))
        # Display the result as a label on the grid.
        self.result_label.grid(row=3,column=2)
    
# Create an instance of the celtoferGUI class.
ctf_conv = celtoferGUI()
