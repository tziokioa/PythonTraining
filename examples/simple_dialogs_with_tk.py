import tkinter
from tkinter import messagebox
from tkinter import simpledialog


# hide main window
root = tkinter.Tk()
root.withdraw()

# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")

messagebox.askokcancel("Title","The application will be closed")
messagebox.askyesno("Title","Do you want to save?")
messagebox.askretrycancel("Title","Installation failed, try again?")

userName = simpledialog.askstring(title="Title",prompt="What's your Name?:")
print("Hello", userName)
