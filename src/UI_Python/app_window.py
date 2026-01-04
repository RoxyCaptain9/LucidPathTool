import tkinter as tk
from tkinter import ttk
import json
import os
from UI_Python.instruction_tab import InstructionTab
from UI_Python.search_tab import SearchTab
from UI_Python.settings_tab import SettingsTab
from UI_Python.terms_tab import TermsPage
from config import THEMES



class AppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("LucidPathTool v1.0")
        self.root.geometry("900x600")
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.current_theme = self.load_settings()
        self.search_page = SearchTab(self.notebook)
        self.settings_page = SettingsTab(self.notebook, self.change_theme, self.current_theme)
        self.instruction_page = InstructionTab(self.notebook)
        self.terms_page = TermsPage(self.notebook)
        self.notebook.add(self.search_page, text=" Search ")
        self.notebook.add(self.settings_page, text=" Settings ")
        self.notebook.add(self.instruction_page, text=" Instruction ")
        self.notebook.add(self.terms_page, text=" Terms ")
        self.change_theme(self.current_theme)

    def load_settings(self):
        try:
            if os.path.exists("settings.json"):
                with open("settings.json", "r") as f:
                    data = json.load(f)
                    saved_theme = data.get("theme", "Default")
                    if saved_theme in THEMES:
                        return saved_theme
                    else:
                        return "Default"
        except Exception:
            pass
        return "Default"

    def save_settings(self, theme):
        try:
            with open("settings.json", "w") as f:
                json.dump({"theme": theme}, f)
        except Exception as e:
            print(f"Не вдалося зберегти налаштування: {e}")

    def change_theme(self, theme_name):
        self.search_page.update_theme_colors(theme_name)
        self.settings_page.update_theme_colors(theme_name)
        self.instruction_page.update_theme_colors(theme_name)
        self.terms_page.update_theme_colors(theme_name)
        self.save_settings(theme_name)