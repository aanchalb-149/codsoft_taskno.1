import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        self.root.config(bg="white")

        self.tasks = []

        # Title Label
        self.label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="white")
        self.label.pack(pady=10)

        # Entry box
        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        # Add button
        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=self.add_task)
        self.add_button.pack(pady=5)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), height=10, selectbackground="lightblue")
        self.task_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Button frame
        self.button_frame = tk.Frame(root, bg="white")
        self.button_frame.pack(pady=5)

        self.remove_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=0, column=0, padx=10)

        self.complete_button = tk.Button(self.button_frame, text="Mark Completed", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            if not task.endswith(" ✔"):
                self.task_listbox.delete(index)
                task += " ✔"
                self.task_listbox.insert(index, task)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()