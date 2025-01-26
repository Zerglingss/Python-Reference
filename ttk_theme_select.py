import tkinter as tk
from tkinter import ttk

class ThemeTesterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Theme Tester")
        self.geometry("400x300")

        # Initialize the style
        self.style = ttk.Style(self)

        # Configure menu
        self.configure_menu()

        # Add widgets for testing
        self.add_widgets()

        # List available themes
        print("Available themes:", self.style.theme_names())

    def configure_menu(self):
        menubar = tk.Menu(self)
        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Default", command=lambda: self.change_theme("default"))
        theme_menu.add_command(label="Classic", command=lambda: self.change_theme("classic"))

        # Add ttk themes
        for theme in self.style.theme_names():
            theme_menu.add_command(label=theme, command=lambda t=theme: self.change_theme(t))

        menubar.add_cascade(label="Themes", menu=theme_menu)
        self.config(menu=menubar)

    def change_theme(self, theme):
        try:
            self.style.theme_use(theme)
            print(f"Switched to theme: {theme}")
        except tk.TclError as e:
            print(f"Failed to switch to theme '{theme}': {e}")

    def add_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Test Label").pack(pady=5)
        ttk.Button(frame, text="Test Button").pack(pady=5)
        ttk.Checkbutton(frame, text="Test Checkbutton").pack(pady=5)

        entry = ttk.Entry(frame)
        entry.insert(0, "Test Entry")
        entry.pack(pady=5)

        combobox = ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"])
        combobox.set("Test Combobox")
        combobox.pack(pady=5)

        grid_buttons = ttk.Frame(self, padding=10)
        grid_row_one = ttk.Frame(grid_buttons, padding=10)
        ttk.Button(grid_row_one, text="Test Button").pack(pady=5, side='left')
        ttk.Button(grid_row_one, text="Test Button").pack(pady=5, side='left')
        ttk.Button(grid_row_one, text="Test Button").pack(pady=5, side='left')
        grid_row_one.pack()
        grid_buttons.pack()


if __name__ == "__main__":
    app = ThemeTesterApp()
    app.mainloop()
