import tkinter as tk
import random
import pyttsx3
from plyer import notification
import pyperclip

# Compliments list
compliments = [
    "You're doing amazing, sweetie! 🌟",
    "You are stronger than you think 💪",
    "You’re a gift to this world 🎁",
    "Your smile can light up a room 😄",
    "You code like a pro 👩‍💻",
    "You are beautifully, wonderfully made 💖",
    "You're sunshine mixed with a little bit of hurricane ☀️🌪️",
    "Your energy is infectious 🔥",
    "You're proof that magic exists ✨",
    "You're a masterpiece in progress 🎨"
]

# Colors for background
bg_colors = ["#FFEBEF", "#E0F7FA", "#FFF3E0", "#E8F5E9", "#F3E5F5"]

# Text-to-speech engine
engine = pyttsx3.init()

# Main App
root = tk.Tk()
root.title("💌 Compliment Me!")
root.geometry("400x300")
root.configure(bg=random.choice(bg_colors))

compliment_label = tk.Label(root, text="Click to receive love 💖", font=("Helvetica", 14), wraplength=350, bg=root["bg"])
compliment_label.pack(pady=40)

def generate_compliment():
    compliment = random.choice(compliments)
    compliment_label.config(text=compliment)

    # Notification
    notification.notify(
        title="💌 Compliment for You!",
        message=compliment,
        timeout=4
    )

def copy_compliment():
    text = compliment_label.cget("text")
    pyperclip.copy(text)
    copy_label.config(text="📋 Copied!")

# Buttons
button = tk.Button(root, text="💖 Get Compliment 💖", font=("Helvetica", 12, "bold"), command=generate_compliment, bg="#FFCDD2")
button.pack(pady=10)

copy_btn = tk.Button(root, text="📋 Copy Compliment", font=("Helvetica", 10), command=copy_compliment, bg="#E1BEE7")
copy_btn.pack(pady=5)

copy_label = tk.Label(root, text="", font=("Helvetica", 9), bg=root["bg"])
copy_label.pack()

# Footer
footer = tk.Label(root, text="Made with 💕 by You", font=("Helvetica", 8), bg=root["bg"])
footer.pack(side="bottom", pady=10)

root.mainloop()
