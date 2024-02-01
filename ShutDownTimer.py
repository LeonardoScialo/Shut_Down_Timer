from tkinter import *
import time as tm
from tkinter import messagebox
from threading import *
import os
import sys


def resource_path(relative_path):
    base_path = getattr(sys,
                        '_MEIPASS',
                        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class CountDown:
    def __init__(self, _):
        # Tkinter window settings
        self.window = root
        self.window.geometry("400x400+0+0")
        self.window.title("Shut-Down Timer")
        self.window.configure(bg="#000")
        self.window.resizable(False, False)
        self.screen_icon = PhotoImage(file=resource_path("clock-7-64-png.png"))

        self.window.iconphoto(False, self.screen_icon)

        # Variable to pause countdown time
        self.pause = False

        # Start and pause buttons frame
        self.button_frame = Frame(self.window,
                                  bg="#000",
                                  width=380, height=200)
        self.button_frame.place(x=10, y=80)

        # CountDown Timer frame
        self.time_frame = Frame(self.window,
                                bg="#000",
                                width=380, height=100)
        self.time_frame.place(x=10, y=290)

        # Current time clock
        Label(self.window,
              font="arial 15 bold",
              text="current time:",
              bg="#000", fg="#fff").place(x=90, y=70)

        self.current_time = Label(self.window,
                                  font="arial 15 bold",
                                  text="",
                                  fg="#000", bg="#fff")
        self.current_time.place(x=220, y=70)
        self.clock()

        # Hour, minute, and second labels
        time_label = Label(self.window,
                           text="Timer",
                           font="arial 30 bold",
                           bg="#000", fg="#ea3548")
        time_label.place(x=140, y=10)

        hour_label = Label(self.window,
                           text="Hour",
                           font="arial 15",
                           bg="#000", fg="#fff")
        hour_label.place(x=105, y=200)

        minute_label = Label(self.window,
                             text="Min",
                             font="arial 15",
                             bg="#000", fg="#fff")
        minute_label.place(x=225, y=200)

        second_label = Label(self.window,
                             text="Sec",
                             font="arial 15",
                             bg="#000", fg="#fff")
        second_label.place(x=345, y=200)

        # Tkinter Check Buttons
        # sleep
        self.sleep_down = IntVar(value=1)
        self.sleep_check = Checkbutton(root,
                                       text="Sleep",
                                       variable=self.sleep_down,
                                       command=self.shut_down_uncheck,
                                       bg="#000", fg="#fff", bd=0, selectcolor='#ea3548',
                                       activebackground="#000", activeforeground="#fff",
                                       onvalue=1, offvalue=0,
                                       padx=3, pady=3)
        self.sleep_check.place(x=120, y=250)

        # shut down
        self.shut_down = IntVar()
        self.shut_down_check = Checkbutton(root,
                                           text="Shut Down",
                                           variable=self.shut_down,
                                           command=self.sleep_uncheck,
                                           bg="#000", fg="#fff", bd=0, selectcolor='#ea3548',
                                           activebackground="#000", activeforeground="#fff",
                                           onvalue=1, offvalue=0,
                                           padx=3, pady=3)
        self.shut_down_check.place(x=200, y=250)

        # Tkinter Entry Boxes
        # Entry for hours
        self.hour = StringVar()
        self.hour_entry = Entry(root,
                                textvariable=self.hour,
                                width=2,
                                font="arial 50",
                                bg="#000", fg="#fff", bd=0)
        self.hour_entry.place(x=30, y=155)
        self.hour_entry.bind("<FocusIn>", self.hours_Callback)
        self.hour.set("00")

        self.minutes = StringVar()
        self.minutes_entry = Entry(root,
                                   width=2,
                                   textvariable=self.minutes,
                                   font="arial 50",
                                   bg="#000", fg="#fff", bd=0)
        self.minutes_entry.place(x=150, y=155)
        self.minutes_entry.bind("<FocusIn>", self.minutes_Callback)
        self.minutes.set("00")

        self.seconds = StringVar()
        self.seconds_entry = Entry(root,
                                   width=2,
                                   textvariable=self.seconds,
                                   font="arial 50",
                                   bg="#000", fg="#fff", bd=0)
        self.seconds_entry.place(x=270, y=155)
        self.seconds_entry.bind("<FocusIn>", self.seconds_Callback)
        self.seconds.set("00")

        # Tkinter Buttons
        # Cancel button
        cancel_button = Button(self.window,
                               text="Exit",
                               bg="#ea3548", bd=0, fg="#fff",
                               width=12, height=3,
                               font="arial 10 bold",
                               command=self.Cancel)
        cancel_button.place(x=278, y=325)

        # Start button
        start_button = Button(self.window,
                              text="Start",
                              bg="#ea3548", bd=0, fg="#fff",
                              width=12, height=3,
                              font="arial 10 bold",
                              command=self.Get_Time)
        start_button.place(x=20, y=325)

        # Pause button
        pause_button = Button(self.window,
                              text="Pause",
                              bg="#ea3548", bd=0, fg="#fff",
                              width=12, height=3,
                              font="arial 10 bold",
                              command=self.pause_time)
        pause_button.place(x=149, y=325)

        # Additional
        self.time_display = None
        self.time_left = None
        self.x = None
        self.pause_variable = 0

    def hours_Callback(self, _):
        self.hour_entry.selection_range(0, END)

    def minutes_Callback(self, _):
        self.minutes_entry.selection_range(0, END)

    def seconds_Callback(self, _):
        self.seconds_entry.selection_range(0, END)

    def shut_down_uncheck(self):
        if self.sleep_down.get() == 1:
            self.shut_down_check.deselect()
        elif self.sleep_down.get() == 0:
            self.shut_down_check.select()

    def sleep_uncheck(self):
        if self.shut_down.get() == 1:
            self.sleep_check.deselect()
        elif self.shut_down.get() == 0:
            self.sleep_check.select()

    def Cancel(self):
        self.pause = True
        self.window.destroy()

    def clock(self):
        clock_time = tm.strftime('%H:%M:%S')
        self.current_time.config(text=clock_time, bg="#000", fg="#fff")
        self.current_time.after(1000, self.clock)

    def pause_time(self):
        print("pausing")

        self.pause = True

        mins, secs = divmod(self.time_left, 60)
        hours = 0
        if mins > 60:
            # hour minute
            hours, mins = divmod(mins, 60)

        self.time_display.config(text=f"Time Left: {hours}: {mins}: {secs}")
        self.time_display.update()

    def Get_Time(self):
        self.time_display = Label(self.time_frame,
                                  font="ariel 20 bold",
                                  bg="blue", fg="red")
        self.time_display.place(x=130, y=210)
        try:
            if self.hour_entry.get() == "":
                self.hour.set("00")
            if self.minutes_entry.get() == "":
                self.minutes.set("00")
            if self.seconds_entry.get() == "":
                self.seconds.set("00")
            # Convert total amount of time in seconds
            h = (int(self.hour_entry.get()) * 3600)
            m = (int(self.minutes_entry.get()) * 60)
            s = (int(self.seconds_entry.get()))
            self.time_left = h + m + s

            # If time is set to all 0's give a warning message
            if s == 0 and m == 0 and h == 0:
                messagebox.showwarning('Warning!', 'Please select a valid time')
            else:
                self.Threading()
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")

    def Threading(self):
        self.x = Thread(target=self.start_time, daemon=True)
        self.x.start()

    def start_time(self):
        self.pause = False

        while self.time_left > -1:
            mins, secs = (self.time_left // 60, self.time_left % 60)

            hrs = 0
            if mins > 60:
                hrs, mins = (mins // 60, mins % 60)

            self.seconds.set(f"{secs:02}")
            self.minutes.set(f"{mins:02}")
            self.hour.set(f"{hrs:02}")

            self.window.update()
            self.window.after(1000)

            self.time_left -= 1

            if self.time_left == 0:
                print("Timer Over")
                if self.sleep_down.get() == 1:
                    os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")
                elif self.shut_down.get() == 1:
                    os.system("shutdown /s /t 1")

            if self.pause:
                break


if __name__ == "__main__":
    root = Tk()
    # Creating a CountDown class object
    obj = CountDown(root)
    root.mainloop()
