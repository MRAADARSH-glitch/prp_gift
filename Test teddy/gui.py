import tkinter as tk
from PIL import Image, ImageTk
import random

click_count = 0

# Fireworks simulation (expanding circles)
def fireworks():
    for _ in range(50):
        x = random.randint(50, 450)
        y = random.randint(50, 250)
        size = random.randint(10, 40)
        color = random.choice(["red", "blue", "green", "yellow", "pink", "orange", "purple"])
        canvas.create_oval(x, y, x+size, y+size, outline=color, width=2)
    root.after(200, fireworks)

# Teddy bounce animation
def teddy_bounce(scale=150, step=0):
    global bear_img_tk
    if step < 6:
        new_size = scale + (20 if step % 2 == 0 else -20)
        resized = bear_img.resize((new_size, new_size))
        bear_img_tk = ImageTk.PhotoImage(resized)
        bear_label.config(image=bear_img_tk)
        root.after(150, lambda: teddy_bounce(scale, step+1))

# Function when NO is clicked
def on_no():
    global click_count
    click_count += 1
    if click_count < 5:
        plea_text.set("Plsss 🙏" * click_count)
        plea_label.config(font=("Arial", 14 + click_count*4, "bold"))
        # Shrink NO button gradually
        new_width = max(5, 10 - click_count*1)
        no_button.config(width=new_width)
    elif click_count == 5:
        no_button.pack_forget()  # remove the No button after 5th click

# Function when YES is clicked
def on_yes():
    plea_text.set("I Love You Sweetheart ❤️")
    plea_label.config(font=("Arial", 28, "bold"), fg="red")
    fireworks()
    teddy_bounce()

# Setup window
root = tk.Tk()
root.title("Proposal App")
root.geometry("500x600")

plea_text = tk.StringVar()
plea_text.set("Hey love, will you date me?")

plea_label = tk.Label(root, textvariable=plea_text, font=("Arial", 18, "bold"), wraplength=450, justify="center")
plea_label.pack(pady=20)

# Load teddy bear image (place a teddy.png in the same folder)
bear_img = Image.open("teddy.png")
bear_img_tk = ImageTk.PhotoImage(bear_img.resize((150, 150)))
bear_label = tk.Label(root, image=bear_img_tk)
bear_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

yes_button = tk.Button(button_frame, text="Yes 💕", font=("Arial", 14), bg="lightgreen", command=on_yes)
yes_button.grid(row=0, column=0, padx=20)

no_button = tk.Button(button_frame, text="No 🙈", font=("Arial", 14), bg="tomato", width=10, command=on_no)
no_button.grid(row=0, column=1, padx=20)

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=10)

root.mainloop()