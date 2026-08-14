import tkinter as tk
from tkinter import filedialog, font, simpledialog, messagebox
import webbrowser
import random
import ast


data_list = []
data_read = []

# -------------------------
# File handling
# -------------------------

def folder():
    global data_read

    chosefile = filedialog.askopenfilename(
        title="Choose a SS File",
        filetypes=[("SS", "*.SS")]
    )

    if chosefile:
        with open(chosefile, "r") as f:
            data_read = ast.literal_eval(f.read())

        print("Loaded:", data_read)


def createFile(data):
    newfile = filedialog.asksaveasfilename(
        defaultextension=".SS",
        filetypes=[("SS", "*.SS")]
    )

    if newfile:
        with open(newfile, "w") as file:
            file.write(str(data))


# -------------------------
# New class
# -------------------------

def open_new_window():

    def save_and_reset():
        user_input = my_entry.get()

        if user_input.strip():
            data_list.append(user_input)

            status_label.config(
                text=f"Added: '{user_input}' "
                     f"(Total items: {len(data_list)})"
            )

        my_entry.delete(0, tk.END)

    new_win = tk.Toplevel(root)
    new_win.title("New Class")
    new_win.geometry("350x250")
    new_win.configure(bg="#98C1D9")


    my_entry = tk.Entry(new_win, width=25)
    my_entry.pack(pady=10)

    status_label = tk.Label(
        new_win,
        bg="#98C1D9"
    )
    status_label.pack(pady=5)

    submit_btn = tk.Button(
        new_win,
        text="Add to List",
        command=save_and_reset
    )
    submit_btn.pack(pady=5)

    save_btn = tk.Button(
        new_win,
        text="Save to File",
        command=lambda: createFile(data_list)
    )
    save_btn.pack(pady=5)


# -------------------------
# Split groups
# -------------------------

def split_groups():

    if not data_read:
        print("No students loaded!")
        return

    num_groups = simpledialog.askinteger(
        "Split Groups",
        f"How many groups?\n\n"
        f"Students loaded: {len(data_read)}",
        minvalue=1,
        maxvalue=len(data_read)
    )

    if num_groups is None:
        return

    students = data_read.copy()

    # Randomize the students
    random.shuffle(students)

    # Create empty groups
    groups = [[] for _ in range(num_groups)]

    # Distribute students evenly
    for i, student in enumerate(students):
        groups[i % num_groups].append(student)

    # Display results
    show_groups(groups)


# -------------------------
# Display groups
# -------------------------

def show_groups(groups):

    group_window = tk.Toplevel(root)
    group_window.title("Groups")
    group_window.geometry("500x500")
    group_window.configure(bg="#98C1D9")



    title = tk.Label(
        group_window,
        text="Student Groups",
        font=("Helvetica", 18, "bold"),
        bg="#98C1D9"
    )
    title.pack(pady=10)

    for i, group in enumerate(groups):

        group_frame = tk.Frame(
            group_window,
            bg="white",
            padx=10,
            pady=5
        )

        group_frame.pack(
            fill="x",
            padx=20,
            pady=5
        )

        group_title = tk.Label(
            group_frame,
            text=f"Group {i + 1} ({len(group)} students)",
            font=("Helvetica", 13, "bold"),
            bg="white"
        )

        group_title.pack(anchor="w")

        for student in group:

            student_label = tk.Label(
                group_frame,
                text=f"• {student}",
                bg="white",
                font=("Helvetica", 11)
            )

            student_label.pack(anchor="w")


# -------------------------
# Random student
# -------------------------

def chooseRandom():
    if not data_read:
        print("No students loaded!")
        return

    # Create the window
    random_window = tk.Toplevel(root)
    random_window.title("Voluntolding")
    random_window.geometry("350x200")
    random_window.configure(bg="#98C1D9")

    title = tk.Label(
        random_window,
        text="Random Student",
        font=("Helvetica", 18, "bold"),
        bg="#98C1D9"
    )
    title.pack(pady=15)

    student_label = tk.Label(
        random_window,
        text=random.choice(data_read),
        font=("Helvetica", 20, "bold"),
        bg="#98C1D9",
        fg="#931621"
    )
    student_label.pack(pady=15)

    def choose_again():
        student_label.config(
            text=random.choice(data_read)
        )

    again_button = tk.Button(
        random_window,
        text="Choose Again",
        command=choose_again
    )
    again_button.pack(pady=10)

# -------------------------
# GitHub
# -------------------------

def opengithub():
    webbrowser.open_new(
        "https://github.com/Cheesidibb1/Student-Splitter"
    )


# -------------------------
# Main window
# -------------------------

root = tk.Tk()

root.geometry("500x400")
root.title("Student Splitter")
root.configure(background="#98C1D9")



helvetica = font.Font(
    family="Helvetica",
    size=14,
    weight="bold"
)


# Menu

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)

menu.add_cascade(
    label="File",
    menu=filemenu
)

filemenu.add_command(
    label="Open...",
    command=folder
)

filemenu.add_command(
    label="New",
    command=open_new_window
)

filemenu.add_separator()

filemenu.add_command(
    label="Exit",
    command=root.quit
)


helpmenu = tk.Menu(menu)

menu.add_cascade(
    label="Help",
    menu=helpmenu
)

helpmenu.add_command(
    label="About",
    command=opengithub
)


# Title

title = tk.Label(
    root,
    text="Student Splitter",
    fg="#931621",
    bg="#98C1D9",
    font=("Helvetica", 14, "bold")
)

title.pack(pady=10)


# Buttons

choose_button = tk.Button(
    root,
    text="Choose Random Student",
    command=chooseRandom
)

choose_button.pack(pady=5)


split_button = tk.Button(
    root,
    text="Split Into Groups",
    command=split_groups
)

split_button.pack(pady=5)


root.mainloop()
