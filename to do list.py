import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful To-Do List App")
        self.root.configure(bg="black")

        self.tasks = []
        self.task_vars = []

        style = ThemedStyle(root)
        style.set_theme("radiance")  # You can change the theme to your preference
        style.configure("TFrame", background="black")

        # Entry widget for adding tasks
        entry_frame = ttk.Frame(root, style="TFrame")
        entry_frame.pack(pady=10)
        entry_label = ttk.Label(entry_frame, text="Add Task:", background="black", foreground="green")
        entry_label.grid(row=0, column=0, padx=5)
        entry_entry = ttk.Entry(entry_frame, width=30)
        entry_entry.grid(row=0, column=1, padx=5)
        add_button = ttk.Button(entry_frame, text="Add Task", command=lambda: self.add_task(entry_entry.get()), style="TButton")
        add_button.grid(row=0, column=2, padx=5)

        # Frame for task list
        task_frame = ttk.Frame(root, style="TFrame")
        task_frame.pack(pady=10)

        # Scrollbar and Listbox for displaying tasks
        scrollbar = ttk.Scrollbar(task_frame, orient=tk.VERTICAL)
        self.task_listbox = tk.Listbox(task_frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, width=40, height=10, bd=0, selectbackground="#a6a6a6", background="black", foreground="green")
        scrollbar.config(command=self.task_listbox.yview)
        self.task_listbox.grid(row=0, column=0)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Button to remove selected task
        remove_button = ttk.Button(root, text="Remove Selected Task", command=self.remove_task, style="TButton")
        remove_button.pack(pady=5)

        # Set the style for the checkbutton
        style.configure("TCheckbutton", background="black", foreground="green")

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            var = tk.StringVar(value=task)
            self.task_vars.append(var)
            checkbox = ttk.Checkbutton(self.task_listbox, text=task, variable=var, onvalue=task, offvalue="", command=lambda t=task: self.toggle_strike(t), style="TCheckbutton")
            checkbox.grid(sticky="w")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
            del self.task_vars[task_index]
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def toggle_strike(self, task):
        task_index = self.tasks.index(task)
        if self.task_vars[task_index].get():
            self.task_listbox.itemconfig(task_index, {'fg': 'gray', 'font': ('Helvetica', 10, 'strikethrough')})
        else:
            self.task_listbox.itemconfig(task_index, {'fg': 'green', 'font': ('Helvetica', 10)})


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
