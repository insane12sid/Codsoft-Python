import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.task_label = tk.Label(self.root, text="Enter task:")
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(padx=10, pady=10)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            self.tasks.append(task_description)
            self.update_tasklist()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_tasklist()
            self.save_tasks()

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task = self.tasks[index]
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Task")

            edit_label = tk.Label(edit_window, text="Edit Task:")
            edit_label.pack(pady=10)

            edit_entry = tk.Entry(edit_window, width=40)
            edit_entry.insert(tk.END, task)
            edit_entry.pack()

            save_button = tk.Button(edit_window, text="Save Changes", command=lambda:self.save_edited_task(index, edit_entry.get(), edit_window))
            save_button.pack(pady=5)

    def save_edited_task(self, index, description, edit_window):
        self.tasks[index] = description
        self.update_tasklist()
        self.save_tasks()
        edit_window.destroy()
        
    def update_tasklist(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("todo_list.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("todo_list.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_tasklist()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

