# pip instal qrcode[pil]
import qrcode
data = " the text you wanna turn to QR code"
qr = qrcode.make(data)
qr.save("qrcode.png")
print("QR code created succesfully")
