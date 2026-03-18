import tkinter as tk
import sys
import os
import time
import sys

def typing_effect(message, delay=0.05):
    """Print message with typing effect"""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

def on_yes():
    root.destroy()
    typing_effect("I always knew you liked me:)", delay=0.08)

def on_no_or_cancel():
    root.destroy()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def center_window(win, width, height):
    """Center the window on screen"""
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

def create_window():
    global root
    root = tk.Tk()
    root.title("A Simple Question ❤️")
    root.configure(bg="#f7f3f2")


    window_width, window_height = 400, 200
    center_window(root, window_width, window_height)


    label = tk.Label(
        root, 
        text="Do You Like Me?", 
        font=("Helvetica", 18, "bold"), 
        bg="#f7f3f2", 
        fg="#333"
    )
    label.pack(pady=30)

    frame = tk.Frame(root, bg="#f7f3f2")
    frame.pack(pady=10)

    btn_style = {"width": 12, "height": 2, "font": ("Helvetica", 10, "bold")}

    yes_btn = tk.Button(frame, text="Yes", bg="#4CAF50", fg="white",
                        activebackground="#45a049", **btn_style, command=on_yes)
    yes_btn.grid(row=0, column=0, padx=8)

    no_btn = tk.Button(frame, text="No", bg="#f44336", fg="white",
                       activebackground="#da190b", **btn_style, command=on_no_or_cancel)
    no_btn.grid(row=0, column=1, padx=8)

    cancel_btn = tk.Button(frame, text="Cancel", bg="#9E9E9E", fg="white",
                           activebackground="#7e7e7e", **btn_style, command=on_no_or_cancel)
    cancel_btn.grid(row=0, column=2, padx=8)

    root.mainloop()

if __name__ == "__main__":
    create_window()