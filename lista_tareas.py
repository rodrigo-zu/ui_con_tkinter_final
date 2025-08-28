import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x500")
        self.crear_widgets()
        self.configurar_layout()

    def crear_widgets(self):
        self.label_title = tk.Label(self.root, text="Mi Lista de Tareas", font=("Arial", 18))
        self.entry_task = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.btn_add = tk.Button(self.root, text="Agregar", font=("Arial", 12), command=self.agregar_tarea)

        # Frame con scroll
        self.frame_container = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.frame_container)
        self.scrollbar = tk.Scrollbar(self.frame_container, orient="vertical", command=self.canvas.yview)
        self.frame_tasks = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.frame_tasks, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.frame_tasks.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.entry_task.bind("<Return>", self.agregar_tarea)

    def configurar_layout(self):
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)
        self.entry_task.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.btn_add.grid(row=1, column=1, padx=10, pady=10)
        self.frame_container.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def agregar_tarea(self, event=None):
        tarea = self.entry_task.get()
        if tarea.strip() == "":
            messagebox.showwarning("Error", "La tarea no puede estar vacía")
        else:
            self.crear_widget_tarea(tarea)
            self.entry_task.delete(0, tk.END)

    def crear_widget_tarea(self, tarea_texto):
        tarea_frame = tk.Frame(self.frame_tasks, pady=5)
        tarea_frame.pack(fill="x")

        label = tk.Label(tarea_frame, text=tarea_texto, font=("Arial", 12))
        label.pack(side="left", padx=5)

        def completar():
            label.config(fg="gray", font=("Arial", 12, "overstrike"))
            tarea_frame.config(bg="#d3ffd3")

        btn_complete = tk.Button(tarea_frame, text="✔", command=completar)
        btn_complete.pack(side="right", padx=5)

        def eliminar():
            if messagebox.askyesno("Confirmar", "¿Eliminar esta tarea?"):
                tarea_frame.destroy()

        btn_delete = tk.Button(tarea_frame, text="❌", command=eliminar)
        btn_delete.pack(side="right", padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
