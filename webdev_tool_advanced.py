import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import webbrowser
import threading
import time
import os

# Open links
def open_telegram():
    webbrowser.open("https://t.me/darkvaiadmin")

def open_website():
    webbrowser.open("https://serialkey.top/")

# Hacker Animation
def hacker_animation():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    while True:
        line = ''.join([chars[ord(c) % len(chars)] for c in str(time.time())[:10]])
        animation_label.config(text=line)
        time.sleep(0.2)

# Utility: Get current editor
def get_current_editor():
    tab = notebook.tab(notebook.select(), "text")
    if tab == "HTML": return html_editor
    elif tab == "CSS": return css_editor
    elif tab == "JavaScript": return js_editor
    elif tab == "PHP": return php_editor
    return None

# File Import (Open)
def import_file():
    editor = get_current_editor()
    if not editor:
        return
    path = filedialog.askopenfilename(
        title="Import File",
        filetypes=[
            ("All Supported", "*.html *.css *.js *.php"),
            ("HTML Files", "*.html"),
            ("CSS Files", "*.css"),
            ("JavaScript Files", "*.js"),
            ("PHP Files", "*.php"),
            ("All Files", "*.*")
        ]
    )
    if path:
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            editor.delete(1.0, tk.END)
            editor.insert(tk.END, content)
            messagebox.showinfo("Success", f"Loaded: {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")

# File Export (Save As)
def export_file():
    editor = get_current_editor()
    if not editor:
        return
    content = editor.get(1.0, tk.END).strip()
    if not content:
        messagebox.showwarning("Empty", "No content to save!")
        return

    tab = notebook.tab(notebook.select(), "text")
    ext = ".html" if tab == "HTML" else ".css" if tab == "CSS" else ".js" if tab == "JavaScript" else ".php"
    default_name = f"code{ext}"

    path = filedialog.asksaveasfilename(
        title="Export File",
        initialfile=default_name,
        defaultextension=ext,
        filetypes=[
            (f"{tab} File", f"*{ext}"),
            ("All Files", "*.*")
        ]
    )
    if path:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Saved", f"File saved successfully!\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")

# Clear Editor
def clear_editor():
    editor = get_current_editor()
    if editor:
        if messagebox.askyesno("Confirm", "Are you sure you want to clear this editor?"):
            editor.delete(1.0, tk.END)

# Copy All
def copy_all():
    editor = get_current_editor()
    if editor:
        content = editor.get(1.0, tk.END)
        root.clipboard_clear()
        root.clipboard_append(content)
        messagebox.showinfo("Copied", "All code copied to clipboard!")

# Paste
def paste_content():
    editor = get_current_editor()
    if editor:
        try:
            content = root.clipboard_get()
            editor.insert(tk.INSERT, content)
        except tk.TclError:
            messagebox.showwarning("Paste Error", "Clipboard is empty or not text.")

# Create main window
root = tk.Tk()
root.title("Advanced Web Dev Tools - darkboss1bd")
root.geometry("1100x750")
root.configure(bg="black")

# Hacker Animation Label
animation_label = tk.Label(
    root,
    text="",
    font=("Courier", 12, "bold"),
    fg="green",
    bg="black",
    anchor="nw",
    justify="left",
    wraplength=1080
)
animation_label.place(x=10, y=10, width=1080, height=20)

# Start animation thread
threading.Thread(target=hacker_animation, daemon=True).start()

# Banner
banner_frame = tk.Frame(root, bg="black")
banner_frame.pack(pady=10)

title_label = tk.Label(
    banner_frame,
    text="🔥 DARKBOSS1BD WEB DEVELOPMENT SUITE 🔥",
    font=("Consolas", 16, "bold"),
    fg="red",
    bg="black"
)
title_label.pack()

subtitle = tk.Label(
    banner_frame,
    text="Create Websites with HTML, CSS, JS, PHP | Fully Advanced Tool",
    font=("Courier", 10),
    fg="lightgreen",
    bg="black"
)
subtitle.pack()

# Links
link_frame = tk.Frame(root, bg="black")
link_frame.pack(pady=5)

tk.Label(link_frame, text="🔗 Contact & Links:", fg="white", bg="black", font=("Arial", 10)).pack()

btn_telegram = tk.Button(
    link_frame,
    text="💬 Telegram: @darkvaiadmin",
    command=open_telegram,
    bg="blue",
    fg="white",
    font=("Arial", 10),
    relief="flat",
    width=35
)
btn_telegram.pack(pady=2)

btn_website = tk.Button(
    link_frame,
    text="🌐 Website: serialkey.top",
    command=open_website,
    bg="purple",
    fg="white",
    font=("Arial", 10),
    relief="flat",
    width=35
)
btn_website.pack(pady=2)

# Toolbar
toolbar = tk.Frame(root, bg="black")
toolbar.pack(pady=5)

tk.Button(toolbar, text="📁 Import", command=import_file, bg="orange", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(toolbar, text="💾 Export", command=export_file, bg="green", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(toolbar, text="🧾 Clear", command=clear_editor, bg="red", fg="white", width=10).grid(row=0, column=2, padx=5)
tk.Button(toolbar, text="📋 Copy All", command=copy_all, bg="cyan", fg="black", width=10).grid(row=0, column=3, padx=5)
tk.Button(toolbar, text="📝 Paste", command=paste_content, bg="magenta", fg="white", width=10).grid(row=0, column=4, padx=5)

# Notebook (Tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=20, pady=10)

html_frame = tk.Frame(notebook, bg="black")
css_frame = tk.Frame(notebook, bg="black")
js_frame = tk.Frame(notebook, bg="black")
php_frame = tk.Frame(notebook, bg="black")

notebook.add(html_frame, text="HTML")
notebook.add(css_frame, text="CSS")
notebook.add(js_frame, text="JavaScript")
notebook.add(php_frame, text="PHP")

# Create editors
def create_editor(parent, lang):
    tk.Label(parent, text=f"Edit {lang} Code", font=("Consolas", 12), fg="cyan", bg="black").pack(pady=5)
    text_area = scrolledtext.ScrolledText(
        parent,
        wrap=tk.WORD,
        font=("Consolas", 11),
        bg="black",
        fg="white",
        insertbackground="white",
        selectbackground="gray",
        height=22
    )
    text_area.pack(fill="both", expand=True, padx=10, pady=5)
    text_area.insert("1.0", f"<!-- {lang} Code by darkboss1bd -->\n")
    if lang == "CSS":
        text_area.insert("end", "body {\n    background: #121212;\n    color: #0f0;\n}\n")
    elif lang == "JavaScript":
        text_area.insert("end", "console.log('Hacked by darkboss1bd!');\n")
    elif lang == "PHP":
        text_area.insert("end", "<?php\necho 'Secure PHP Engine';\n?>\n")
    return text_area

html_editor = create_editor(html_frame, "HTML")
css_editor = create_editor(css_frame, "CSS")
js_editor = create_editor(js_frame, "JavaScript")
php_editor = create_editor(php_frame, "PHP")

# Footer
footer = tk.Label(
    root,
    text="🔐 darkboss1bd | Advanced Web Tools | File I/O + Copy/Paste + Export/Import",
    font=("Arial", 10),
    fg="yellow",
    bg="black"
)
footer.pack(side="bottom", pady=10)

# Run
root.mainloop()