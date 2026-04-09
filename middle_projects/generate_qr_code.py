import qrcode

qr = qrcode.QRCode(
    version=1,  # controls size (1–40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # size of each box
    border=4,  # thickness of border
)

qr.add_data("https://github.com/Kuba-Kuba-Mac/my_first_push")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("custom_qr.png")