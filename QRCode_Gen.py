import qrcode
import os
import tkinter as tk
from tkinter import messagebox

# Folder where images will be saved
folder_path = r"C:\DEV 204\QR Code Generator\QRCode Files"
os.makedirs(folder_path, exist_ok=True)

# Function to generate QR code
def generate_qr():
    url = url_entry.get()
    fileName = name_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL!")
        return

    if not fileName:
        messagebox.showerror("Error", "Please enter a file name!")
        return

    if not fileName.endswith(".png"):
        fileName += ".png"

    full_path = os.path.join(folder_path, fileName)

    try:
        img = qrcode.make(url)
        img.save(full_path)
        messagebox.showinfo("Success", f"QR code saved at:\n{full_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x200")
root.resizable(False, False)

# URL input
tk.Label(root, text="Enter URL:").pack(pady=(20,5))
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# File name input
tk.Label(root, text="Enter file name:").pack(pady=(10,5))
name_entry = tk.Entry(root, width=50)
name_entry.pack()

# Generate button
tk.Button(root, text="Generate QR Code", command=generate_qr, bg="green", fg="white").pack(pady=20)

root.mainloop()