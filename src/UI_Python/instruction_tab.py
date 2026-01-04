import tkinter as tk
from config import THEMES

class InstructionTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=20)

        lbl = tk.Label(self, text="USER MANUAL", font=("Arial", 14, "bold"))
        lbl.pack(pady=(0, 10))

        self.text_area = tk.Text(self, wrap=tk.WORD, height=20, padx=10, pady=10, font=("Consolas", 10))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        text = """1. Search Tab.
This is the main section for scanning the file system.

Folder Field: Specify the path to the directory where the search should be performed. Example: C:/Users/User/Downloads or D:/.

⚠️WARNING⚠️
 On devices with limited performance, it is NOT RECOMMENDED to specify the entire system drive (e.g., just C:/). This may lead to long scanning times and heavy system load.

Name Field: Enter a keyword, partial name, file extension, or number. The utility searches for all elements that fully or partially contain the entered query in their name.

Launch: Click the search button. Results will be displayed in the table below.

2. Settings Tab.
Section for changing the visual appearance of the program.
There are 13 interface themes available. Select the desired one from the list to change the color scheme.

3. Manual Tab.
You are currently viewing this tab. It contains instructions and recommendations for using the utility.

4. Terms of Use Tab.
Contains legal information, software terms of use, and disclaimer."""
        
        self.text_area.insert(tk.END, text)
        self.text_area.configure(state=tk.DISABLED)

    def update_theme_colors(self, theme):
        colors = THEMES[theme]
        self.configure(bg=colors["bg"])
        self.text_area.configure(bg=colors["text_bg"], fg=colors["text_fg"])
        for widget in self.winfo_children():
             if isinstance(widget, tk.Label):
                widget.configure(bg=colors["bg"], fg=colors["fg"])