import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.update_button = tk.Button(master, text="Update Status", command=self.update_status)
        self.update_button.pack()

        self.display_button = tk.Button(master, text="Display Tasks", command=self.display_tasks)
        self.display_button.pack()

    def add_task(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Task")

        name_label = tk.Label(add_window, text="Task Name:")
        name_label.grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)

        description_label = tk.Label(add_window, text="Task Description:")
        description_label.grid(row=1, column=0, padx=10, pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.grid(row=1, column=1, padx=10, pady=5)

        due_date_label = tk.Label(add_window, text="Due Date:")
        due_date_label.grid(row=2, column=0, padx=10, pady=5)
        due_date_entry = tk.Entry(add_window)
        due_date_entry.grid(row=2, column=1, padx=10, pady=5)

        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_task_to_list(name_entry.get(), description_entry.get(), due_date_entry.get(), add_window))
        add_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_task_to_list(self, name, description, due_date, add_window):
        task = Task(name, description, due_date)
        self.tasks.append(task)
        self.task_listbox.insert(tk.END, f"{task.name} - {task.description} - Due: {task.due_date} - Status: {task.status}")
        add_window.destroy()

    def update_status(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Error", "Please select a task to update.")
            return

        task = self.tasks[selected_index[0]]
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Status")

        status_label = tk.Label(update_window, text="Task Status:")
        status_label.grid(row=0, column=0, padx=10, pady=5)

        status_var = tk.StringVar()
        status_var.set(task.status)

        status_entry = tk.Entry(update_window, textvariable=status_var)
        status_entry.grid(row=0, column=1, padx=10, pady=5)

        update_button = tk.Button(update_window, text="Update", command=lambda: self.update_task_status(task, status_var.get(), update_window))
        update_button.grid(row=1, column=0, columnspan=2, pady=10)

    def update_task_status(self, task, status, update_window):
        task.status = status
        self.task_listbox.delete(0, tk.END)
        for t in self.tasks:
            self.task_listbox.insert(tk.END, f"{t.name} - {t.description} - Due: {t.due_date} - Status: {t.status}")
        update_window.destroy()

    def display_tasks(self):
        display_window = tk.Toplevel(self.master)
        display_window.title("Task List")

        if not self.tasks:
            message_label = tk.Label(display_window, text="No tasks available.")
            message_label.pack(pady=10)
        else:
            for task in self.tasks:
                task_label = tk.Label(display_window, text=f"{task.name} - {task.description} - Due: {task.due_date} - Status: {task.status}")
                task_label.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
