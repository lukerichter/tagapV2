import datetime
import tkinter as tk
from tkinter import filedialog

from utils.evaluation import evaluate
from utils.io import read_file, write_file, create_pattern_table
from utils.tables import test_and_prepare_table
from utils.ui_strings import *

f_types = [("CSV", "*.csv")]

b_x = 372
b_width = 20
b_height = 2
element_bg = "#111111"
element_fg = "#bbbbbb"


def run_gui():
    GUI().run()


class GUI:

    def __init__(self):
        self.data = None
        self.target_file = None
        self.test_date = None

        self.root = tk.Tk()
        self.set_window_settings()
        self.text_output = self.add_output_field()
        self.upload_button = self.add_upload_button()
        self.date_input = self.add_date_input()
        self.date_submit = self.add_date_submit()
        self.save_button = self.add_save_button()
        self.save_pattern_button = self.add_save_pattern_button()

        self.write_textbox(first_message, True)

    def run(self):
        self.root.mainloop()

    def set_window_settings(self):
        self.root.resizable(height=False, width=False)
        self.root.title("TAG Test - GUI")
        self.root.geometry("540x304")
        self.root.config(bg="#1F1F1F")

    # GUI elements --------------------------------------------------

    def add_output_field(self):
        text_box = tk.Text(self.root, height=8, width=32, state="disabled", padx=20, pady=20, wrap="word",
                           bg=element_bg, fg=element_fg, borderwidth=0, spacing1=10, font=12)
        text_box.place(x=20, y=20)
        return text_box

    def add_upload_button(self):
        button_upload = tk.Button(self.root, command=self.upload_file, width=b_width, height=b_height,
                                  bg=element_bg, fg=element_fg, borderwidth=0, text=button_text_open_file)
        button_upload.place(x=b_x, y=20)
        return button_upload

    def add_date_input(self):
        input_date = tk.Text(self.root, width=b_width // 2, height=1, bg=element_bg, fg=element_fg, borderwidth=0,
                             padx=10, pady=11)
        input_date.place(x=b_x, y=70)
        return input_date

    def add_date_submit(self):
        input_date_submit = tk.Button(self.root, command=self.get_date, width=4, height=2,
                                      bg=element_bg, fg=element_fg, borderwidth=0, text=button_text_submit_date)
        input_date_submit.place(x=b_x + 110, y=70)
        return input_date_submit

    def add_save_button(self):
        button_download = tk.Button(self.root, command=self.save_file, width=b_width, height=b_height,
                                    text=button_text_save_file, bg=element_bg, fg=element_fg, borderwidth=0,
                                    state="disabled")
        button_download.place(x=b_x, y=120)
        return button_download

    def add_save_pattern_button(self):
        button_download_pattern = tk.Button(self.root, command=self.download_pattern, width=b_width, height=b_height,
                                            bg="#111", fg=element_fg, borderwidth=0, text=button_text_pattern)
        button_download_pattern.place(x=b_x, y=247)
        return button_download_pattern

    # Button functions --------------------------------------------

    def get_date(self):
        raw_date = self.date_input.get("1.0", "end").strip()

        # Determine the date format: 'mm/dd/yyyy' or 'dd.mm.yyyy', but also 'mm/dd/yy' or 'dd.mm.yy'
        if '/' in raw_date:
            date_format = '%m/%d/%Y' if max([len(x) for x in raw_date.split('/')]) == 4 else '%d/%m/%y'
        else:
            date_format = '%d.%m.%Y' if max([len(x) for x in raw_date.split('.')]) == 4 else '%d.%m.%y'

        try:
            self.test_date = datetime.datetime.strptime(raw_date.strip(), date_format)
            print(raw_date, "->", self.test_date)
            self.write_textbox(download_message, True)
        except ValueError:
            self.test_date = None
            print("Invalid date format")
            self.write_textbox(date_error_message, True)

        self.check_save_button()

    def upload_file(self):
        file_name = filedialog.askopenfilename(filetypes=f_types)

        data = read_file(file_name)
        errors = test_and_prepare_table(data)
        if errors:
            self.date_submit.config(state="disabled")
            self.data = None
            self.write_textbox(error_head_message(len(errors)), True)
            for error in errors:
                self.write_textbox(str(error), False)
        else:
            self.date_submit.config(state="normal")
            self.data = data
            self.write_textbox(date_message, True)

        self.check_save_button()

    def save_file(self):
        default_name = f"Auswertung_TAG_{str(self.test_date.year)}"
        file_io = filedialog.asksaveasfile(filetypes=f_types, defaultextension=".csv", initialfile=default_name)
        if file_io is not None:
            self.target_file = file_io.name
            self.run_evaluation()
            self.write_textbox(download_success_message, True)

    def download_pattern(self):
        file = filedialog.asksaveasfile(filetypes=f_types, defaultextension=".csv", initialfile="Vorlage_TAG")
        create_pattern_table(file.name)
        self.write_textbox(pattern_message, True)

    # Helper functions -------------------------------------------\

    def run_evaluation(self):
        data = evaluate(self.data, self.test_date)
        write_file(self.target_file, data)

    def check_save_button(self):
        if self.data is not None and self.test_date is not None:
            self.save_button.config(state="normal")
        else:
            self.save_button.config(state="disabled")

    def write_textbox(self, mes, replace):
        self.text_output.config(state="normal")
        if replace:
            self.text_output.delete("1.0", "end")
        self.text_output.insert("end", mes + "\n")
        self.text_output.config(state="disabled")
