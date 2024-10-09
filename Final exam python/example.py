import tkinter as tk


class TempatureConverter:

    def __init__(self, master):
        self.master = master
        self.instructions_window = tk.Toplevel()
        self.master.title("Tempature Converter")

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack(pady=10)

        tk.Label(self.instructions_window, text="Instructions").pack(padx=30)
        tk.Label(self.instructions_window,
                 text="1. Enter your temperature").pack(pady=10, padx=30)
        tk.Label(self.instructions_window,
                 text="2. Select the temperature scale you want to convert to"
                 ).pack(padx=30)

        self.temp_input = tk.Entry(self.master)
        self.temp_input.pack(pady=10, padx=30)

        self.new_temp = tk.Label(self.master,
                                 text="Your tempature will appear here")
        self.new_temp.pack()

        self.convert_f = tk.Button(self.buttons_frame,
                                   text="Fahrenheit",
                                   command=self.do_convert_f)
        self.convert_f.pack(side=tk.LEFT, padx=5)

        self.convert_c = tk.Button(self.buttons_frame,
                                   text="Celcius",
                                   command=self.do_convert_c)
        self.convert_c.pack(side=tk.LEFT, padx=5)

        self.reset = tk.Button(self.buttons_frame,
                               text="Reset",
                               command=self.do_reset)
        self.reset.pack(side=tk.LEFT, padx=5)

    def do_convert_f(self):
        if not self.validate_input():
            self.new_temp.config(text="Input must be a valid number")
        else:
            f_temp = (9 / 5) * int(self.temp_input.get()) + 32
            self.new_temp.config(text=str(f_temp) + "ºF")

    def do_convert_c(self):

        if not self.validate_input():
            self.new_temp.config(text="Input must be a valid number")
        else:
            c_temp = (int(self.temp_input.get()) - 32) * (5 / 9)
            self.new_temp.config(text=str(c_temp) + "ºC")

    def do_reset(self):
        self.temp_input.delete(0, 'end')

    def validate_input(self):
        txt = self.temp_input.get()

        return txt != '' and txt.lstrip('-').isnumeric()


if __name__ == "__main__":
    root = tk.Tk()
    game = TempatureConverter(root)
    root.mainloop()
