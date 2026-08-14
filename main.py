import tkinter as tk
from tkinter import filedialog, font
import webbrowser
import random
import ast


data_list = []
data_read = []
# File handling
def createFile(data):
    newfile = filedialog.asksaveasfilename(
        defaultextension='.SS',
        filetypes=[('SS', '*.SS')]
    )

    if newfile:
        with open(newfile, "w") as file:
            file.write(str(data))


def folder():
    global data_read

    chosefile = filedialog.askopenfilename(
        title='Choose a SS File',
        filetypes=[('SS', '*.SS')]
    )

    if chosefile:
        with open(chosefile, 'r') as f:
            data_read = ast.literal_eval(f.read())

        print("Loaded:", data_read)


def open_new_window():
    def save_and_reset(entry, status_label):
        user_input = entry.get()

        if user_input.strip():
            data_list.append(user_input)
            print("Current List:", data_list)

            status_label.config(
                text=f"Added: '{user_input}' (Total items: {len(data_list)})"
            )

        entry.delete(0, tk.END)

    new_win = tk.Toplevel(root)
    new_win.title("New Class")
    new_win.geometry("350x250")
    new_win.configure(bg="#98C1D9")

    my_entry = tk.Entry(new_win, width=25)
    my_entry.pack(pady=10)

    status_label = tk.Label(new_win, bg="#98C1D9")
    status_label.pack(pady=5)

    submit_btn = tk.Button(new_win, text="Add to List", command=lambda: save_and_reset(my_entry, status_label))
    submit_btn.pack(pady=5)

    save_btn = tk.Button(new_win, text="Save to File", command=lambda: createFile(data_list))
    save_btn.pack(pady=5)

def chooseRandom():
    if data_read:
        test = random.randint(0, len(data_read) - 1)
        print(data_read[test])
        print(test)

def opengithub():
    webbrowser.open_new("https://github.com/Cheesidibb1/StudentSplitter")
root = tk.Tk()
root.geometry("500x400")
root.title("Student Splitter")
root.configure(background="#98C1D9")
helvetica = font.Font(family="Helvetica", size=14, weight="bold")

# Menu
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=folder)
filemenu.add_command(label="New", command=open_new_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=opengithub)

title = tk.Label(root, text="Student Splitter", fg ="#931621", bg="#98C1D9", font=("helvetica", 14, "bold"))
title.pack()
# tools
chosevlntr = tk.Label(root, text="Volunteer", bg="#98C1D9")
chosevlntr.pack()
choose = button = tk.Button(root, text="Choose", command=chooseRandom)
choose.pack()


root.mainloop()