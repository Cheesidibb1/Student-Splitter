import tkinter as tk
from tkinter import filedialog, font
import webbrowser
import random
data_list = []
# File handling
def folder():
    chosefile = filedialog.askopenfilename(title='Choose a SS File', filetypes=[('SS', '*.SS')])
    print(chosefile)
    return chosefile

def createFile(data):
    newfile = filedialog.asksaveasfilename(defaultextension='.SS', filetypes=[('SS', '*.SS')])
    if newfile:
        with open(newfile, "w") as file:
            file.write(str(data))
    return None



def save_and_reset(event=None):
    user_input = my_entry.get()
    if user_input.strip():
        data_list.append(user_input)
        print("Current List:", data_list)


        status_label.config(text=f"Added: '{user_input}' (Total items: {len(data_list)})")

    # 3. Reset the entry box back to empty
    my_entry.delete(0, tk.END)

def opengithub():
    webbrowser.open_new("https://github.com/Cheesidibb1/StudentSplitter")
root = tk.Tk()
root.geometry("500x400")
root.title("Student Splitter")
root.configure(background="#98C1D9")
helvetica = font.Font(family="Helvetica", size=14, weight="bold")
menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=folder)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=opengithub)

title = tk.Label(root, text="Student Splitter", fg ="#931621", bg="#98C1D9", font=("helvetica", 14, "bold"))
title.pack()

my_entry = tk.Entry(root, width=25)
my_entry.pack(pady=10)

# Submit Button
submit_btn = tk.Button(root, text="Add to List", command=save_and_reset)
submit_btn.pack(pady=5)
submit_btn = tk.Button(root, text="save to file", command=lambda: createFile(data_list))
submit_btn.pack(pady=5)
# Status Label (to show visual feedback)
status_label = tk.Label(root)

root.mainloop()