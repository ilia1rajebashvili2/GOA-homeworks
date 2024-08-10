import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Drop-down Menu Example")

# Create a label
label = tk.Label(root, text="Select a Programming Language:")
label.pack(pady=10)

# Create a drop-down menu with 20 programming languages
programming_languages = [
    "Python", "JavaScript", "Java", "C#", "C++", "Ruby", "PHP", "Swift", "Go", "Kotlin",
    "TypeScript", "R", "Objective-C", "SQL", "Dart", "Scala", "Perl", "Haskell", "Rust", "MATLAB"
]

# Create the drop-down menu
selected_language = tk.StringVar()
selected_language.set("Select a language")  # Default value

dropdown = ttk.Combobox(root, textvariable=selected_language, values=programming_languages, state="readonly")
dropdown.pack(pady=10)

# Function to display selected language
def show_selection():
    selected = selected_language.get()
    print(f"Selected language: {selected}")

# Create a button to show the selected language
button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack(pady=10)

# Run the application
root.mainloop()
