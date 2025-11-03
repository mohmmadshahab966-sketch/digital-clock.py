# digital-clock.py
import tkinter as tk import time  def update_time():     current = time.strftime("%H:%M:%S")     label.config(text=current)     label.after(1000, update_time)  root = tk.Tk() root.title("⏰ Digital Clock") label = tk.Label(root, font=("Courier", 44), fg="#00ffff", bg="#000000") label.pack(padx=30, pady=30) update_time() root.mainloop()
