import qrcode

# qr = qrcode.make('hello world')
# qr.save('myQr.png')

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=15,
    border=5
)

data = 'https://vk.com/id362685172'
qr.add_data(data)
qr.make(fit=False)
img = qr.make_image(fill='black', back_color='white')
img.save('My VK.png')
