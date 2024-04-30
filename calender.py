import tkinter as tk
import calendar


# Function to display calendar
def DisplayCalendar():
    newRoot = tk.Tk()
    newRoot.title('Calendar Screen')
    newRoot.config(bg='light blue')
    newRoot.geometry('700x700')
    actualyear = int(yearEntry.get())
    calendarContent = calendar.calendar(actualyear)
    lblNew = tk.Label(newRoot, text=calendarContent, font='Consolas 10 bold')
    lblNew.grid(row=0, column=0, padx=30, pady=30)
    newRoot.mainloop()


def display_holidays():
    year = int(yearEntry.get())
    holidays = [
        (1, 1),   # New Year's Day
        (7, 4),   # Independence Day
        (12, 25), # Christmas Day
        (1, 26),  # Republic Day
        (8, 15)   # Independence Day
    ]

    root = tk.Tk()
    root.title(f"Holidays in {year}")

    cal = calendar.Calendar()
    holidays_in_year = [date for date in cal.itermonthdates(year, 1) if date.month == 1 and date.weekday() < 5]

    for holiday in holidays_in_year:
        if (holiday.day, holiday.month) in holidays:
            label = tk.Label(root, text="Holiday", fg="red")
        else:
            label = tk.Label(root, text="Working Day", fg="green")
        label.pack()

    root.mainloop()


# Designing first window
root = tk.Tk()
root.config(bg='deep sky blue')
root.title('Calendar App')
root.geometry("400x400")

header = tk.Label(root,
                  text='CALENDAR',
                  bg='light pink',
                  fg='brown',
                  font=('times', 32, 'bold'))
header.grid(row=0, column=0, padx=25, pady=25)

lbl = tk.Label(root, text='Enter the year: ')
lbl.grid(row=1, column=0, padx=25)

yearEntry = tk.Entry(root, width=5)
yearEntry.grid(row=2, column=0, padx=25, pady=10)

showcalendar = tk.Button(root,
                         text='Show Calendar',
                         fg='dark green',
                         command=DisplayCalendar)
showcalendar.grid(row=3, column=0, padx=25)
holiday = tk.Button(root, text='Holiday', fg='red', command=display_holidays)
holiday.grid(row=4, column=0, padx=30)
exitButton = tk.Button(root, text='Exit', fg='purple', command=root.destroy)
exitButton.grid(row=5, column=0, padx=25)
root.mainloop()
