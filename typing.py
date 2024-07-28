import tkinter as tk
import keyboard
from time import time, sleep
from threading import Thread

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Monitor")
        self.label = tk.Label(root, text="Typing Speed: 0 cps", font=("Helvetica", 24))
        self.label.pack(pady=20)
        self.chars_typed = 0
        self.start_time = time()
        self.update_speed()
        self.listen_for_keys()

    def update_speed(self):
        elapsed_time = time() - self.start_time
        cps = self.chars_typed / elapsed_time if elapsed_time > 0 else 0
        self.label.config(text=f"Typing Speed: {cps:.2f} cps")
        self.root.after(1000, self.update_speed)

    def listen_for_keys(self):
        def on_key_event(event):
            self.chars_typed += 1

        keyboard.on_press(on_key_event)
        thread = Thread(target=keyboard.wait)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
