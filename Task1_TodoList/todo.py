import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft To-Do List")
        self.root.geometry("450x550")
        self.root.resizable(False, False)

        # Define Colors and Fonts
        self.bg_color = "#f0f0f0"
        self.accent_color = "#4a90e2"
        self.text_color = "#333333"
        self.root.configure(bg=self.bg_color)
        
        # --- UI Header ---
        self.header_label = tk.Label(
            root, text="My Tasks", font=("Helvetica", 24, "bold"),
            bg=self.bg_color, fg=self.accent_color, pady=20
        )
        self.header_label.pack()

        # --- Entry Field for New Tasks ---
        self.task_entry = tk.Entry(
            root, font=("Helvetica", 14), width=30, 
            bd=0, highlightthickness=2, highlightbackground="#cccccc"
        )
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', lambda event: self.add_task()) # Press Enter to add

        # --- Buttons Frame ---
        btn_frame = tk.Frame(root, bg=self.bg_color)
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(
            btn_frame, text="Add Task", command=self.add_task,
            bg="#2ecc71", fg="white", font=("Helvetica", 10, "bold"),
            width=12, relief="flat", padx=5, pady=5
        )
        self.add_btn.grid(row=0, column=0, padx=5)

        self.update_btn = tk.Button(
            btn_frame, text="Update Selected", command=self.update_task,
            bg="#f1c40f", fg="white", font=("Helvetica", 10, "bold"),
            width=12, relief="flat", padx=5, pady=5
        )
        self.update_btn.grid(row=0, column=1, padx=5)

        # --- Listbox for Tasks ---
        self.tasks_listbox = tk.Listbox(
            root, font=("Helvetica", 12), width=45, height=12,
            selectmode=tk.SINGLE, bd=0, highlightthickness=1, 
            highlightbackground="#dddddd", activestyle='none'
        )
        self.tasks_listbox.pack(pady=10, padx=20)

        # Scrollbar for Listbox
        self.scrollbar = tk.Scrollbar(root)
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        # Position scrollbar manually if needed, or just pack it
        
        # --- Bottom Buttons ---
        bottom_frame = tk.Frame(root, bg=self.bg_color)
        bottom_frame.pack(pady=10)

        self.delete_btn = tk.Button(
            bottom_frame, text="Delete Task", command=self.delete_task,
            bg="#e74c3c", fg="white", font=("Helvetica", 10, "bold"),
            width=12, relief="flat", padx=5, pady=5
        )
        self.delete_btn.grid(row=0, column=0, padx=5)

        self.clear_btn = tk.Button(
            bottom_frame, text="Clear All", command=self.clear_all,
            bg="#95a5a6", fg="white", font=("Helvetica", 10, "bold"),
            width=12, relief="flat", padx=5, pady=5
        )
        self.clear_btn.grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            current_text = self.tasks_listbox.get(selected_task_index)
            
            # Simple prompt logic: If entry is empty, move listbox item to entry to edit
            new_task = self.task_entry.get()
            if new_task != "":
                self.tasks_listbox.delete(selected_task_index)
                self.tasks_listbox.insert(selected_task_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                # If entry is empty, put selected item into entry for editing convenience
                self.task_entry.insert(0, current_text)
                messagebox.showinfo("Info", "Task loaded into entry box. Edit it and click Update again.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
            self.tasks_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
