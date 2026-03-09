# 🔳 QR Code Generator

A simple Windows desktop app that turns any URL into a QR code image — no setup, no hassle.

---

## ✨ Features

- 🖥️ Clean graphical interface — no command line needed
- ⚡ Instantly generates and saves QR codes as `.png` files
- 🏷️ Custom file naming for every QR code
- 📁 Files auto-saved to a dedicated output folder
- 📦 Runs as a standalone `.exe` — no Python or dependencies required

---

## 🚀 How to Use

1. **Double-click** `QRCodeGenerator.exe` to launch the app
2. **Enter the URL** you want to encode
3. **Give your file a name** (`.png` is added automatically if you skip it)
4. **Click "Generate QR Code"** — done! ✅

---

## 📂 Output Location

QR code images are saved to:

```
C:\DEV 204\QR Code Generator\QRCode Files\
```

> This folder is created automatically on first run — no need to set it up manually.

---

## ⚠️ Notes

- Both the **URL** and **file name** fields are required — the app will alert you if either is missing
- The `.png` extension is added automatically if you leave it out
- Any valid URL works: websites, social profiles, links, etc.

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [qrcode](https://pypi.org/project/qrcode/) — QR code generation
- [tkinter](https://docs.python.org/3/library/tkinter.html) — GUI
- [PyInstaller](https://pyinstaller.org/) — compiled to `.exe`