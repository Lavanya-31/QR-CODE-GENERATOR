import qrcode
import matplotlib.pyplot as plt
# Data to encode
data = "https://www.ieee.org//"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                     box_size=10,
				border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
					back_color = 'black')

img.save('MyQRCode.png')

print("QR code generated successfully for the provided URL.")
plt.imshow(img, cmap='gray')
