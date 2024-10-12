# Import tkinter (gui) and pillow to import images
import tkinter as tk
from PIL import Image, ImageTk


# Main class
class TempatureConverter:
    # Creates second window, sets title, adds images, adds instructions, adds buttons, and adds user input
    def __init__(self, master):

        # Creates second window and sets titles
        self.master = master
        self.instructions_window = tk.Toplevel()
        self.master.title("Tempature Converter")

        # Inserts Snowflake Image
        snowflake = Image.open("snowflake.jpg").resize((100, 100))
        snowflake = ImageTk.PhotoImage(snowflake)
        tk.Label(self.instructions_window, image=snowflake).pack()

        # Inserts Sun Image
        sun = Image.open("sun.jpg").resize((100, 100))
        sun = ImageTk.PhotoImage(sun)
        tk.Label(self.instructions_window, image=sun).pack()

        # Gives user instructions
        tk.Label(self.instructions_window, text="Instructions").pack(padx=30)
        tk.Label(self.instructions_window,
                 text="1. Enter your temperature").pack(pady=10, padx=30)
        tk.Label(self.instructions_window,
                 text="2. Select the temperature scale you want to convert to"
                 ).pack(padx=30)

        # Creates container for buttons
        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=10)

        # Creates input for temperature
        self.temp_input = tk.Entry(self.master)
        self.temp_input.pack(pady=10, padx=30)
        self.new_temp = tk.Label(self.master,
                                 text="Your tempature will appear here")
        self.new_temp.pack()

        # Creates fahrenheit button
        self.convert_f = tk.Button(self.buttons_frame,
                                   text="Fahrenheit",
                                   command=self.do_convert_f)
        self.convert_f.pack(side=tk.LEFT, padx=5)

        # Creates Celcius button
        self.convert_c = tk.Button(self.buttons_frame,
                                   text="Celcius",
                                   command=self.do_convert_c)
        self.convert_c.pack(side=tk.LEFT, padx=5)

        # Creates Reset Button
        self.reset = tk.Button(self.buttons_frame,
                               text="Reset",
                               command=self.do_reset)
        self.reset.pack(side=tk.LEFT, padx=5)

        self.instructions_window.mainloop()

# Converts tempature to Fahrenheit and conducts input validation

    def do_convert_f(self):

        # If input validation fails, shows error message
        if not self.validate_input():
            self.new_temp.config(text="Input must be a valid number")

        else:
            # Otherwise converts tempature and displays it
            f_temp = (9 / 5) * int(self.temp_input.get()) + 32
            self.new_temp.config(text=str(f_temp) + "ºF")

    # Converts tempature to Celcius and conducts input validation

    def do_convert_c(self):

        # If input validation fails, shows error message
        if not self.validate_input():
            self.new_temp.config(text="Input must be a valid number")

        else:

            # Otherwise converts tempature and displays it
            c_temp = (int(self.temp_input.get()) - 32) * (5 / 9)
            self.new_temp.config(text=str(c_temp) + "ºC")

# Resets user input

    def do_reset(self):
        self.temp_input.delete(0, 'end')

# Validates input by making sure its a valid number and not empty

    def validate_input(self):
        txt = self.temp_input.get()

        # Checks if the input is empty and removes the '-' since python treats it as non-numeric when it's there
        return txt != '' and txt.lstrip('-').isnumeric()

# Copied from example code
if __name__ == "__main__":
    root = tk.Tk()
    game = TempatureConverter(root)
    root.mainloop()
