import tkinter as tk
from config import THEMES

class TermsPage(tk.Frame):
    """Вкладка 4: Правила"""
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=20)

        lbl = tk.Label(self, text="TERMS OF USE", font=("Arial", 14, "bold"))
        lbl.pack(pady=(0, 10))
        
        self.text_area = tk.Text(self, wrap=tk.WORD, height=20, padx=10, pady=10, font=("Consolas", 10))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        text = """1. GENERAL PROVISIONS.
This software (hereinafter referred to as the "Program") is provided to users free of charge for personal use. By downloading or using the Program, you automatically agree to these terms.

2. USAGE RESTRICTIONS.
Commercial Use: It is prohibited to sell, rent, or distribute copies of the Program for a fee without written permission from the author.
Code Interference: It is prohibited to decompile, modify the source code, or alter the structure of the Program.

3. DATA PRIVACY.
The Program operates exclusively locally (offline).
The Program does not collect, store, or transmit user personal data or file system information to third parties.
All search processes occur entirely on your device.

4. DISCLAIMER.
The product is provided on an "as is" basis, without any warranties.
The developer is not responsible for any system malfunctions, processor load during deep disk scanning or other consequences of using the Program.

5. FEEDBACK.
This is the first version of the product. In case of interface or functionality errors (bugs), it is recommended to contact support for their resolution in future updates."""

        self.text_area.insert(tk.END, text)
        self.text_area.configure(state=tk.DISABLED)

    def update_theme_colors(self, theme):
        colors = THEMES[theme]
        self.configure(bg=colors["bg"])
        self.text_area.configure(bg=colors["text_bg"], fg=colors["text_fg"])
        for widget in self.winfo_children():
             if isinstance(widget, tk.Label):
                widget.configure(bg=colors["bg"], fg=colors["fg"])
