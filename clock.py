from tkinter import Label,Tk
import time

app_windows = Tk()
app_windows.title("Digital Clock")
app_windows.geometry("400x200")
app_windows.resizable(0,0)
app_windows.configure(bg="black")

text_font = ("Boulder",36,"italic")
background = "black"
foreground = "yellow"
border_width = 20


label = Label(app_windows,font=text_font,bg=background,fg=foreground)
label.grid(row=0,column=1,padx=border_width,pady=10)

date_label = Label(app_windows,font=text_font,bg=background,fg=foreground)

date_label.grid(row=1,column=1,padx=border_width,pady=10)

def clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)

    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)

    label.after(200,clock)
    


clock()

app_windows.mainloop()