import tkinter as tk
from tkinter import ttk
import threading
from backend_interface import run_backend_search
from config import THEMES

class SearchTab(tk.Frame):
    """Вкладка 1: Головна сторінка пошуку"""
    def __init__(self, parent):
        super().__init__(parent)
        
        #Панель вводу
        top_frame = tk.Frame(self, pady=10, padx=10)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        
        tk.Label(top_frame, text="Folder:").pack(side=tk.LEFT)
        self.entry_path = tk.Entry(top_frame, width=30)
        self.entry_path.insert(0, "C:/Windows/Fonts")
        self.entry_path.pack(side=tk.LEFT, padx=5)
        self.add_context_menu(self.entry_path)
        
        tk.Label(top_frame, text="Name:").pack(side=tk.LEFT)
        self.entry_query = tk.Entry(top_frame, width=20)
        self.entry_query.insert(0, "arial")
        self.entry_query.pack(side=tk.LEFT, padx=5)
        self.add_context_menu(self.entry_query)
        self.btn_search = ttk.Button(top_frame, text=" SEARCH ", command=self.start_search)
        self.btn_search.pack(side=tk.LEFT, padx=10)

        #Футер
        self.footer_frame = tk.Frame(self)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=15, pady=(5, 10))
        self.status_label = tk.Label(self.footer_frame, text="Done ", anchor="w", relief=tk.FLAT)
        self.status_label.pack(side=tk.LEFT)

        self.author_label = tk.Label(self.footer_frame, text="made by @RoxyCaptain9", font=("Arial", 9, "italic"))
        self.author_label.pack(side=tk.RIGHT)

        #Таблиця виводу
        table_container = tk.Frame(self)
        table_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=15, pady=0)

        columns = ("name", "path", "size")
        self.tree = ttk.Treeview(table_container, columns=columns, show="headings")
        self.tree.heading("name", text="File name")
        self.tree.heading("path", text="Path")
        self.tree.heading("size", text="Size")
        self.tree.column("name", width=150)
        self.tree.column("path", width=400)
        self.tree.column("size", width=100)
        
        self.scrollbar = ttk.Scrollbar(table_container, orient=tk.VERTICAL, command=self.tree.yview)

        def toggle_scroll(first, last):
            self.scrollbar.set(first, last)
            if float(first) <= 0.0 and float(last) >= 1.0:
                self.scrollbar.pack_forget()
            else:
                self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.configure(yscroll=toggle_scroll)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree.bind("<Button-3>", self.show_tree_menu)

    def show_tree_menu(self, event):
        item_id = self.tree.identify_row(event.y)
        if item_id:
            self.tree.selection_set(item_id)
            menu = tk.Menu(self, tearoff=0)
            menu.add_command(label="Copy path", command=lambda: self.copy_path(item_id))
            menu.post(event.x_root, event.y_root)

    def copy_path(self, item_id):
        values = self.tree.item(item_id, 'values')
        if values:
            path = values[1]
            self.clipboard_clear()
            self.clipboard_append(path)
            self.update()

    def add_context_menu(self, widget):
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="Copy", command=lambda: widget.event_generate("<<Copy>>"))
        menu.add_command(label="Paste", command=lambda: widget.event_generate("<<Paste>>"))
        menu.add_command(label="Cut", command=lambda: widget.event_generate("<<Cut>>"))

        def show_menu(event):
            widget.focus()
            menu.post(event.x_root, event.y_root)
        widget.bind("<Button-3>", show_menu)

    def start_search(self):
        path = self.entry_path.get()
        query = self.entry_query.get()
        self.status_label.config(text="Searching ... beep beep")
        threading.Thread(target=self._run_search, args=(path, query), daemon=True).start()

    def _run_search(self, path, query):
        data = run_backend_search(path, query)
        self.tree.delete(*self.tree.get_children())
        for file in data:
            self.tree.insert("", tk.END, values=(file['name'], file['path'], file['size']))
        self.status_label.config(text=f"Found: {len(data)}")

    def update_theme_colors(self, theme):
        colors = THEMES[theme]
        self.configure(bg=colors["bg"])
        self.footer_frame.configure(bg=colors["bg"])
        self.status_label.configure(bg=colors["bg"], fg=colors["fg"])
        self.author_label.configure(bg=colors["bg"], fg=colors["footer_fg"])


        for widget in self.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.footer_frame:
                widget.configure(bg=colors["bg"])
                for child in widget.winfo_children():
                     if isinstance(child, tk.Label):
                        child.configure(bg=colors["bg"], fg=colors["fg"])
                     elif isinstance(child, tk.Entry):
                        child.configure(
                            bg=colors["entry_bg"], 
                            fg=colors["entry_fg"], 
                            insertbackground=colors["insert_bg"])

        style = ttk.Style()
        style.theme_use('clam') 

        style.layout('TButton', [
            ('Button.border', {'sticky': 'nswe', 'border': '1', 'children': [
                ('Button.padding', {'sticky': 'nswe', 'children': [
                    ('Button.label', {'sticky': 'nswe'})
                ]})
            ]})
        ])

        style.layout("TNotebook.Tab", [
            ('Notebook.tab', {'sticky': 'nswe', 'children': [
                ('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children': [
                    ('Notebook.label', {'side': 'top', 'sticky': ''})
                ]})
            ]})
        ])

        style.configure("Treeview", 
                        background=colors["tree_bg"], 
                        foreground=colors["tree_fg"], 
                        fieldbackground=colors["tree_bg"],
                        rowheight=25,
                        bordercolor=colors["bg"],
                        lightcolor=colors["bg"],
                        darkcolor=colors["bg"])
        
        style.configure("Treeview.Heading",
                        background=colors["bg"], 
                        foreground=colors["fg"], 
                        relief="flat")
        
        style.map("Treeview",
            background=[('selected', colors['select_bg'])],
            foreground=[('selected', colors['select_fg'])])
        
        style.map("Treeview.Heading",
            background=[('active', colors['bg'])], 
            foreground=[('active', colors['fg'])])

        style.configure("TButton",
                        background=colors["btn_bg"], 
                        foreground=colors["btn_fg"], 
                        bordercolor=colors["bg"], 
                        lightcolor=colors["btn_bg"], 
                        darkcolor=colors["btn_bg"])
        
        style.map("TButton",
                  background=[('active', colors['btn_active']), ('pressed', colors['btn_pressed'])],
                  foreground=[('active', colors['btn_fg'])])
