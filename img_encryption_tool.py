import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import random

# Global variable
image_path = ""


# Select Image
def select_image():
    global image_path
    image_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )

    if image_path:
        messagebox.showinfo("Success", "Image Selected Successfully")


# Encryption Function
def encrypt_image():
    global image_path

    if image_path == "":
        messagebox.showerror("Error", "Please select an image first")
        return

    try:
        key = int(key_entry.get())
    except:
        messagebox.showerror("Error", "Enter a valid numeric key")
        return

    img = Image.open(image_path)
    pixels = list(img.getdata())

    encrypted_pixels = []

    # Pixel value manipulation
    for r, g, b in pixels:
        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        encrypted_pixels.append((r, g, b))

    # Pixel shuffling
    random.seed(key)
    indices = list(range(len(encrypted_pixels)))
    random.shuffle(indices)

    shuffled_pixels = [encrypted_pixels[i] for i in indices]

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(shuffled_pixels)

    encrypted_img.save("encrypted_image.png")

    messagebox.showinfo("Success", "Image Encrypted!\nSaved as encrypted_image.png")


# Decryption Function
def decrypt_image():
    global image_path

    if image_path == "":
        messagebox.showerror("Error", "Please select encrypted image")
        return

    try:
        key = int(key_entry.get())
    except:
        messagebox.showerror("Error", "Enter a valid numeric key")
        return

    img = Image.open(image_path)
    pixels = list(img.getdata())

    random.seed(key)
    indices = list(range(len(pixels)))
    random.shuffle(indices)

    # Reverse shuffle
    unshuffled_pixels = [None] * len(pixels)

    for i, j in enumerate(indices):
        unshuffled_pixels[j] = pixels[i]

    decrypted_pixels = []

    # Reverse pixel manipulation
    for r, g, b in unshuffled_pixels:
        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256

        decrypted_pixels.append((r, g, b))

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)

    decrypted_img.save("decrypted_image.png")

    messagebox.showinfo("Success", "Image Decrypted!\nSaved as decrypted_image.png")


# GUI Window
window = tk.Tk()
window.title("Image Encryption Tool")
window.geometry("400x300")

title = tk.Label(
    window,
    text="Pixel Manipulation Image Encryption",
    font=("Arial", 14, "bold")
)
title.pack(pady=20)

select_btn = tk.Button(
    window,
    text="Select Image",
    command=select_image,
    width=20
)
select_btn.pack(pady=10)

key_label = tk.Label(window, text="Enter Secret Key")
key_label.pack()

key_entry = tk.Entry(window)
key_entry.pack(pady=5)

encrypt_btn = tk.Button(
    window,
    text="Encrypt Image",
    command=encrypt_image,
    width=20
)
encrypt_btn.pack(pady=10)

decrypt_btn = tk.Button(
    window,
    text="Decrypt Image",
    command=decrypt_image,
    width=20
)
decrypt_btn.pack(pady=10)

window.mainloop()