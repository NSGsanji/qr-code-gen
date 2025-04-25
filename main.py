import qrcode
from tkinter import *
from PIL import Image, ImageTk
import io

# khidki
root = Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.config(bg="#1e1e1e")

# label
Label(root, text="Enter text or URL", font=("Arial", 14), fg="white", bg="#1e1e1e").pack(pady=10)

# daanpatra
entry = Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# imglabel placeholder
img_label = Label(root, bg="#1e1e1e")
img_label.pack(pady=20)

# gen fn
def generate_qr():
    data = entry.get()
    if not data.strip():
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # img to photoimg
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    pil_img = Image.open(buffer)
    tk_img = ImageTk.PhotoImage(pil_img)

    # khidki mei dikhao
    img_label.config(image=tk_img)
    img_label.image = tk_img

    # sambhaal k rkho
    img.save("generated_qr.png")

# Button
Button(root, text="Generate QR", command=generate_qr, font=("Arial", 12),
       bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

# run
root.mainloop()
