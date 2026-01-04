import tkinter as tk
from config import THEMES

class SettingsTab(tk.Frame):
    """Вкладка 2: Налаштування"""
    def __init__(self, parent, theme_callback, current_theme): 
        super().__init__(parent, padx=20, pady=20)
        self.theme_callback = theme_callback
        
        lbl = tk.Label(self, text="INTERFACE THEME:", font=("Arial", 12, "bold"))
        lbl.pack(anchor="w", pady=(0, 10))
        self.var_theme = tk.StringVar(value=current_theme) 

        themes = [("Default (Light)", "Default"), ("Dark night", "Dark night"), ("Blue Lagoon", "Blue Lagoon"), ("Hacker", "Hacker"), ("Mint Tea", "Mint Tea"), ("Dark Cherry", "Dark Cherry"), ("Lavender Haze", "Lavender Haze"), ("Vintage Leather", "Vintage Leather"), ("Cappuccino", "Cappuccino"), ("Terminal", "Terminal"), ("Morning Tide", "Morning Tide"), ("Toxic Teal", "Toxic Teal"), ("Northern Lights", "Northern Lights")]
        for text, val in themes:
            rb = tk.Radiobutton(self, text=text, variable=self.var_theme, value=val, command=self.apply_theme_selection)
            rb.pack(anchor="w", pady=2)

    def apply_theme_selection(self):
        selected = self.var_theme.get()
        self.theme_callback(selected)
    
    def update_theme_colors(self, theme):
        colors = THEMES[theme]
        self.configure(bg=colors["bg"])
        for widget in self.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=colors["bg"], fg=colors["fg"])
            elif isinstance(widget, tk.Radiobutton):
                widget.configure(bg=colors["bg"], fg=colors["fg"], selectcolor=colors["bg"])