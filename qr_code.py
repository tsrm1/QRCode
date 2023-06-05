import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")


# qr = QRCode(box_size=2)
# qr.add_data('test text')
# qr.make()
# img = qr.make_image()
# img.save('qrcode_test2.png')